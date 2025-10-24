# VendasIA - Quick Reference Cheat Sheet

## 🔗 IMPORTANT URLS (Save These!)

### Accounts
- Make.com Dashboard: https://www.make.com/
- OpenAI Dashboard: https://platform.openai.com/
- Google Sheet: [ADD YOUR URL]
- Carrd Landing Page: https://vendas-ia.carrd.co
- LinkedIn: https://linkedin.com

### Webhook URL
```
[ADD YOUR MAKE.COM WEBHOOK URL HERE]
```

### OpenAI API Key
```
sk-[YOUR KEY - KEEP SECRET!]
```

---

## ⚡ QUICK COMMANDS

### Test Webhook (Good Lead)
```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{"nome":"João Silva","email":"joao@techstartup.pt","empresa":"TechStartup","website":"https://techstartup.pt","telefone":"+351912345678"}'
```

### Test Webhook (Bad Lead)
```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{"nome":"Test","email":"test@gmail.com","empresa":"Small","website":"","telefone":""}'
```

### Check OpenAI API
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"model":"gpt-4-turbo-preview","messages":[{"role":"user","content":"hi"}]}'
```

---

## 📱 LINKEDIN MESSAGE TEMPLATES

### Template 1: CEO (Problem-Focused)
```
Olá [Nome],

Vi que a [Empresa] está a crescer no setor [setor].

Pergunta rápida: quanto tempo a vossa equipa perde por semana a qualificar leads que não convertem?

Criámos uma solução IA que automatiza isto - poupamos +30h/mês aos nossos clientes.

Vale 15min?

Cumprimentos,
Tomás
```

### Template 2: Sales Director (ROI)
```
[Nome], parabéns pelo crescimento da [Empresa]!

Ajudamos equipas como a vossa a poupar 20-40h/mês na qualificação.

ROI imediato: €49/mês poupa €300+ em tempo.

Posso mostrar como em 10min?

Tomás
```

---

## 🎯 DAILY CHECKLIST

### Morning (30 min)
- [ ] Check Google Sheets for new leads
- [ ] Respond to LinkedIn messages
- [ ] Follow up on demos

### Afternoon (30 min)
- [ ] Send 10 new LinkedIn messages
- [ ] Update tracking spreadsheet
- [ ] Book demos for tomorrow

### Evening (15 min)
- [ ] Review day's metrics
- [ ] Plan tomorrow's targets
- [ ] Prepare demo materials

---

## 📊 KEY METRICS

### Week 1 Targets
- **Messages**: 50
- **Responses**: 12 (24%)
- **Demos**: 5 (42%)
- **Customers**: 2 (40%)
- **MRR**: €98

### Success Indicators
✅ Response rate >20%
✅ Demo booking rate >40%
✅ Demo-to-customer >30%
✅ At least 1 customer by Friday

---

## 🆘 EMERGENCY CONTACTS

### Technical Issues
- Make.com Support: help.make.com
- OpenAI Support: help.openai.com
- Carrd Support: carrd.co/support

### Quick Fixes
- **Workflow stopped**: Toggle OFF then ON in Make.com
- **API errors**: Check billing at platform.openai.com/account/billing
- **Form not working**: Test webhook URL with curl
- **No emails**: Check Gmail spam, verify filter condition

---

## 💰 COSTS TRACKING

### Monthly Expenses
- Make.com: €0 (free tier, 1000 ops)
- OpenAI API: ~€2 (100 leads @ €0.02 each)
- Carrd Pro: €1.58/month (€19/year)
- **Total: ~€3.58/month**

### Revenue Target
- Month 1: €147-245 (3-5 customers)
- Profit: €143-241 💰

---

## 🎯 PITCH POINTS

### Problem
"60% do tempo de vendas desperdiçado em leads frios"

### Solution
"IA qualifica automaticamente 24/7 em português"

### ROI
"€49/mês poupa €300-600 em tempo = ROI de 500-1200%"

### Proof
"TechStartup poupou 35 horas/mês no primeiro mês"

### CTA
"14 dias grátis, sem cartão, sem risco"

---

## 📞 DEMO SCRIPT (15 min)

1. **Opening** (30s): "Em 15min vou mostrar como poupar 30h/mês"
2. **Discovery** (3min): "Quantos leads recebem? Quanto tempo na qualificação?"
3. **Demo** (7min): Show form → AI → notification → dashboard
4. **ROI** (3min): Calculate their savings live
5. **Close** (2min): "Vês valor? Quando começamos?"

---

## 🔥 OBJECTION HANDLING

| Objection | Response |
|-----------|----------|
| "Too expensive" | "2 horas poupadas = payback completo. Vocês vão poupar 20-40h." |
| "Too good to be true" | "14 dias grátis. Testa com leads reais. Sem compromisso." |
| "Need to think" | "O que especificamente? Talvez esclareça agora." |
| "Have a system" | "Ótimo! VendasIA integra. Quer ver como?" |

---

## 📈 TRACKING SHORTCUTS

### Quick Log Format
```
[Date] [Name] - [Company] - [Status]
28/10 João Silva - TechStartup - Message sent
29/10 João Silva - TechStartup - Response received  
30/10 João Silva - TechStartup - Demo booked
01/11 João Silva - TechStartup - Customer! €99 MRR
```

---

## ✅ SHORTCUTS

### Mac
- New LinkedIn tab: `Cmd+T` → `linkedin.com/search/people`
- New email: `Cmd+N` in Gmail
- Copy last command: `↑` in Terminal

### LinkedIn Search
```
Portuguese SaaS CEO site:linkedin.com
Lisboa "Sales Director" "10-50 employees"
Porto "Head of Marketing" B2B
```

---

## 🎯 FOCUS AREAS

### Week 1: Validation
**Goal**: Prove people will pay
**Action**: Get 2-3 customers at €49-99

### Week 2-4: Scale
**Goal**: Reach €500 MRR
**Action**: Referrals + content

### Month 2: Product
**Goal**: Build real product
**Action**: Use revenue to hire/build

---

**REMEMBER**: Done > Perfect. Ship fast, iterate faster! 🚀
