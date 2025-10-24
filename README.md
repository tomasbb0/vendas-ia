# 🤖 AI Sales Toolkit by Tomás

> **2 Products for Modern Sales Teams**  
> Autonomous SDR Agent + M&A CRM with AI

---

## 📦 What's Inside This Monorepo

This repository contains **2 AI-powered sales products**:

### 1. 🤖 [VendasIA SDR](./vendasia-sdr/) - Autonomous Sales Agent
**Generate personalized Portuguese B2B messages at scale**

- ✅ AI-powered lead processing (Gemini 2.0 Flash)
- ✅ Portuguese PT-PT native messages  
- ✅ 1,500 leads/day FREE tier
- ✅ LinkedIn + Email outreach
- ✅ Response tracking & analytics

**Perfect for**: Portuguese B2B sales teams, SDRs, founders doing outbound

👉 **[Get Started →](./vendasia-sdr/README.md)**

---

### 2. 🌐 [Pairwire CRM](./pairwire-crm/) - M&A Deal Management
**Google Sheets Add-on with AI Code Editor**

- ✅ Lead tracking with Campaign Batches
- ✅ Bulk email campaigns  
- ✅ Email tracking (timestamps, responses)
- ✅ AI Code Editor integrated
- ✅ Real-time collaboration
- ✅ Repository integration

**Perfect for**: M&A advisors, investment bankers, fundraising consultants

👉 **[Get Started →](./pairwire-crm/README.md)** | **[Use Template →](https://docs.google.com/spreadsheets/d/1-3vRM8y67szYUyQVhl6e7WGKpzNzJZQx8jSvcTozSJg/edit)**

---

## ⚡ Quick Start

### VendasIA SDR
```bash
cd vendasia-sdr
pip install -r requirements.txt
python test_gemini.py
```

### Pairwire CRM
1. Open [template](https://docs.google.com/spreadsheets/d/1-3vRM8y67szYUyQVhl6e7WGKpzNzJZQx8jSvcTozSJg/edit)
2. File → Make a copy
3. Start tracking deals!

---

## 🛠️ Tech Stack

### VendasIA SDR
- **AI**: Google Gemini 2.0 Flash (1,500 requests/day FREE)
- **Backup AI**: Groq Llama 3.1 70B (14,400 requests/day FREE)
- **Web Search**: Tavily API (1,000 searches/month FREE)
- **Language**: Python 3.9+
- **Email**: Gmail SMTP (500/day FREE)

**Total Cost**: €0/month

### Pairwire CRM
- **Platform**: Google Sheets + Apps Script
- **UI**: HTML/CSS/JavaScript (Google Material Design)
- **Deployment**: clasp (Google Apps Script CLI)
- **Collaboration**: Real-time Google Sheets
- **Cost**: 100% Free

---

## 🎯 Features Comparison

| Feature | VendasIA SDR | Pairwire CRM |
|---------|--------------|--------------|
| **Use Case** | Outbound sales automation | M&A deal tracking |
| **Target** | B2B sales teams 🇵🇹 | M&A professionals 💼 |
| **AI Integration** | ✅ Gemini 2.0 | 🔄 Coming soon |
| **Lead Processing** | ✅ Automated | ✅ Manual + Bulk |
| **Email Campaigns** | 🔄 Phase 2 | ✅ Built-in |
| **Collaboration** | ❌ Single user | ✅ Real-time multi-user |
| **Platform** | Python CLI | Google Sheets |
| **Cost** | €0/month | €0/month |

---

## 📂 Repository Structure

```
vendas-ia/                     # Monorepo root
├── README.md                  # This file
├── .gitignore
├── LICENSE
│
├── vendasia-sdr/              # 🤖 Product 1: SDR Agent
│   ├── README.md
│   ├── src/                   # Core Python code
│   ├── test_gemini.py         # Test Gemini API
│   ├── process_leads.py       # Batch processor
│   ├── leads-manual.csv       # Input leads
│   ├── leads_processed.json   # AI output
│   ├── requirements.txt
│   ├── docs/                  # Documentation
│   │   ├── AI-STACK-COMPARISON.md
│   │   ├── COMPLETE-ROADMAP.html
│   │   └── SUCCESS.html
│   ├── content/               # Email templates
│   ├── demo/                  # Demo materials
│   ├── tracking/              # Response tracking
│   └── workflows/             # n8n automation (future)
│
├── pairwire-crm/              # 🌐 Product 2: M&A CRM
│   ├── README.md
│   ├── apps-script/           # Google Apps Script code
│   │   ├── AIEditor.html
│   │   ├── ApiKeyDialog.html
│   │   ├── RepositoryDialog
│   │   ├── RegisterFileDialog.html
│   │   └── appsscript.json
│   ├── sheets-template/
│   │   └── TEMPLATE-LINK.txt  # Google Sheets template
│   └── docs/
│       └── SETUP.md
│
└── docs/                      # Shared documentation
    ├── WEEKEND-BUILD-GUIDE.md
    ├── DECISION-EXCEL-VS-CLOUD.html
    └── EXCEL-MVP-GUIDE.html
```

---

## 🚀 Roadmap

### VendasIA SDR

- ✅ **Phase 0**: Manual MVP (Python scripts) - **DONE**
- 🔄 **Phase 1**: Cloud infrastructure (Supabase + Railway) - Starting soon
- 📅 **Phase 2**: Stripe payments
- 📅 **Phase 3**: n8n automation  
- 📅 **Phase 4**: Apollo.io + Instantly.ai integration
- 📅 **Phase 5**: Next.js dashboard

### Pairwire CRM

- ✅ **V1.0**: Lead tracking + Email campaigns - **DONE**
- ✅ **V1.1**: AI Code Editor - **DONE**
- 🔄 **V2.0**: Gemini integration for AI messages - In progress
- 📅 **V2.1**: Dashboard with charts
- 📅 **V3.0**: Zapier/n8n webhooks
- 📅 **V3.1**: Advanced analytics

---

## 💡 Why 2 Products in 1 Repo?

### Shared Technology
- Both use Google Gemini for AI
- Both target sales professionals
- Shared utilities and helpers
- Common authentication patterns

### Portfolio Benefits
- **Unified showcase**: "Multi-product AI toolkit"
- **Single GitHub star**: Better visibility
- **Easier maintenance**: One place for updates
- **Code reuse**: DRY principles

### Separation of Concerns
- Each product has its own `/README.md`
- Independent versioning
- Different target audiences
- Clear folder structure

---

## 📊 Success Metrics

### VendasIA SDR
- ✅ 10 test leads processed successfully
- ✅ Portuguese PT-PT quality: 5/5
- ✅ Gemini API working perfectly
- 🎯 Goal: 1,500 leads/day capacity
- 🎯 Target: €2,970/month profit at 10 customers

### Pairwire CRM
- ✅ Google Sheets template live
- ✅ Apps Script UI functional
- ✅ Email tracking working
- 🎯 Goal: Real-time collaboration for teams
- 🎯 Target: Used by M&A advisors

---

## 🤝 Contributing

These are personal projects, but feedback is welcome!

- **Issues**: Report bugs or suggest features
- **PRs**: Small improvements accepted
- **Discussions**: Share your use case

---

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details

---

## 👤 Author

**Tomás Batalha**
- GitHub: [@tomasbb0](https://github.com/tomasbb0)
- Building AI tools for sales teams 🚀

---

## 🙏 Acknowledgments

- **Google Gemini** for free AI API tier
- **Groq** for blazing-fast inference
- **Google Apps Script** for Sheets automation
- **MIT** open-source community

---

## 📚 Documentation

### VendasIA SDR
- [Main README](./vendasia-sdr/README.md)
- [AI Stack Comparison](./vendasia-sdr/docs/AI-STACK-COMPARISON.md)
- [Complete Roadmap](./vendasia-sdr/docs/COMPLETE-ROADMAP.html)
- [Success Guide](./vendasia-sdr/docs/SUCCESS.html)

### Pairwire CRM
- [Main README](./pairwire-crm/README.md)
- [Google Sheets Template](https://docs.google.com/spreadsheets/d/1-3vRM8y67szYUyQVhl6e7WGKpzNzJZQx8jSvcTozSJg/edit)
- [Apps Script Setup](./pairwire-crm/docs/SETUP.md)

### Shared Docs
- [Weekend Build Guide](./docs/WEEKEND-BUILD-GUIDE.md)
- [Excel vs Cloud Decision](./docs/DECISION-EXCEL-VS-CLOUD.html)
- [Excel MVP Guide](./docs/EXCEL-MVP-GUIDE.html)

---

## 🎓 Learn More

### Articles & Guides
- How I built an AI SDR for €0/month
- Portuguese B2B sales automation  
- Google Sheets as a CRM platform
- Monorepo strategy for SaaS products

### Tech Stack Deep Dives
- Why Gemini 2.0 > GPT-4 for Portuguese
- Google Apps Script best practices
- Python CLI tools for sales

---

## ⭐ Star This Repo!

If you find these tools useful, please star the repo! It helps others discover it.

**[⭐ Star on GitHub →](https://github.com/tomasbb0/vendas-ia)**

---

## 📞 Get In Touch

Questions? Want to collaborate?

- Open an issue
- Email: [Your email if you want]
- LinkedIn: [Your LinkedIn if you want]

---

**Built with ❤️ in Portugal 🇵🇹**
