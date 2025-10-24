# VendasIA - System Architecture

## 🔄 Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         CUSTOMER JOURNEY                         │
└─────────────────────────────────────────────────────────────────┘

1. PROSPECT DISCOVERS YOU
   │
   ├─→ LinkedIn message
   ├─→ Google search
   ├─→ Referral
   └─→ Direct visit
        │
        ▼

2. LANDS ON WEBSITE (Carrd.co)
   │
   ├─→ Reads value proposition
   ├─→ Sees pricing
   ├─→ Checks testimonials
   └─→ Fills form
        │
        ▼

3. FORM SUBMISSION
   │
   └─→ POST to Make.com Webhook
        │
        ▼

┌─────────────────────────────────────────────────────────────────┐
│                       AUTOMATION FLOW                            │
└─────────────────────────────────────────────────────────────────┘

   [WEBHOOK TRIGGER]
   Receives: nome, email, empresa, website, telefone
        │
        ▼
   [OPENAI GPT-4]
   Analyzes lead quality
   Returns: SCORE (1-10) + MOTIVO
        │
        ▼
   [GOOGLE SHEETS]
   Saves all data + AI analysis
        │
        ▼
   [FILTER: Score ≥ 7?]
        │
        ├─→ YES → [GMAIL]
        │         Sends notification to you
        │         "🔥 Lead Quente!"
        │
        └─→ NO → (Silent, just saves to sheet)

```

## 📊 Data Flow

```
INPUT (Form)                 PROCESSING (AI)              OUTPUT (Notification)
─────────────                ────────────────             ─────────────────────

Nome: João Silva       →     GPT-4 Analysis         →     Email to YOU if hot
Email: joao@tech.pt    →     • Domain check         →     
Empresa: TechCo        →     • Company size         →     Google Sheet (all)
Website: tech.pt       →     • Industry match       →     
Telefone: +351...      →     • Contact quality      →     

                             SCORE: 8/10
                             MOTIVO: "Empresa tech 
                             com 25 funcionários"
```

## 🎯 User Flow

```
COLD LEAD                 WARM LEAD                  HOT LEAD                 CUSTOMER
─────────                 ─────────                  ────────                 ────────

LinkedIn           →      Visits website      →      Fills form        →     Trial starts
message                   Reads content              Score ≥7                 14 days free
                                                     Gets call                │
                                                     Has demo                 ▼
                                                                        Converts to paid
                                                                        €49/€99/€199 MRR
```

## 💰 Revenue Flow

```
WEEK 1                    WEEK 2-4                   MONTH 2                  MONTH 6
──────                    ────────                   ───────                  ───────

50 messages      →       100+ messages       →      Scale with        →      €5K MRR
↓                        ↓                          revenue                   
12 responses             25 responses               ↓                        Build real
↓                        ↓                          Use €300+                product
5 demos                  10 demos                   MRR to hire              
↓                        ↓                          ↓                        Fork 
2 customers              5 total customers          Build proper             Activepieces
↓                        ↓                          product                  or Langflow
€98 MRR                  €392 MRR                   
```

## 🛠️ Tech Stack

```
FRONTEND (Landing)       BACKEND (Automation)        DATABASE               COMMUNICATION
──────────────────       ────────────────────        ────────              ─────────────

Carrd.co          →      Make.com             →      Google         →      Gmail
• Landing page           • Workflow engine            Sheets                • Hot leads
• Contact form          • Orchestration              • Lead storage        • Notifications
• €19/year              • Free (1K ops/mo)           • Free                • Free
                        
                        OpenAI GPT-4
                        • Lead scoring
                        • ~€2/month
```

## 📈 Scale Path

```
PHASE 1: MVP (Now)           PHASE 2: Growth             PHASE 3: Product
──────────────────           ───────────────             ────────────────

No-code tools         →      Keep no-code         →      Real product
Make.com + GPT-4             Scale to 20-50              Fork open source
€3/month cost                customers                   Hire developer
Manual demos                 €1-3K MRR                   Scale to 200+
2-3 customers                Add features                €10K+ MRR
€100-150 MRR                 Referrals
```

## 🔐 Data Security

```
CUSTOMER DATA FLOW
──────────────────

Form (HTTPS)  →  Make.com (encrypted)  →  Google Sheets (private)  →  Only YOU
                          ↓
                    OpenAI (processed)
                    (not stored by OpenAI)
```

## ⚡ Performance

```
LEAD QUALIFICATION TIME
───────────────────────

MANUAL PROCESS:                    VENDASIA:
─────────────                      ─────────

1. Read email (2 min)       →      1. Form submit (30s)
2. Google company (5 min)   →      2. AI analysis (5s)
3. Check LinkedIn (3 min)   →      3. Auto-save (1s)
4. Research industry (5 min)→      4. Notification (1s)
5. Score manually (2 min)   →      
6. Update CRM (3 min)       →      TOTAL: 37 seconds
                                   ────────────────────
TOTAL: 20 minutes                  60X FASTER
```

## 🎯 Success Metrics Dashboard

```
┌────────────────────────────────────────────────────────┐
│  VENDASIA METRICS - WEEK 1                             │
├────────────────────────────────────────────────────────┤
│                                                        │
│  LinkedIn Outreach                                     │
│  ─────────────────                                     │
│  Messages Sent:      50  ████████████████████ 100%    │
│  Responses:          12  ████░░░░░░░░░░░░░░░  24%     │
│  Demos Booked:        5  ██░░░░░░░░░░░░░░░░░  42%     │
│                                                        │
│  Sales Pipeline                                        │
│  ──────────────                                        │
│  Demos Completed:     3  ████████░░░░░░░░░░░  60%     │
│  Customers Closed:    2  ████████████░░░░░░░  67%     │
│                                                        │
│  Revenue                                               │
│  ───────                                               │
│  MRR: €98           ███████░░░░░░░ (Target: €147)     │
│                                                        │
│  ✅ SUCCESS: First customers acquired!                 │
└────────────────────────────────────────────────────────┘
```

---

**This diagram shows the complete VendasIA system from prospect to paying customer!**
