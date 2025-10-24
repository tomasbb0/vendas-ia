# VendasIA - Visual Setup Guide

## 🎯 Complete Setup in 2 Hours

---

## SATURDAY MORNING (9:00-12:00)

### Hour 1: Account Creation (9:00-10:00)

#### ✅ Task 1.1: Make.com Account (5 min)
1. Go to https://www.make.com/en/register
2. Sign up with Google/Email
3. Verify email
4. Skip tutorial (we'll do custom)

#### ✅ Task 1.2: OpenAI API Key (10 min)
1. Go to https://platform.openai.com/signup
2. Create account
3. Add payment method (€5 credit)
4. Go to https://platform.openai.com/api-keys
5. Click "Create new secret key"
6. Copy and save key: `sk-...`
7. **SAVE THIS KEY** - you can't see it again!

#### ✅ Task 1.3: Google Sheet Setup (15 min)
1. Open: https://sheets.google.com/create
2. Name it: "VendasIA-Leads"
3. Add these columns in Row 1:
   - A1: `Timestamp`
   - B1: `Nome`
   - C1: `Email`
   - D1: `Empresa`
   - E1: `Website`
   - F1: `Telefone`
   - G1: `IA_Score`
   - H1: `IA_Motivo`
4. Format: Make Row 1 bold, freeze it
5. Share → Get link → Copy URL
6. Save this URL!

#### ✅ Task 1.4: Test OpenAI API (5 min)
Open Terminal and run:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4-turbo-preview",
    "messages": [{"role": "user", "content": "Say hello"}],
    "max_tokens": 10
  }'
```
If you see a response, API works! ✅

---

### Hour 2: Build Make.com Workflow (10:00-11:00)

#### ✅ Task 2.1: Create New Scenario (2 min)
1. Login to Make.com
2. Click "Create a new scenario"
3. Name it: "VendasIA Lead Pipeline"

#### ✅ Task 2.2: Add Webhook Trigger (8 min)
1. Click the `+` button
2. Search "Webhooks"
3. Choose "Custom webhook"
4. Click "Create a webhook"
5. Name: "VendasIA Form"
6. Click "Save"
7. **COPY THE WEBHOOK URL** - save it!
8. Click "OK"
9. Leave the scenario open (don't test yet)

#### ✅ Task 2.3: Add OpenAI Module (15 min)
1. Click `+` after webhook
2. Search "OpenAI"
3. Choose "Create a Completion"
4. Click "Add" to create connection
5. Paste your API key from Task 1.2
6. Connection name: "VendasIA OpenAI"
7. Click "Save"
8. Configure module:
   - **Model**: Select `gpt-4-turbo-preview`
   - **Role**: User
   - **Message**: Click and paste this prompt:
   ```
   Analisa este lead B2B português e dá uma pontuação de 1-10:

   Nome: {{1.nome}}
   Email: {{1.email}}
   Empresa: {{1.empresa}}
   Website: {{1.website}}
   Telefone: {{1.telefone}}

   Critérios de qualificação:
   - Empresa 10+ funcionários: +3 pontos
   - Website profissional: +2 pontos
   - Email corporativo: +2 pontos
   - Setor SaaS/Tech: +2 pontos
   - Telefone preenchido: +1 ponto

   Responde apenas com:
   SCORE: [1-10]
   MOTIVO: [razão em 1 frase]
   ```
   - **Temperature**: 0.3
   - **Max tokens**: 150
9. Click "OK"

#### ✅ Task 2.4: Add Google Sheets Module (15 min)
1. Click `+` after OpenAI
2. Search "Google Sheets"
3. Choose "Add a Row"
4. Click "Add" to create Google connection
5. Sign in with your Google account
6. Allow permissions
7. Configure module:
   - **Spreadsheet ID**: Click and search "VendasIA-Leads"
   - **Sheet**: Sheet1
   - **Values**: Map these fields:
     - Column A: Click clock icon → `formatDate(now, DD/MM/YYYY HH:mm)`
     - Column B: Click `1.nome`
     - Column C: Click `1.email`
     - Column D: Click `1.empresa`
     - Column E: Click `1.website`
     - Column F: Click `1.telefone`
     - Column G: Type this formula: `{{parseNumber(substring(2.choices[0].message.content, 7, 2))}}`
     - Column H: Type this formula: `{{substring(2.choices[0].message.content, indexOf(2.choices[0].message.content, "MOTIVO:") + 8)}}`
8. Click "OK"

#### ✅ Task 2.5: Add Gmail Module (10 min)
1. Click `+` after Google Sheets
2. Search "Gmail"
3. Choose "Send an Email"
4. Click "Add" to create Gmail connection
5. Sign in with your Gmail
6. Allow permissions
7. **BEFORE configuring**, add a FILTER:
   - Click the wrench icon between Sheets and Gmail
   - Add condition:
     - Field: `{{parseNumber(substring(2.choices[0].message.content, 7, 2))}}`
     - Condition: "Greater than or equal to"
     - Value: `7`
   - Click "OK"
8. Configure Gmail module:
   - **To**: your@email.com
   - **Subject**: `🔥 Lead Quente: {{1.empresa}}`
   - **Content**: Paste this:
   ```
   Nova lead qualificada no VendasIA!

   👤 CONTACTO:
   Nome: {{1.nome}}
   Email: {{1.email}}
   Empresa: {{1.empresa}}
   Website: {{1.website}}
   Telefone: {{1.telefone}}

   🤖 ANÁLISE IA:
   Score: {{parseNumber(substring(2.choices[0].message.content, 7, 2))}}/10
   Motivo: {{substring(2.choices[0].message.content, indexOf(2.choices[0].message.content, "MOTIVO:") + 8)}}

   Ver todos os leads: [YOUR_GOOGLE_SHEETS_URL]
   ```
9. Replace `[YOUR_GOOGLE_SHEETS_URL]` with your sheet URL
10. Click "OK"

---

### Hour 3: Test & Launch (11:00-12:00)

#### ✅ Task 3.1: Test Workflow (20 min)
1. Right-click webhook module → "Run this module only"
2. Open new tab, use this curl command:
```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao@techstartup.pt",
    "empresa": "TechStartup",
    "website": "https://techstartup.pt",
    "telefone": "+351912345678"
  }'
```
3. Go back to Make.com
4. Click "Run once" button
5. Watch the flow execute
6. Check:
   - ✅ Webhook received data
   - ✅ OpenAI returned score
   - ✅ Data in Google Sheets
   - ✅ Email received (if score ≥7)

#### ✅ Task 3.2: Test with Bad Lead (10 min)
```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Test User",
    "email": "test@gmail.com",
    "empresa": "Small Co",
    "website": "",
    "telefone": ""
  }'
```
- Should get low score
- Should NOT get email
- Should appear in Sheets

#### ✅ Task 3.3: Activate Workflow (5 min)
1. Click "Save" (bottom right)
2. Toggle switch to "ON"
3. Workflow is LIVE! 🎉

#### ✅ Task 3.4: Document Everything (15 min)
Create a note with:
- Webhook URL
- Google Sheet URL
- OpenAI API usage
- Test results

---

## SATURDAY AFTERNOON (14:00-17:00)

### Hour 4: Carrd Landing Page (14:00-15:00)

#### ✅ Task 4.1: Create Carrd Account (5 min)
1. Go to https://carrd.co
2. Sign up (free or Pro €19/year)
3. Choose "Start from scratch"

#### ✅ Task 4.2: Build Landing Page (45 min)
1. Choose template: "SaaS" or "Landing"
2. Edit headline: "VendasIA - O Seu Estagiário de Vendas IA"
3. Edit subheadline: "Pare de Perder Tempo com Leads Não Qualificados"
4. Add 3 feature blocks:
   - 🤖 Qualificação Automática
   - 📊 Enriquecimento de Dados
   - ⚡ Integração Simples
5. Add pricing section (€49/€99/€199)
6. Add contact form:
   - Form action: YOUR_WEBHOOK_URL
   - Fields: nome, email, empresa, website, telefone
   - Button text: "Começar Teste Grátis"
7. Colors: Blue (#2563eb)
8. Font: Inter or System

#### ✅ Task 4.3: Publish (10 min)
1. Click "Publish"
2. Choose subdomain: vendas-ia.carrd.co
3. (Optional) Add custom domain
4. Click "Publish"
5. Test the form submission!

---

### Hour 5: Demo Materials (15:00-16:00)

#### ✅ Task 5.1: Create Pitch Deck (30 min)
Use Google Slides:
1. Slide 1: Problem (60% time on cold leads)
2. Slide 2: Solution (VendasIA screenshot)
3. Slide 3: Demo (workflow diagram)
4. Slide 4: ROI (€49 vs €300 saved)
5. Slide 5: CTA (Start free trial)

#### ✅ Task 5.2: Record Demo Video (20 min)
1. Open QuickTime → New Screen Recording
2. Show: Form submission → AI analysis → Email notification
3. Keep it 90 seconds
4. Upload to YouTube (Unlisted)
5. Save link

#### ✅ Task 5.3: Prepare Email Templates (10 min)
- Demo confirmation
- Follow-up (day 3)
- Follow-up (day 7)

---

### Hour 6: LinkedIn Prep (16:00-17:00)

#### ✅ Task 6.1: Optimize Your LinkedIn (20 min)
1. Update headline: "Helping Portuguese B2B companies automate sales"
2. Add VendasIA to experience
3. Update banner with VendasIA branding

#### ✅ Task 6.2: Create Message Templates (20 min)
Save 4 templates in notes:
1. CEO template
2. Sales Director template
3. Marketing Head template
4. Agency Owner template

#### ✅ Task 6.3: Set Up Tracking (20 min)
Create spreadsheet:
- Name
- Company
- Date contacted
- Response
- Demo booked
- Status

---

## SUNDAY MORNING (9:00-11:00)

### Hour 7-8: Prospect Research (9:00-11:00)

#### ✅ Find 50 Companies
Use LinkedIn Sales Navigator or manual search:

**Search terms**:
- "Portuguese SaaS" + "10-50 employees"
- "Agência digital Lisboa"
- "Software empresa Portugal"

**Target**: 
- 20 SaaS companies
- 15 Digital agencies
- 10 Consulting firms
- 5 Tech services

**For each company**, note:
- Company name
- CEO/Sales Director name
- LinkedIn URL
- Employee count
- Recent activity
- Personalization hook

---

## SUNDAY AFTERNOON (14:00-17:00)

### Hour 9-11: Send 50 LinkedIn Messages (14:00-17:00)

#### ✅ Process (3 min per message)
1. Find prospect on LinkedIn
2. Read their last 2 posts
3. Personalize template
4. Send connection request with note
5. Log in tracking sheet
6. Repeat!

#### ✅ Goal
- 50 messages sent
- 50 tracked in spreadsheet
- Templates personalized
- Follow-ups scheduled

---

## ✅ END OF WEEKEND CHECKLIST

### Technical ✅
- [ ] Make.com workflow live and tested
- [ ] Google Sheets receiving data
- [ ] OpenAI API working
- [ ] Email notifications working
- [ ] Landing page published
- [ ] Form submissions tested

### Marketing ✅
- [ ] Landing page live at vendas-ia.carrd.co
- [ ] Demo video recorded
- [ ] Pitch deck ready
- [ ] LinkedIn profile updated
- [ ] Message templates created

### Sales ✅
- [ ] 50 prospects researched
- [ ] 50 LinkedIn messages sent
- [ ] Tracking spreadsheet active
- [ ] Follow-up calendar set
- [ ] Demo booking process ready

---

## 📊 WEEK 1 TARGETS

**Monday-Friday**:
- Respond to LinkedIn messages
- Book 5 demos
- Complete 3 demos
- Close 1-2 customers
- **Target MRR: €49-98** 🎯

---

## 🆘 TROUBLESHOOTING

### Webhook not receiving data
- Check webhook URL is correct
- Test with curl command
- Check Make.com scenario is ON

### OpenAI errors
- Verify API key is correct
- Check you have credits
- Try gpt-3.5-turbo if gpt-4 fails

### Google Sheets not updating
- Check Sheet name is exact
- Verify Google connection
- Test formulas manually

### No emails received
- Check filter condition (score ≥7)
- Verify Gmail connection
- Check spam folder

---

**You got this! 🚀 Go build VendasIA!**
