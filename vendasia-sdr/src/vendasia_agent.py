# VendasIA Autonomous Agent - MVP Starter Code
# Week 1-2: Foundation that you can SELL for €199/month

import os
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import json

# pip install openai requests pandas python-dotenv
import openai
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# CONFIG
# =============================================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
INSTANTLY_API_KEY = os.getenv("INSTANTLY_API_KEY")

openai.api_key = OPENAI_API_KEY

# =============================================================================
# DATA MODELS
# =============================================================================

@dataclass
class Lead:
    """Representa um lead B2B"""
    company_name: str
    contact_name: str
    contact_email: str
    title: str
    linkedin_url: Optional[str]
    company_size: Optional[str]
    industry: Optional[str]
    location: str
    apollo_id: Optional[str] = None
    
    def to_dict(self):
        return {
            'company_name': self.company_name,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'title': self.title,
            'linkedin_url': self.linkedin_url,
            'company_size': self.company_size,
            'industry': self.industry,
            'location': self.location,
            'apollo_id': self.apollo_id
        }

@dataclass
class Research:
    """Research sobre uma empresa"""
    lead: Lead
    pain_points: List[str]
    personalization_hooks: List[str]
    lead_score: int  # 1-10
    reasoning: str

@dataclass
class Message:
    """Mensagem gerada pela IA"""
    lead: Lead
    content: str
    variant: str  # A, B, or C
    channel: str  # email or linkedin

# =============================================================================
# AGENT 1: LEAD FINDER
# =============================================================================

class LeadFinderAgent:
    """
    Encontra leads usando Apollo.io API
    
    Exemplo de uso:
    >>> finder = LeadFinderAgent()
    >>> leads = finder.find_leads(
    ...     industry="Software Development",
    ...     company_size="10-50",
    ...     location="Portugal"
    ... )
    """
    
    def __init__(self, api_key: str = APOLLO_API_KEY):
        self.api_key = api_key
        self.base_url = "https://api.apollo.io/v1"
    
    def find_leads(
        self,
        industry: str,
        company_size: str,
        location: str,
        titles: List[str] = ["CEO", "Founder", "Sales Director"],
        limit: int = 100
    ) -> List[Lead]:
        """
        Procura leads no Apollo.io
        
        Args:
            industry: Setor (e.g., "Software Development", "SaaS")
            company_size: Tamanho (e.g., "10-50", "51-200")
            location: Localização (e.g., "Portugal", "Lisbon")
            titles: Cargos alvo
            limit: Número máximo de leads
            
        Returns:
            Lista de objetos Lead
        """
        
        # Apollo.io API endpoint
        url = f"{self.base_url}/mixed_people/search"
        
        headers = {
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key
        }
        
        # Query payload
        payload = {
            "person_titles": titles,
            "organization_num_employees_ranges": [company_size],
            "organization_locations": [location],
            "q_organization_keyword_tags": [industry],
            "page": 1,
            "per_page": min(limit, 100)  # Apollo max 100 per page
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            
            leads = []
            for person in data.get("people", []):
                lead = Lead(
                    company_name=person.get("organization", {}).get("name", ""),
                    contact_name=person.get("name", ""),
                    contact_email=person.get("email", ""),
                    title=person.get("title", ""),
                    linkedin_url=person.get("linkedin_url"),
                    company_size=company_size,
                    industry=person.get("organization", {}).get("industry", ""),
                    location=location,
                    apollo_id=person.get("id")
                )
                leads.append(lead)
            
            print(f"✅ Found {len(leads)} leads from Apollo.io")
            return leads
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Apollo.io API error: {e}")
            return []

# =============================================================================
# AGENT 2: RESEARCH AGENT (SIMPLIFIED)
# =============================================================================

class ResearchAgent:
    """
    Faz research básico sobre cada lead usando GPT-4
    
    Nota: Versão MVP usa só o nome da empresa + setor.
    Versão avançada vai fazer web scraping.
    """
    
    def __init__(self, model: str = "gpt-4-turbo-preview"):
        self.model = model
    
    def research_lead(self, lead: Lead) -> Research:
        """
        Analisa um lead e identifica pain points
        
        Args:
            lead: Objeto Lead
            
        Returns:
            Objeto Research com insights
        """
        
        prompt = f"""
You are a B2B sales research expert.

Analyze this Portuguese company and identify likely pain points:

Company: {lead.company_name}
Industry: {lead.industry}
Size: {lead.company_size} employees
Contact: {lead.contact_name} - {lead.title}

Based on typical challenges for companies in this industry and size:

1. List 3 specific pain points they likely have (related to sales/lead generation)
2. Suggest 2 personalization hooks (based on industry trends)
3. Rate this lead 1-10 for VendasIA (AI sales automation tool)
4. Explain your reasoning

Respond in JSON format:
{{
  "pain_points": ["point1", "point2", "point3"],
  "personalization_hooks": ["hook1", "hook2"],
  "lead_score": 8,
  "reasoning": "explanation..."
}}
"""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a B2B research analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            
            research = Research(
                lead=lead,
                pain_points=result["pain_points"],
                personalization_hooks=result["personalization_hooks"],
                lead_score=result["lead_score"],
                reasoning=result["reasoning"]
            )
            
            print(f"✅ Researched {lead.company_name} - Score: {research.lead_score}/10")
            return research
            
        except Exception as e:
            print(f"❌ Research error for {lead.company_name}: {e}")
            # Return default research
            return Research(
                lead=lead,
                pain_points=["Manual lead qualification", "Time-consuming prospecting"],
                personalization_hooks=["Industry automation trends"],
                lead_score=5,
                reasoning="Default research due to API error"
            )

# =============================================================================
# AGENT 3: WRITER AGENT
# =============================================================================

class WriterAgent:
    """
    Escreve mensagens personalizadas usando GPT-4
    """
    
    def __init__(self, model: str = "gpt-4-turbo-preview"):
        self.model = model
    
    def generate_message(
        self,
        research: Research,
        channel: str = "email",
        variants: int = 3
    ) -> List[Message]:
        """
        Gera mensagens personalizadas
        
        Args:
            research: Objeto Research com insights
            channel: "email" ou "linkedin"
            variants: Número de variantes (A/B testing)
            
        Returns:
            Lista de objetos Message
        """
        
        lead = research.lead
        
        if channel == "linkedin":
            max_length = 300
            message_type = "LinkedIn connection message"
        else:
            max_length = 150
            message_type = "Email subject line + first line"
        
        prompt = f"""
You are an expert B2B copywriter for Portuguese market.

Write {variants} variants of a {message_type} for:

Company: {lead.company_name}
Contact: {lead.contact_name}, {lead.title}
Industry: {lead.industry}

Research insights:
- Pain points: {', '.join(research.pain_points[:2])}
- Hooks: {', '.join(research.personalization_hooks)}

Requirements:
1. Max {max_length} characters
2. Reference something SPECIFIC (not generic)
3. Natural Portuguese from Portugal (não do Brasil)
4. Soft CTA, not pushy
5. NO "Espero que esteja bem" or similar

Generate {variants} variants:
- Variant A: Direct value proposition
- Variant B: Question-based hook  
- Variant C: Insight/statistic approach

Respond in JSON:
{{
  "messages": [
    {{"variant": "A", "content": "..."}},
    {{"variant": "B", "content": "..."}},
    {{"variant": "C", "content": "..."}}
  ]
}}
"""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a Portuguese B2B copywriter."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,  # Higher for creativity
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            
            messages = []
            for msg in result["messages"]:
                message = Message(
                    lead=lead,
                    content=msg["content"],
                    variant=msg["variant"],
                    channel=channel
                )
                messages.append(message)
            
            print(f"✅ Generated {len(messages)} messages for {lead.company_name}")
            return messages
            
        except Exception as e:
            print(f"❌ Message generation error: {e}")
            return []

# =============================================================================
# AGENT 4: SENDER AGENT (SIMPLIFIED)
# =============================================================================

class SenderAgent:
    """
    Envia emails usando Instantly.ai
    
    Nota: LinkedIn automation requer Phantombuster (setup separado)
    """
    
    def __init__(self, api_key: str = INSTANTLY_API_KEY):
        self.api_key = api_key
        self.base_url = "https://api.instantly.ai/api/v1"
    
    def send_email(
        self,
        message: Message,
        from_email: str,
        subject: str = None
    ) -> bool:
        """
        Envia email via Instantly.ai
        
        Args:
            message: Objeto Message
            from_email: Email remetente (deve estar configurado no Instantly)
            subject: Assunto (se None, usa primeira linha do content)
            
        Returns:
            True se enviado, False se erro
        """
        
        if not subject:
            # Use first line as subject
            lines = message.content.split('\n')
            subject = lines[0] if lines else "Regarding VendasIA"
        
        url = f"{self.base_url}/lead/add"
        
        payload = {
            "api_key": self.api_key,
            "campaign_id": "YOUR_CAMPAIGN_ID",  # Configure no Instantly.ai
            "email": message.lead.contact_email,
            "first_name": message.lead.contact_name.split()[0],
            "last_name": " ".join(message.lead.contact_name.split()[1:]),
            "company_name": message.lead.company_name,
            "personalization": {
                "custom_message": message.content
            }
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            print(f"✅ Email sent to {message.lead.contact_email}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Email send error: {e}")
            return False

# =============================================================================
# ORCHESTRATOR (Main Pipeline)
# =============================================================================

class VendasIAOrchestrator:
    """
    Orquestra todos os agentes num pipeline completo
    """
    
    def __init__(self):
        self.lead_finder = LeadFinderAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.sender = SenderAgent()
    
    def run_full_pipeline(
        self,
        icp_criteria: Dict[str, str],
        limit: int = 10,
        send_emails: bool = False
    ):
        """
        Executa pipeline completo: Find → Research → Write → Send
        
        Args:
            icp_criteria: Dict com industry, company_size, location, titles
            limit: Número de leads a processar
            send_emails: Se True, envia emails (cuidado!)
            
        Returns:
            DataFrame com resultados
        """
        
        print("\n" + "="*70)
        print("🚀 VendasIA Autonomous Agent - Starting Pipeline")
        print("="*70 + "\n")
        
        # Step 1: Find Leads
        print("📍 Step 1: Finding leads with Apollo.io...")
        leads = self.lead_finder.find_leads(
            industry=icp_criteria.get("industry", "Software"),
            company_size=icp_criteria.get("company_size", "10-50"),
            location=icp_criteria.get("location", "Portugal"),
            titles=icp_criteria.get("titles", ["CEO", "Founder"]),
            limit=limit
        )
        
        if not leads:
            print("❌ No leads found. Check your Apollo.io API key and criteria.")
            return None
        
        # Step 2: Research each lead
        print(f"\n🔍 Step 2: Researching {len(leads)} leads...")
        researches = []
        for lead in leads:
            research = self.researcher.research_lead(lead)
            researches.append(research)
        
        # Filter by score (only 7+)
        high_quality = [r for r in researches if r.lead_score >= 7]
        print(f"✅ Found {len(high_quality)} high-quality leads (score ≥7)")
        
        # Step 3: Generate messages
        print(f"\n✍️ Step 3: Generating personalized messages...")
        all_messages = []
        for research in high_quality:
            messages = self.writer.generate_message(research, channel="email")
            all_messages.extend(messages)
        
        # Step 4: Send (optional)
        if send_emails and all_messages:
            print(f"\n📧 Step 4: Sending {len(all_messages)} emails...")
            for message in all_messages:
                if message.variant == "A":  # Only send variant A in MVP
                    self.sender.send_email(
                        message,
                        from_email="your-email@domain.com"  # Configure
                    )
        else:
            print(f"\n📧 Step 4: Skipping email send (send_emails=False)")
        
        # Step 5: Save results
        print(f"\n💾 Step 5: Saving results...")
        results = []
        for research in high_quality:
            # Find messages for this lead
            lead_messages = [m for m in all_messages if m.lead == research.lead]
            
            results.append({
                'company': research.lead.company_name,
                'contact': research.lead.contact_name,
                'email': research.lead.contact_email,
                'title': research.lead.title,
                'score': research.lead_score,
                'pain_points': ', '.join(research.pain_points),
                'message_a': lead_messages[0].content if len(lead_messages) > 0 else '',
                'message_b': lead_messages[1].content if len(lead_messages) > 1 else '',
                'message_c': lead_messages[2].content if len(lead_messages) > 2 else '',
            })
        
        df = pd.DataFrame(results)
        
        # Save to CSV
        filename = f"vendasia_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        
        print(f"\n✅ Results saved to {filename}")
        print("\n" + "="*70)
        print(f"🎉 Pipeline complete! Processed {len(leads)} leads, found {len(high_quality)} qualified")
        print("="*70 + "\n")
        
        return df

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    
    # Define your ICP (Ideal Customer Profile)
    icp = {
        "industry": "Software Development",
        "company_size": "11-50",  # Apollo format: 11-50, 51-200, etc.
        "location": "Portugal",
        "titles": ["CEO", "Founder", "Sales Director", "Head of Sales"]
    }
    
    # Initialize orchestrator
    agent = VendasIAOrchestrator()
    
    # Run pipeline (test with 5 leads first!)
    results = agent.run_full_pipeline(
        icp_criteria=icp,
        limit=5,  # Start small!
        send_emails=False  # Set True when ready to send
    )
    
    # View results
    if results is not None:
        print("\n📊 Results Preview:")
        print(results[['company', 'contact', 'score', 'message_a']].head())
        
        print("\n🎯 Next Steps:")
        print("1. Review the generated messages in the CSV")
        print("2. If quality is good, increase limit to 50-100")
        print("3. Set send_emails=True to start outreach")
        print("4. Monitor replies and optimize prompts")
