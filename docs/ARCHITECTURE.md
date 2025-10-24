# VendasIA 2.0 - Autonomous SDR Agent Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SALES PERSON INTERFACE                          │
│                    (Next.js Dashboard - Vercel)                         │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Define   │  │ Monitor  │  │ Review   │  │ Close    │              │
│  │ ICP      │  │ Pipeline │  │ Hot      │  │ Deals    │              │
│  │          │  │          │  │ Leads    │  │          │              │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↕ REST API
┌─────────────────────────────────────────────────────────────────────────┐
│                     ORCHESTRATION LAYER                                 │
│                  (LangGraph Multi-Agent System)                         │
│                                                                         │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐   │
│  │  Lead     │ →  │ Research  │ →  │  Writer   │ →  │  Sender   │   │
│  │  Finder   │    │  Agent    │    │  Agent    │    │  Agent    │   │
│  │  Agent    │    │           │    │           │    │           │   │
│  └───────────┘    └───────────┘    └───────────┘    └───────────┘   │
│       ↓                ↓                 ↓                 ↓          │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                Response Handler Agent                         │   │
│  │         (Monitors replies, qualifies, escalates)              │   │
│  └───────────────────────────────────────────────────────────────┘   │
│       ↓                                                                │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                  CRM Manager Agent                            │   │
│  │            (Syncs everything to Pipedrive)                    │   │
│  └───────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↕
┌─────────────────────────────────────────────────────────────────────────┐
│                         AI & DATA LAYER                                 │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ OpenAI   │  │ Anthropic│  │ Pinecone │  │ LangChain│              │
│  │ GPT-4    │  │ Claude   │  │ Vectors  │  │ RAG      │              │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↕
┌─────────────────────────────────────────────────────────────────────────┐
│                      EXTERNAL SERVICES LAYER                            │
│                                                                         │
│  Data Sources:        Outreach:           CRM:                         │
│  ┌────────────┐      ┌────────────┐      ┌────────────┐              │
│  │ Apollo.io  │      │Phantombuster│     │ Pipedrive  │              │
│  │ Hunter.io  │      │Instantly.ai │     │ HubSpot    │              │
│  │ Clearbit   │      │ Lemlist     │     │ Salesforce │              │
│  │ Firecrawl  │      │ Waalaxy     │     │            │              │
│  │ SerpAPI    │      └────────────┘      └────────────┘              │
│  └────────────┘                                                        │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↕
┌─────────────────────────────────────────────────────────────────────────┐
│                       BACKEND INFRASTRUCTURE                            │
│                     (FastAPI + PostgreSQL + Redis)                      │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │
│  │  PostgreSQL  │  │    Redis     │  │   Celery     │                │
│  │  (Leads DB)  │  │   (Cache)    │  │ (Task Queue) │                │
│  └──────────────┘  └──────────────┘  └──────────────┘                │
│                                                                         │
│                     Hosted on Railway/Render                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 End-to-End Flow (Detailed)

### Phase 1: Lead Discovery (Daily @ 9 AM)
```
1. Lead Finder Agent wakes up
2. Queries Apollo.io API with ICP criteria
3. Gets 100 companies matching profile
4. Enriches with Hunter.io (emails)
5. Stores in PostgreSQL `leads` table
6. Triggers Research Agent for each lead
```

### Phase 2: Deep Research (Parallel Processing)
```
For each lead (Celery async tasks):
1. Firecrawl scrapes company website
2. SerpAPI searches recent news/funding
3. Claude analyzes LinkedIn profile
4. GPT-4 synthesizes into:
   - Company description
   - Recent events
   - Identified pain points
   - Personalization hooks
5. Creates embeddings → Pinecone
6. Stores research → PostgreSQL
7. Triggers Writer Agent
```

### Phase 3: Message Generation
```
Writer Agent (GPT-4):
1. Retrieves lead + research from DB
2. Queries Pinecone for similar successful messages (RAG)
3. Generates 3 message variants (A/B/C testing)
4. Stores in `messages` table
5. Triggers Sender Agent
```

### Phase 4: Multi-Channel Outreach
```
Sender Agent:
1. Checks optimal send time (Tue-Thu, 9-11 AM)
2. If LinkedIn:
   - Phantombuster API sends connection request
   - Schedules follow-up message (Day +3)
3. If Email:
   - Instantly.ai API sends via warmed domain
   - Sets up sequence (Day 1, 5, 8)
4. Logs activity in CRM
5. Sets up Response Monitor
```

### Phase 5: Response Handling (Real-time)
```
Response Handler Agent (webhook-triggered):
1. Receives reply (LinkedIn/Email webhook)
2. GPT-4 classifies:
   - Sentiment (positive/neutral/negative)
   - Intent (interested/not interested/question)
   - BANT score (0-10)
3. Decision tree:
   - If BANT ≥ 7: Notify sales person + propose meeting
   - If 4-6: Send nurture content
   - If <4: Mark as cold, stop outreach
4. Generates AI response (if appropriate)
5. Updates CRM stage
```

### Phase 6: CRM Sync (Continuous)
```
CRM Manager Agent:
1. Every action creates Pipedrive activity
2. Lead states mapped to Deal stages:
   - New Lead → "Prospecting"
   - Contacted → "Outreach"
   - Replied → "Engaged"
   - BANT ≥7 → "Qualified"
   - Meeting booked → "Demo Scheduled"
3. Dashboard updates in real-time
```

---

## 🗄️ Database Schema

```sql
-- Core tables
CREATE TABLE leads (
    id UUID PRIMARY KEY,
    company_name VARCHAR(255),
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_linkedin VARCHAR(255),
    title VARCHAR(255),
    company_size VARCHAR(50),
    industry VARCHAR(100),
    location VARCHAR(100),
    apollo_id VARCHAR(100),
    created_at TIMESTAMP,
    status VARCHAR(50),  -- new, researched, contacted, replied, qualified, closed
    pipedrive_deal_id INT
);

CREATE TABLE research (
    id UUID PRIMARY KEY,
    lead_id UUID REFERENCES leads(id),
    website_content TEXT,
    recent_news TEXT,
    linkedin_summary TEXT,
    pain_points JSONB,  -- ["pain1", "pain2", "pain3"]
    personalization_hooks JSONB,
    company_description TEXT,
    embedding_id VARCHAR(255),  -- Pinecone ID
    created_at TIMESTAMP
);

CREATE TABLE messages (
    id UUID PRIMARY KEY,
    lead_id UUID REFERENCES leads(id),
    channel VARCHAR(50),  -- linkedin, email
    variant VARCHAR(10),  -- A, B, C
    content TEXT,
    sent_at TIMESTAMP,
    opened_at TIMESTAMP,
    replied_at TIMESTAMP,
    reply_content TEXT,
    bant_score INT,  -- 0-10
    sentiment VARCHAR(50),  -- positive, neutral, negative
    created_at TIMESTAMP
);

CREATE TABLE sequences (
    id UUID PRIMARY KEY,
    lead_id UUID REFERENCES leads(id),
    channel VARCHAR(50),
    step_number INT,
    scheduled_at TIMESTAMP,
    executed_at TIMESTAMP,
    status VARCHAR(50),  -- pending, sent, skipped
    message_id UUID REFERENCES messages(id)
);

CREATE TABLE icp_profiles (
    id UUID PRIMARY KEY,
    user_id UUID,
    name VARCHAR(255),  -- "Portuguese SaaS Companies"
    criteria JSONB,  -- {"industry": "SaaS", "size": "10-50", ...}
    active BOOLEAN,
    created_at TIMESTAMP
);

CREATE TABLE performance_metrics (
    id UUID PRIMARY KEY,
    date DATE,
    leads_found INT,
    messages_sent INT,
    open_rate DECIMAL(5,2),
    reply_rate DECIMAL(5,2),
    meeting_rate DECIMAL(5,2),
    channel VARCHAR(50),
    variant VARCHAR(10)
);
```

---

## 🧠 Agent Prompts (Examples)

### Lead Finder Agent
```python
LEAD_FINDER_PROMPT = """
You are a lead discovery agent for VendasIA.

Current ICP:
{icp_criteria}

Your task:
1. Query Apollo.io with these exact criteria
2. Filter results to only Portuguese companies
3. Prioritize companies with:
   - Recent funding/growth
   - Active LinkedIn presence
   - Technology stack match
4. Return top 100 leads as JSON

Output format:
[
  {
    "company": "...",
    "contact_name": "...",
    "email": "...",
    "title": "...",
    "priority_score": 8
  }
]
"""
```

### Research Agent
```python
RESEARCH_PROMPT = """
You are a deep research agent. Analyze this B2B company:

Company: {company_name}
Website: {website_url}
Recent news: {news_summary}
LinkedIn: {linkedin_data}

Tasks:
1. Identify 3 specific pain points they likely have
2. Find 2-3 personalization hooks (recent events, achievements, changes)
3. Assess buying intent signals (hiring SDRs? Growing fast? Recent funding?)
4. Rate lead quality 1-10

Output JSON:
{
  "pain_points": ["...", "...", "..."],
  "personalization_hooks": ["...", "..."],
  "buying_signals": ["..."],
  "lead_score": 8,
  "reasoning": "..."
}
"""
```

### Writer Agent
```python
WRITER_PROMPT = """
You are an expert B2B outreach copywriter.

Lead context:
- Name: {contact_name}
- Title: {title}
- Company: {company_name}
- Industry: {industry}

Research insights:
{research_summary}

Write a LinkedIn connection message (max 300 chars) that:
1. References something SPECIFIC about their company (from research)
2. Hints at a pain point without being pushy
3. Has a soft CTA (not "book a call")
4. Sounds natural, Portuguese from Portugal
5. NO generic openers like "Espero que esteja bem"

Generate 3 variants (A/B/C testing):
- Variant A: Direct value proposition
- Variant B: Question-based hook
- Variant C: Insight/observation approach

Output JSON with 3 messages.
"""
```

### Response Handler Agent
```python
RESPONSE_HANDLER_PROMPT = """
You are a conversation AI for VendasIA.

Lead replied to outreach:
Original message: {original_message}
Their reply: {reply_content}

Tasks:
1. Classify sentiment: positive/neutral/negative
2. Extract BANT signals:
   - Budget: Do they mention cost/ROI?
   - Authority: Are they decision maker?
   - Need: Do they confirm pain point?
   - Timeline: Any urgency signals?
3. Calculate BANT score 0-10
4. Decide next action:
   - If score ≥7: Propose meeting
   - If 4-6: Share case study
   - If <4: Polite close
5. Draft response (if appropriate)

Output JSON with classification + suggested response.
"""
```

---

## 🔧 Key Technologies & Costs

### AI & ML
- **OpenAI GPT-4**: $20-30/1M tokens (~€100/month for 5000 leads)
- **Anthropic Claude**: $15/1M tokens (research backup)
- **Pinecone**: $70/month (100k vectors, 1-pod)
- **LangChain**: Free (open source)

### Data & Enrichment
- **Apollo.io**: $99/month (5000 credits)
- **Hunter.io**: $49/month (10k searches)
- **Clearbit**: $99/month (Reveal)
- **Firecrawl**: $29/month (1000 scrapes)

### Outreach
- **Phantombuster**: $59/month (LinkedIn automation)
- **Instantly.ai**: $97/month (1000 emails/day)
- **Lemlist**: Alternative ~$59/month

### CRM & Tools
- **Pipedrive**: $14/user/month
- **Railway**: $20/month (hosting)
- **Vercel**: Free (frontend)

**Total Monthly Cost**: ~€600-700/month
**Target Price**: €499/month (Professional plan)
**Margin**: Break-even at 2 customers, profit at 3+

---

## 📊 Success Metrics

### Agent Performance
- **Lead Discovery**: 100 qualified leads/day
- **Research Quality**: 90%+ accuracy on pain points
- **Message Quality**: <5% spam reports, >15% open rate
- **Response Rate**: 25%+ (vs 5% industry average)
- **Meeting Conversion**: 20% of positive replies

### Business Metrics
- **CAC**: €50 (mostly ads for dashboard access)
- **LTV**: €5,988 (€499/month × 12 months average)
- **Payback Period**: <1 month
- **Churn**: <10% monthly (high value, hard to replace)

### Technical Metrics
- **Uptime**: 99.9% (Railway SLA)
- **API Latency**: <2s average
- **Agent Execution Time**: <5 min per lead (research → message)
- **Daily Processing**: 500-1000 leads

---

## 🚀 MVP Implementation Priority

### Week 1-2: Foundation (Can Sell!)
```
✅ Apollo.io integration (lead finder)
✅ GPT-4 basic message generation
✅ Instantly.ai email sending
✅ Google Sheets as CRM (temporary)
✅ Manual trigger for each step

= Sellable as "AI-assisted outreach" for €199/month
```

### Week 3-4: Automation
```
✅ LangChain agents (research + writer)
✅ Celery task queue (async processing)
✅ Firecrawl web scraping
✅ Pipedrive integration
✅ Basic sequencing

= Sellable as "Semi-autonomous SDR" for €299/month
```

### Week 5-6: Intelligence
```
✅ Pinecone embeddings (RAG)
✅ Response classification
✅ BANT auto-scoring
✅ Multi-channel (LinkedIn + Email)

= Sellable as "Autonomous SDR" for €499/month
```

### Week 7-8: Polish
```
✅ Next.js dashboard
✅ Real-time metrics
✅ A/B testing
✅ Performance optimization

= Full product! Target €499-999/month
```

---

## 🎯 Go-to-Market Strategy

### Phase 1: Beta (Week 1-4)
- **Target**: 5 beta customers @ €99/month
- **Offer**: "Help us test, 50% off forever"
- **Channel**: Direct LinkedIn outreach (ironic!)
- **Goal**: Validate tech + get testimonials

### Phase 2: Launch (Week 5-8)
- **Target**: 20 customers @ €299/month = €5,980 MRR
- **Offer**: Early bird pricing
- **Channel**: LinkedIn ads + content
- **Goal**: Prove product-market fit

### Phase 3: Scale (Month 3-6)
- **Target**: 100 customers @ €499/month = €49,900 MRR
- **Channel**: Partnerships (sales agencies), SEO, referrals
- **Goal**: Default alive, hire first employee

### Phase 4: Dominate (Month 6-12)
- **Target**: 500+ customers, €250k+ MRR
- **Channel**: Enterprise deals, resellers
- **Goal**: Raise seed round or stay bootstrapped

---

## 💡 Competitive Advantages

### vs. Apollo/ZoomInfo
- ❌ They: Just data, you do outreach
- ✅ Us: Data + AI writes + AI sends + AI qualifies

### vs. Instantly/Lemlist
- ❌ They: Email tool, you write messages
- ✅ Us: Full autonomous agent, we write messages

### vs. Clay
- ❌ They: Enrichment + workflows, still manual
- ✅ Us: 100% autonomous, zero manual work

### vs. 11x.ai / Artisan
- ❌ They: US market, English only, $$$
- ✅ Us: Portuguese market, 1/3 the price

**Key Differentiator**: We're the ONLY fully autonomous SDR in Portuguese! 🇵🇹

---

## 🔐 Risk Mitigation

### Technical Risks
- **API rate limits**: Use multiple accounts, rotate proxies
- **AI accuracy**: Human review for first 100 messages, improve prompts
- **Email deliverability**: Warm-up domains, multiple senders, DKIM/SPF

### Business Risks
- **LinkedIn bans**: Use Phantombuster limits, add delays, rotate accounts
- **Compliance (GDPR)**: Only B2B data, opt-out links, legitimate interest
- **Competition**: Move fast, build moat with Portuguese training data

### Market Risks
- **Recession**: SDRs are first to get cut → our automation is cheaper
- **AI hype crash**: We deliver ROI, not just hype
- **Platform changes**: Diversify channels, own the relationship

---

## 📈 Unit Economics (at Scale)

### Per Customer (€499/month plan)
```
Revenue:                    €499/month
Costs:
  - AI (GPT-4 + Claude):    -€50
  - Data (Apollo/Hunter):   -€30
  - Outreach (Instantly):   -€20
  - Infrastructure:         -€10
  - Support (10% time):     -€50
  --------------------------------
  Gross Margin:             €339 (68%)
```

### At 100 Customers
```
MRR:                        €49,900
Gross Profit:               €33,900/month
Operating Costs:
  - Founder salary:         -€5,000
  - Developer:              -€4,000
  - Customer Success:       -€3,000
  - Marketing:              -€5,000
  - Other:                  -€2,000
  --------------------------------
  Net Profit:               €14,900/month (~30% margin)
```

**Break-even**: 25 customers (~€12,500 MRR)
**Comfortable**: 50 customers (~€25k MRR)
**Scaling**: 100+ customers (hire team, raise funding)

---

## 🎓 Learning Resources

### LangGraph / Agents
- https://langchain-ai.github.io/langgraph/
- https://github.com/langchain-ai/langgraph-example
- https://www.youtube.com/watch?v=XXXXXXX (Multi-agent tutorial)

### Sales Automation
- https://www.apollo.io/api
- https://instantly.ai/developers
- https://www.phantombuster.com/automations

### Vector Databases
- https://docs.pinecone.io/docs/quickstart
- https://python.langchain.com/docs/integrations/vectorstores/pinecone

---

**Next**: Want me to create the actual Python code for the first agent? 🚀
