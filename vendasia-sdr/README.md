# 🤖 VendasIA SDR - Autonomous Sales Agent

> **AI-powered SDR agent for Portuguese B2B sales**  
> Generate personalized LinkedIn messages at scale with Google Gemini 2.0 Flash

---

## 🎯 What It Does

- **Scrapes leads** from LinkedIn/Apollo
- **Generates personalized messages** with AI (Portuguese PT-PT native)
- **Tracks responses** and demo bookings
- **100% Free tier** (1,500 leads/day with Gemini)

---

## 🚀 Quick Start

### 1. Setup API Key

```bash
# Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env
```

Get your free Gemini API key: https://aistudio.google.com/app/apikey

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Test Gemini

```bash
python test_gemini.py
```

### 4. Process Leads

```bash
# Edit leads-manual.csv with your leads
python process_leads.py

# Output: leads_processed.json with generated messages
```

---

## 📊 Example Output

```json
{
  "name": "João Silva",
  "company": "TechCorp PT",
  "title": "CEO",
  "pain_points": ["Scaling sales", "Lead quality"],
  "hook": "Vejo o crescimento da TechCorp!",
  "message": "João, vejo o crescimento da TechCorp PT! Escalar vendas pode ser um desafio. Vale conversar?",
  "fit_score": 8
}
```

---

## 🏗️ Architecture

```
vendasia-sdr/
├── src/                    # Core Python code
│   └── vendasia_free_agent.py
├── test_gemini.py         # Test Gemini API
├── process_leads.py       # Batch process leads
├── leads-manual.csv       # Input: Your leads
├── leads_processed.json   # Output: AI messages
├── docs/                  # Documentation
│   ├── AI-STACK-COMPARISON.md
│   ├── COMPLETE-ROADMAP.html
│   └── SUCCESS.html
├── tracking/              # Track responses
└── workflows/             # n8n automation (future)
```

---

## 💰 Pricing (€0/month)

- **Gemini 2.0 Flash**: 1,500 requests/day FREE
- **Groq Llama 3.1 70B**: 14,400 requests/day FREE (backup)
- **Tavily Search**: 1,000 searches/month FREE
- **Gmail SMTP**: 500 emails/day FREE

**Total**: €0/month for MVP validation

---

## 📈 Roadmap

- ✅ **Phase 0**: Manual MVP (Python scripts) - DONE
- 🔄 **Phase 1**: Cloud infrastructure (Supabase + Railway)
- 📅 **Phase 2**: Stripe payments
- 📅 **Phase 3**: n8n automation
- 📅 **Phase 4**: Apollo.io + Instantly.ai integration
- 📅 **Phase 5**: Next.js dashboard

See `docs/COMPLETE-ROADMAP.html` for full plan.

---

## 🎓 Learn More

- **Stack Comparison**: `docs/AI-STACK-COMPARISON.md` (800+ lines)
- **Weekend Build**: `docs/WEEKEND-BUILD-GUIDE.md`
- **Success Guide**: `docs/SUCCESS.html`

---

## 📞 Support

Built by [@tomasbb0](https://github.com/tomasbb0)  
For Portuguese B2B sales teams 🇵🇹

---

## 📄 License

MIT License - See parent repo LICENSE
