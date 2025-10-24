# VendasIA - Weekend Action Plan

## 🗓️ Saturday Schedule (8 hours total)

### Saturday Morning (9:00-12:00) - 3 hours
**Priority: Build Core Infrastructure**

#### Hour 1 (9:00-10:00): Make.com Setup
- [ ] Create Make.com account
- [ ] Set up OpenAI API key
- [ ] Create Google Sheet "VendasIA-Leads"
- [ ] Test webhook connection

#### Hour 2 (10:00-11:00): Build Workflow
- [ ] Configure webhook trigger
- [ ] Set up GPT-4 module
- [ ] Connect Google Sheets
- [ ] Add Gmail notification

#### Hour 3 (11:00-12:00): Test & Debug
- [ ] Test with 3 dummy leads
- [ ] Verify email notifications
- [ ] Fix any bugs
- [ ] Document workflow

**Deliverables**: ✅ Working automation pipeline

### Saturday Afternoon (14:00-17:00) - 3 hours  
**Priority: Landing Page & Brand**

#### Hour 1 (14:00-15:00): Carrd Setup
- [ ] Create Carrd account
- [ ] Choose SaaS template
- [ ] Set up basic structure
- [ ] Add VendasIA branding

#### Hour 2 (15:00-16:00): Content & Design
- [ ] Add Portuguese copy from template
- [ ] Configure pricing tables
- [ ] Add contact form (connect to webhook)
- [ ] Optimize for mobile

#### Hour 3 (16:00-17:00): Launch & Test
- [ ] Publish to vendas-ia.carrd.co
- [ ] Test form submission end-to-end
- [ ] Check mobile responsiveness
- [ ] Set up Google Analytics

**Deliverables**: ✅ Live landing page

### Saturday Evening (19:00-21:00) - 2 hours
**Priority: Demo Materials**

#### Hour 1 (19:00-20:00): Demo Video
- [ ] Record 2-minute demo video
- [ ] Show problem → solution → results
- [ ] Upload to YouTube (unlisted)
- [ ] Create demo slide deck

#### Hour 2 (20:00-21:00): Sales Materials
- [ ] Prepare 5-slide pitch deck
- [ ] Create email templates
- [ ] Plan demo script
- [ ] Set up calendar booking

**Deliverables**: ✅ Demo materials ready

---

## 🗓️ Sunday Schedule (5 hours total)

### Sunday Morning (9:00-11:00) - 2 hours
**Priority: Prospect Research**

#### Hour 1 (9:00-10:00): Company Research
- [ ] Research 25 Portuguese B2B companies
- [ ] Focus on SaaS + Digital Agencies
- [ ] Use LinkedIn Sales Navigator
- [ ] Score each prospect (1-10)

#### Hour 2 (10:00-11:00): Contact Research  
- [ ] Find CEOs/Sales Directors
- [ ] Verify LinkedIn activity
- [ ] Create personalization notes
- [ ] Build target list of 50

**Deliverables**: ✅ 50 qualified prospects

### Sunday Afternoon (14:00-17:00) - 3 hours
**Priority: Outreach Campaign**

#### Hour 1 (14:00-15:00): Message Preparation
- [ ] Personalize 50 LinkedIn messages
- [ ] Use templates but customize each
- [ ] Prepare connection requests
- [ ] Schedule sending times

#### Hour 2 (15:00-16:00): LinkedIn Outreach
- [ ] Send 25 connection requests
- [ ] Send 25 personalized messages
- [ ] Track in spreadsheet
- [ ] Set follow-up reminders

#### Hour 3 (16:00-17:00): Follow-up System
- [ ] Set up tracking spreadsheet
- [ ] Plan week 1 follow-ups
- [ ] Prepare demo booking calendar
- [ ] Create response templates

**Deliverables**: ✅ 50 prospects contacted

---

## 📋 Master Checklist

### Technical Setup ✅
- [ ] Make.com workflow working
- [ ] Google Sheets connected
- [ ] GPT-4 API configured
- [ ] Gmail notifications active
- [ ] Landing page live
- [ ] Form submissions tested

### Business Setup ✅
- [ ] Prospect list (50 companies)
- [ ] LinkedIn messages sent (50)
- [ ] Demo materials ready
- [ ] Tracking system active
- [ ] Follow-up plan created
- [ ] Calendar booking setup

### Week 1 Goals 🎯
- [ ] **5 LinkedIn responses** (10% response rate)
- [ ] **3 demo bookings** (60% of responses)
- [ ] **1-2 customers closed** (40% demo conversion)
- [ ] **€49-98 MRR** (First revenue!)

---

## ⚡ Quick Start Commands

### OpenAI API Setup
```bash
# Get API key from: https://platform.openai.com/api-keys
# Test API connection:
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model":"gpt-4","messages":[{"role":"user","content":"Test"}]}' \
     https://api.openai.com/v1/chat/completions
```

### Google Sheets Template
```
A1: Timestamp
B1: Nome  
C1: Email
D1: Empresa
E1: Website
F1: Telefone
G1: IA_Score
H1: IA_Motivo
```

### Carrd Form HTML
```html
<form action="YOUR_MAKE_WEBHOOK_URL" method="POST">
  <input type="text" name="nome" placeholder="Seu nome" required>
  <input type="email" name="email" placeholder="Email empresarial" required>  
  <input type="text" name="empresa" placeholder="Nome da empresa" required>
  <input type="url" name="website" placeholder="Website da empresa">
  <input type="tel" name="telefone" placeholder="Telefone (opcional)">
  <button type="submit">Começar Teste Grátis</button>
</form>
```

---

## 🚨 Success Criteria

### End of Weekend Must-Haves:
1. **Technical**: Working automation (form → AI → email)
2. **Marketing**: Live landing page with clear value prop
3. **Sales**: 50 prospects contacted with personalized messages
4. **Process**: Tracking system for leads and conversations

### Week 1 Success Metrics:
- **Response Rate**: >10% (5+ responses from 50 messages)
- **Demo Booking**: >50% (3+ demos from responses)
- **Customer Conversion**: >30% (1-2 customers from demos)
- **MRR**: €49-98 (First paying customers!)

---

## 🎯 Emergency Backup Plan

If anything breaks:

### Technical Issues:
- **Webhook fails**: Use Google Forms + Zapier
- **Make.com problems**: Use Zapier alternative  
- **GPT-4 API issues**: Use GPT-3.5-turbo
- **Carrd problems**: Use Notion page

### Time Management:
- **Running behind**: Focus on outreach first
- **Saturday overflow**: Move demo prep to Sunday morning
- **Sunday tight**: Send 25 messages, save rest for Monday

### Quality Control:
- **Minimum viable**: 25 good prospects > 50 mediocre
- **Message quality**: 10 great messages > 50 generic
- **Demo readiness**: Simple deck > complex video

---

**Remember**: Better to have 25 perfect prospects contacted than 50 rushed ones. Quality > Quantity! 🎯
