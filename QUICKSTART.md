# VendasIA - Quick Start Guide

## 🚀 Setup (10 minutos)

### 1. Install Python Dependencies
```bash
cd /Users/tomasbatalha/Projects/vendas-ia
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Get API Keys

#### OpenAI (€5 credit)
1. Go to https://platform.openai.com/signup
2. Add payment method
3. Create API key: https://platform.openai.com/api-keys
4. Copy key starting with `sk-proj-...`

#### Apollo.io (Free trial)
1. Sign up: https://app.apollo.io/sign-up
2. Go to Settings → Integrations → API
3. Generate API key
4. Free tier: 50 credits/month (50 leads)

#### Instantly.ai (€97/month, start trial)
1. Sign up: https://instantly.ai
2. Settings → API → Generate key
3. Create a campaign first!
4. Optional for MVP (can skip initially)

### 3. Configure Environment
```bash
# Copy example to real .env
cp .env.example .env

# Edit .env with your keys
nano .env
```

Paste your keys:
```
OPENAI_API_KEY=sk-proj-abc123...
APOLLO_API_KEY=your-apollo-key...
INSTANTLY_API_KEY=your-instantly-key...  # Optional
```

### 4. Test Run
```bash
# Activate venv if not already
source venv/bin/activate

# Run with 5 test leads (NO emails sent)
python src/vendasia_agent.py
```

Expected output:
```
🚀 VendasIA Autonomous Agent - Starting Pipeline
📍 Step 1: Finding leads with Apollo.io...
✅ Found 5 leads from Apollo.io

🔍 Step 2: Researching 5 leads...
✅ Researched Empresa A - Score: 8/10
✅ Researched Empresa B - Score: 7/10
...

✅ Results saved to vendasia_results_20241024_143022.csv
```

### 5. Review Results
```bash
# Open CSV in Numbers/Excel
open vendasia_results_*.csv
```

Check:
- Lead quality (score 7-10?)
- Messages sound natural?
- Personalization relevant?

### 6. Go Live (when ready)
```python
# In src/vendasia_agent.py, change:
results = agent.run_full_pipeline(
    icp_criteria=icp,
    limit=50,  # More leads
    send_emails=True  # ACTUALLY SEND!
)
```

---

## 🎯 Daily Usage

### Morning Routine (10 min)
```bash
# Run agent for 50 new leads
python src/vendasia_agent.py

# Check CSV results
open vendasia_results_*.csv

# Monitor email stats in Instantly.ai
open https://app.instantly.ai
```

### Review & Optimize
1. Check reply rate (target >25%)
2. If low: Improve prompts in `vendasia_agent.py`
3. If high: Scale to 100+ leads/day

---

## 🔧 Customization

### Change ICP (Target Market)
Edit `src/vendasia_agent.py`:
```python
icp = {
    "industry": "SaaS",  # or "E-commerce", "Marketing Agency"
    "company_size": "51-200",  # or "11-50", "201-500"
    "location": "Portugal",  # or "Spain", "Brazil"
    "titles": ["CEO", "CTO"]  # Decision makers
}
```

### Improve Messages
Edit prompts in `WriterAgent.generate_message()`:
- Adjust tone (more formal/casual)
- Change CTA (softer/harder)
- Add social proof

### Test Multiple Variants
```python
messages = self.writer.generate_message(
    research,
    channel="email",
    variants=5  # A/B/C/D/E testing
)
```

---

## 📊 Success Metrics

### Week 1 Targets
- 250 leads found (50/day × 5 days)
- 100+ qualified (score ≥7)
- 100 emails sent
- 25+ replies (25% rate)
- 5 meetings booked

### Troubleshooting

**No leads found?**
- Check Apollo API key
- Verify company_size format: "11-50" not "10-50"
- Try broader industry filter

**Low quality messages?**
- Increase GPT-4 temperature
- Add more research sources
- Refine prompts with examples

**Emails not sending?**
- Verify Instantly campaign ID
- Check from_email is warm
- Start with 10/day, increase slowly

---

## 💰 Costs (MVP)

Monthly:
- OpenAI: ~€20 (500 leads × €0.04)
- Apollo: €99 (5000 credits)
- Instantly: €97 (1000 emails/day)
- **Total: €216/month**

Revenue (10 customers @ €199):
- **€1,990/month**
- **Profit: €1,774/month (820% ROI)**

Break-even: 2 customers (€398)

---

## 🚀 Next: Advanced Features

Once MVP is working:
1. **Web Scraping**: Add Firecrawl for deep research
2. **LinkedIn**: Add Phantombuster automation
3. **CRM Sync**: Auto-update Pipedrive
4. **Response AI**: Auto-reply to questions
5. **Dashboard**: Build Next.js interface

Each adds €50-100/month value → can charge €299-499/month!

---

## 🆘 Support

Questions? Ask me anything:
- Architecture questions
- Code debugging  
- Prompt optimization
- Scaling strategy

Let's get your first customer! 🎯
