"""
VendasIA - 100% FREE MVP com Google Gemini
===========================================

Stack 100% GRÁTIS:
- AI: Google Gemini (1.5M tokens/mês grátis)
- Email: Gmail SMTP (500/dia grátis)
- Data: Manual CSV scraping

Custo: €0/mês
Dura: MESES
"""

import google.generativeai as genai
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json
import time
from datetime import datetime
from typing import Dict, List
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiAgent:
    """AI Agent usando Google Gemini (GRÁTIS!)"""
    
    def __init__(self):
        # Configure Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY not found in .env file!")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini initialized (FREE forever!)")
    
    def research_company(self, company: str, title: str, industry: str = "SaaS") -> Dict:
        """
        Pesquisa empresa e identifica pain points
        
        GRÁTIS: 1,500 calls/dia
        """
        
        prompt = f"""
Analisa esta empresa portuguesa B2B:

**Empresa**: {company}
**Setor**: {industry}
**Cargo do contacto**: {title}

**Tarefa**:
1. Identifica 3 pain points específicos que esta empresa provavelmente tem relacionados com vendas/lead generation
2. Sugere 1 hook de personalização baseado no setor
3. Avalia probabilidade de interesse em automação de vendas (score 1-10)
4. Explica o reasoning

**IMPORTANTE**: Responde APENAS com JSON válido, sem markdown, sem explicações extra:

{{
  "pain_points": [
    "Pain point específico 1",
    "Pain point específico 2",
    "Pain point específico 3"
  ],
  "hook": "Hook de personalização específico para {company}",
  "lead_score": 8,
  "reasoning": "Porque esta empresa provavelmente precisa disto..."
}}
"""
        
        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            # Remove markdown se existir
            if text.startswith('```'):
                text = text.split('```')[1]
                if text.startswith('json'):
                    text = text[4:]
            
            data = json.loads(text.strip())
            
            # Add metadata
            data['company'] = company
            data['researched_at'] = datetime.now().isoformat()
            
            return data
        
        except Exception as e:
            print(f"⚠️ Error researching {company}: {e}")
            return {
                "company": company,
                "pain_points": ["Crescimento lento", "Leads de baixa qualidade", "Falta de automação"],
                "hook": f"crescimento em {industry}",
                "lead_score": 5,
                "reasoning": "Fallback devido a erro"
            }
    
    def write_linkedin_message(self, name: str, company: str, hook: str) -> str:
        """
        Escreve mensagem LinkedIn curta e personalizada
        
        GRÁTIS: 1,500 calls/dia
        """
        
        prompt = f"""
Escreve uma mensagem LinkedIn CURTA e DIRETA para:

**Nome**: {name}
**Empresa**: {company}
**Hook de personalização**: {hook}

**Regras ESTRITAS**:
- Máximo 120 caracteres (SUPER CURTO!)
- Português de Portugal natural
- Menciona o hook subtilmente
- CTA simples: "Vale conversar?" ou similar
- SEM "Espero que esteja bem"
- SEM "Prezado/a"
- SEM fluff, direto ao ponto
- Tom casual mas profissional

**Responde APENAS com a mensagem, sem aspas, sem markdown, sem explicações.**
"""
        
        try:
            response = self.model.generate_content(prompt)
            message = response.text.strip()
            
            # Remove quotes se existirem
            message = message.strip('"\'')
            
            return message
        
        except Exception as e:
            print(f"⚠️ Error writing message: {e}")
            return f"Olá {name}, vi o trabalho da {company}. Vale conversar sobre automação de vendas?"


class FreeEmailSender:
    """Gmail SMTP - 500 emails/dia GRÁTIS"""
    
    def __init__(self):
        self.smtp_host = 'smtp.gmail.com'
        self.smtp_port = 587
        self.from_email = os.getenv('GMAIL_ADDRESS')
        self.app_password = os.getenv('GMAIL_APP_PASSWORD')
        
        if not self.from_email or not self.app_password:
            print("⚠️ Gmail credentials not found. Email sending disabled.")
            print("   Get app password: https://myaccount.google.com/apppasswords")
            self.enabled = False
        else:
            self.enabled = True
            print(f"✅ Gmail SMTP ready: {self.from_email} (500 emails/day FREE)")
    
    def send(self, to: str, subject: str, body: str) -> bool:
        """
        Envia email via Gmail SMTP
        
        FREE: 500 emails/dia
        """
        
        if not self.enabled:
            print(f"📧 [DRY RUN] Email to {to}: {subject}")
            return False
        
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_email
            msg['To'] = to
            
            # Plain text
            text_part = MIMEText(body, 'plain')
            msg.attach(text_part)
            
            # Connect and send
            smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)
            smtp.starttls()
            smtp.login(self.from_email, self.app_password)
            smtp.send_message(msg)
            smtp.quit()
            
            print(f"✅ Email sent to {to}")
            return True
        
        except Exception as e:
            print(f"❌ Failed to send to {to}: {e}")
            return False


class FreeVendasIAOrchestrator:
    """
    Orchestrator 100% GRÁTIS
    
    Custos:
    - Gemini: €0 (1.5M tokens/mês)
    - Gmail: €0 (500 emails/dia)
    - Data: €0 (manual scraping)
    
    TOTAL: €0/mês
    """
    
    def __init__(self):
        self.agent = GeminiAgent()
        self.sender = FreeEmailSender()
        print("\n🎉 VendasIA FREE MVP initialized!")
        print("💰 Cost: €0/month")
        print("⏰ Limits: 1,500 leads/day, 500 emails/day")
        print()
    
    def process_leads(self, csv_path: str, limit: int = 10, send_emails: bool = False):
        """
        Processa leads do CSV manual
        
        Args:
            csv_path: Path para CSV com colunas: name, company, title, linkedin_url, email_guess
            limit: Quantos leads processar (default 10 para teste)
            send_emails: Se True, envia emails via Gmail (max 500/dia)
        """
        
        print(f"📂 Loading leads from {csv_path}...")
        
        try:
            df = pd.read_csv(csv_path)
            print(f"✅ Loaded {len(df)} leads")
        except FileNotFoundError:
            print(f"❌ File not found: {csv_path}")
            print("   Create it with columns: name,company,title,linkedin_url,email_guess")
            return
        
        # Validate columns
        required = ['name', 'company', 'title']
        if not all(col in df.columns for col in required):
            print(f"❌ CSV must have columns: {required}")
            return
        
        # Process leads
        results = []
        leads_to_process = df.head(limit)
        
        print(f"\n🚀 Processing {len(leads_to_process)} leads...\n")
        
        for idx, lead in leads_to_process.iterrows():
            print(f"[{idx+1}/{len(leads_to_process)}] 🔍 {lead['company']}...")
            
            # 1. Research com Gemini (GRÁTIS)
            research = self.agent.research_company(
                company=lead['company'],
                title=lead['title']
            )
            
            print(f"   Score: {research['lead_score']}/10")
            print(f"   Hook: {research['hook']}")
            
            # 2. Write message com Gemini (GRÁTIS)
            message = self.agent.write_linkedin_message(
                name=lead['name'],
                company=lead['company'],
                hook=research['hook']
            )
            
            print(f"   Message: \"{message}\"")
            
            # 3. Send email se habilitado (GRÁTIS - 500/dia)
            email_sent = False
            if send_emails and 'email_guess' in lead and pd.notna(lead['email_guess']):
                email_sent = self.sender.send(
                    to=lead['email_guess'],
                    subject=f"Quick question - {lead['company']}",
                    body=f"Olá {lead['name']},\n\n{message}\n\nAbraço,\nTomás"
                )
            
            # 4. Save results
            results.append({
                'name': lead['name'],
                'company': lead['company'],
                'title': lead['title'],
                'linkedin_url': lead.get('linkedin_url', ''),
                'email_guess': lead.get('email_guess', ''),
                'lead_score': research['lead_score'],
                'pain_points': ' | '.join(research['pain_points']),
                'hook': research['hook'],
                'message': message,
                'email_sent': email_sent,
                'processed_at': datetime.now().isoformat()
            })
            
            print()
            
            # Rate limiting (Gemini: 15 requests/min)
            time.sleep(4)  # ~15 leads/min
        
        # 5. Save to CSV
        output_file = f"vendasia_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_file, index=False)
        
        print(f"\n🎉 DONE! Results saved to: {output_file}")
        print(f"\n📊 SUMMARY:")
        print(f"   Total processed: {len(results)}")
        print(f"   Avg score: {results_df['lead_score'].mean():.1f}/10")
        print(f"   High quality (≥7): {len(results_df[results_df['lead_score'] >= 7])}")
        print(f"   Emails sent: {sum(results_df['email_sent'])}")
        print(f"\n💰 Cost: €0")
        print(f"⏰ Limits remaining today:")
        print(f"   Gemini: {1500 - len(results)} requests")
        print(f"   Gmail: {500 - sum(results_df['email_sent'])} emails")


# Example usage
if __name__ == '__main__':
    """
    QUICKSTART:
    
    1. Get Gemini API key:
       https://makersuite.google.com/app/apikey
    
    2. Create .env file:
       GEMINI_API_KEY=AIza...
       GMAIL_ADDRESS=teu@gmail.com
       GMAIL_APP_PASSWORD=abcd efgh ijkl mnop
    
    3. Create leads-manual.csv:
       name,company,title,linkedin_url,email_guess
       João Silva,TechCorp,CEO,linkedin.com/in/joao,joao@techcorp.pt
       Maria Santos,SaaSPT,Founder,linkedin.com/in/maria,maria@saaspt.com
    
    4. Run:
       python src/vendasia_free_agent.py
    
    5. Profit! 🚀
    """
    
    # Initialize orchestrator
    orchestrator = FreeVendasIAOrchestrator()
    
    # Process 10 test leads (no emails sent)
    orchestrator.process_leads(
        csv_path='leads-manual.csv',
        limit=10,
        send_emails=False  # Change to True when ready
    )
    
    print("\n✨ Next steps:")
    print("   1. Review vendasia_results_*.csv")
    print("   2. Check message quality")
    print("   3. If good, increase limit to 50")
    print("   4. Enable send_emails=True")
    print("   5. Send 20-50 per day to avoid spam flags")
    print("\n💪 Boa sorte!")
