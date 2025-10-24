# VendasIA - Make.com Workflow Setup

## 🎯 Workflow Overview
**Lead Qualification Pipeline**: Form → GPT-4 → Google Sheets → Email Notification

## 📋 Required Tools (All Free Tier)
- [ ] Make.com account (1,000 operations/month free)
- [ ] OpenAI API key (GPT-4)
- [ ] Google Sheets
- [ ] Gmail account

## 🔧 Step-by-Step Setup

### Step 1: Create Google Sheet
**Sheet Name**: "VendasIA-Leads"

**Columns**:
| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Timestamp | Nome | Email | Empresa | Website | Telefone | IA_Score | IA_Motivo |

### Step 2: Make.com Scenario Structure

```
1. Webhook (Trigger)
   ↓
2. OpenAI (GPT-4)
   ↓
3. Google Sheets (Add Row)
   ↓
4. Gmail (Send Email)
```

### Step 3: Module Configurations

#### Module 1: Webhook
- **Type**: Custom webhook
- **URL**: Copy webhook URL to Carrd form
- **Data Structure**: 
  ```json
  {
    "nome": "text",
    "email": "email", 
    "empresa": "text",
    "website": "url",
    "telefone": "text"
  }
  ```

#### Module 2: OpenAI GPT-4
- **Model**: gpt-4-turbo
- **Prompt**:
```
Analisa este lead B2B português e dá uma pontuação de 1-10:

Nome: {{nome}}
Email: {{email}}
Empresa: {{empresa}}
Website: {{website}}
Telefone: {{telefone}}

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

#### Module 3: Google Sheets
- **Action**: Add a row
- **Spreadsheet**: VendasIA-Leads
- **Values**:
  - A: {{formatDate(now; "DD/MM/YYYY HH:mm")}}
  - B: {{nome}}
  - C: {{email}}
  - D: {{empresa}}
  - E: {{website}}
  - F: {{telefone}}
  - G: {{parseNumber(substring(choices[0].message.content; 7; 8))}}
  - H: {{substring(choices[0].message.content; indexOf(choices[0].message.content; "MOTIVO:") + 8; length(choices[0].message.content))}}

#### Module 4: Gmail (Conditional)
- **Condition**: Only if IA_Score ≥ 7
- **To**: seu.email@gmail.com
- **Subject**: 🔥 Lead Quente: {{empresa}}
- **Body**:
```
Nova lead qualificada no VendasIA!

👤 CONTACTO:
Nome: {{nome}}
Email: {{email}}
Empresa: {{empresa}}
Website: {{website}}
Telefone: {{telefone}}

🤖 ANÁLISE IA:
Score: {{IA_Score}}/10
Motivo: {{IA_Motivo}}

Ver todos os leads: [Link Google Sheets]
```

## 🧪 Testing Checklist
- [ ] Webhook receives form data
- [ ] GPT-4 returns score + reason
- [ ] Data saves to Google Sheets
- [ ] Email sent for scores ≥ 7
- [ ] Error handling works

## 💰 Cost Breakdown (100 leads/month)
- Make.com: €0 (free tier)
- OpenAI API: ~€1-2
- Google Sheets: €0
- Gmail: €0
**Total: €1-2/month**

## 🚀 Go-Live Checklist
- [ ] Test with 5 dummy leads
- [ ] Verify email notifications
- [ ] Check Google Sheets formatting
- [ ] Test mobile form submission
- [ ] Share sheets with team
