# 🌐 Pairwire CRM - M&A Deal Management with AI

> **Google Sheets Add-on for M&A professionals**  
> Manage deals, track emails, and use AI code editor directly in spreadsheets

---

## 🎯 What It Is

A **Google Apps Script Add-on** that turns Google Sheets into a powerful CRM for M&A deals:

- ✅ Lead tracking with Campaign Batches
- ✅ Bulk email campaigns
- ✅ Email tracking (sent timestamps, response tracking)
- ✅ **AI Code Editor** integrated (write code in sheets!)
- ✅ Repository integration
- ✅ Real-time collaboration

---

## 🚀 Quick Start

### Option 1: Use the Template (Easiest)

1. **Open the template**: [Pairwire PipeDash Template](https://docs.google.com/spreadsheets/d/1-3vRM8y67szYUyQVhl6e7WGKpzNzJZQx8jSvcTozSJg/edit?usp=sharing)
2. **Make a copy**: File → Make a copy
3. **Start using**: Add leads, create campaigns, track emails!

### Option 2: Deploy Apps Script Yourself

```bash
# 1. Install clasp (Google Apps Script CLI)
npm install -g @google/clasp

# 2. Login to Google
clasp login

# 3. Create new project
clasp create --type sheets --title "Pairwire CRM"

# 4. Push code
cd apps-script
clasp push

# 5. Open in browser
clasp open
```

---

## 📊 Features

### 1. **Lead Management**
- Track leads with unique Lead IDs (e.g., `LD-C1-JB-DIN-31`)
- Organize by Campaign Batches
- Full name, email, company info

### 2. **Email Campaigns**
- Create bulk email campaigns
- Track sent timestamps
- Monitor "days ago" automatically
- Response tracking

### 3. **AI Code Editor** 🤖
- Write and edit code directly in sheets
- Syntax highlighting
- File management integration
- Repository dialogs

### 4. **Real-time Collaboration**
- Multiple users can work simultaneously
- Share via link (no file downloads needed)
- Comment and discuss deals inline

---

## 🏗️ Architecture

```
pairwire-crm/
├── apps-script/           # Google Apps Script code
│   ├── AIEditor.html      # AI code editor UI
│   ├── ApiKeyDialog.html  # API key configuration
│   ├── RepositoryDialog   # Repo management
│   ├── RegisterFileDialog.html
│   └── appsscript.json    # Apps Script manifest
├── sheets-template/       # Link to Google Sheets template
│   └── TEMPLATE-LINK.txt
└── docs/
    └── SETUP.md           # Full setup guide
```

---

## 🎨 UI Components

### AIEditor
- Clean Google Material Design
- Rounded corners, modern styling
- Collapsible file results
- Syntax highlighting ready

### Dialogs
- **ApiKeyDialog**: Set Gemini/OpenAI API keys
- **RepositoryDialog**: Connect GitHub repos
- **RegisterFileDialog**: Register files for tracking

---

## 📈 Sheets Structure

The template includes these sheets:

1. **Main** - Lead database with Campaign Batches
2. **Leads** - Full lead information
3. **Campaign Batches** - Organize campaigns
4. **Email Tracking** - Track sent emails, timestamps, responses

---

## 🔧 Custom Menu

Once installed, you'll see buttons in your sheet:

- 🆕 **Add Leads** - Quick lead entry
- 📧 **Create Bulk Email Campaign** - Send to multiple leads
- 🤖 **AI Code Editor** - Open code editor

---

## 💡 Use Cases

Perfect for:
- **M&A advisors** tracking deal flow
- **Investment bankers** managing prospects
- **Fundraising consultants** organizing leads
- **Corp dev teams** tracking acquisition targets

---

## 🆚 Why Google Sheets?

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| **Collaboration** | ❌ Email files | ✅ Real-time |
| **Cost** | ❌ Office license | ✅ 100% Free |
| **Automation** | Python (openpyxl) | ✅ Apps Script |
| **Access** | Download file | ✅ Share link |
| **Updates** | Manual sync | ✅ Auto-sync |

---

## 🚀 Roadmap

- ✅ Lead tracking
- ✅ Email campaigns
- ✅ AI Code Editor
- 🔄 Gemini integration for AI messages
- 📅 Auto-generate personalized emails
- 📅 Dashboard with charts
- 📅 Zapier/n8n webhooks

---

## 🔗 Related Projects

- **VendasIA SDR** (`../vendasia-sdr/`) - Autonomous SDR agent for B2B sales
- Both use Gemini API and Google Sheets

---

## 📞 Support

Built by [@tomasbb0](https://github.com/tomasbb0)  
For M&A professionals 💼

---

## 📄 License

MIT License - See parent repo LICENSE

---

## 🎓 Learn More

- **Template**: https://docs.google.com/spreadsheets/d/1-3vRM8y67szYUyQVhl6e7WGKpzNzJZQx8jSvcTozSJg/edit
- **Apps Script Docs**: https://developers.google.com/apps-script
- **Clasp CLI**: https://github.com/google/clasp
