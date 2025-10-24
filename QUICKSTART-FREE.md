# 🚀 QUICKSTART - MVP 100% GRÁTIS (10 minutos)

## Stack Escolhida: Gemini + Groq + Tavily + LangFlow

**Custo**: €0/mês  
**Dura**: Meses (free tiers permanentes)  
**Português**: Nativo (Gemini treinado em PT-PT)  

---

## ⚡ PASSO 1: LangFlow (2 minutos)

### Opção A - Docker (RECOMENDADO):
```bash
docker run -d -p 7860:7860 --name langflow langflowai/langflow:latest
```

### Opção B - Python (se não tiveres Docker):
```bash
# Instala uv (package manager rápido)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instala LangFlow
uv pip install langflow -U

# Run
uv run langflow run
```

✅ **Checkpoint**: Abre http://localhost:7860 - deves ver LangFlow UI

---

## 🔑 PASSO 2: Get API Keys (5 minutos)

### 2.1 Google Gemini (2 min) ⭐ PRINCIPAL
```bash
# Abre no browser:
open https://makersuite.google.com/app/apikey
```

1. Click "Create API Key"
2. Copy key: `AIza...`
3. **Guarda** num ficheiro temporário

**Limits FREE**: 1,500 requests/dia = 750 leads/dia

---

### 2.2 Groq (2 min) 🚀 BACKUP
```bash
# Abre no browser:
open https://console.groq.com/keys
```

1. Sign up (email ou Google)
2. Click "Create API Key"
3. Copy key: `gsk_...`
4. **Guarda** no mesmo ficheiro

**Limits FREE**: 14,400 requests/dia (super generoso!)

---

### 2.3 Tavily (1 min) 🔍 WEB SEARCH
```bash
# Abre no browser:
open https://app.tavily.com/
```

1. Sign up (email)
2. Dashboard → API Keys
3. Copy key: `tvly-...`
4. **Guarda** no ficheiro

**Limits FREE**: 1,000 créditos/mês = 500 company researches

---

## 📝 PASSO 3: Criar .env (1 minuto)

```bash
cd ~/Projects/vendas-ia

cat > .env << 'EOF'
# ====================================
# 🆓 FREE TIER API KEYS
# ====================================

# Google Gemini (1,500 requests/dia)
GEMINI_API_KEY=AIza_COLA_TUA_KEY_AQUI

# Groq (14,400 requests/dia - backup)
GROQ_API_KEY=gsk_COLA_TUA_KEY_AQUI

# Tavily (1000 credits/mês)
TAVILY_API_KEY=tvly_COLA_TUA_KEY_AQUI

# Gmail (opcional - para envio)
GMAIL_ADDRESS=teu@gmail.com
GMAIL_APP_PASSWORD=get_from_myaccount.google.com/apppasswords
EOF
```

**IMPORTANTE**: Substitui `COLA_TUA_KEY_AQUI` pelas keys reais!

---

## 🎨 PASSO 4: Build Agent no LangFlow (10 minutos)

### Abre LangFlow:
```bash
open http://localhost:7860
```

### 4.1 Cria Flow "Lead Research Agent"

1. **Click "New Flow"**
2. Nome: `VendasIA Lead Research`

### 4.2 Adiciona Nodes (arrasta da sidebar):

#### Node 1: Input (Company Name)
- Componente: **Text Input**
- Label: `company_name`
- Placeholder: "TechCorp PT"

#### Node 2: Tavily Search
- Componente: **Tavily Search** (procura "Tavily" na sidebar)
- API Key: `{tvly-...}` (cola tua key)
- Query: `{company_name} Portugal B2B SaaS empresa`
- Max Results: `3`
- Search Depth: `basic` (economiza créditos)

#### Node 3: Gemini Analysis (Research)
- Componente: **Google Generative AI**
- Model: `gemini-1.5-flash` (rápido e grátis)
- API Key: `{AIza-...}` (cola tua key)
- System Prompt:
```
És um analista de empresas B2B portuguesas.

Dados da empresa:
{tavily_search_results}

Tarefa:
1. Identifica 3 pain points de vendas/growth
2. Sugere 1 hook de personalização
3. Score interesse em automação (1-10)

Responde JSON:
{
  "pain_points": ["...", "...", "..."],
  "hook": "...",
  "score": 8,
  "reasoning": "..."
}
```

#### Node 4: Gemini Message Writer
- Componente: **Google Generative AI**
- Model: `gemini-1.5-pro` (melhor qualidade português)
- API Key: `{AIza-...}` (mesma key)
- System Prompt:
```
És um copywriter B2B português (Portugal).

Empresa: {company_name}
Hook: {hook do node anterior}

Escreve mensagem LinkedIn:
- Max 120 caracteres
- Menciona hook subtilmente
- CTA: "Vale conversar?"
- Português PT natural
- Sem formalidades ("Prezado", etc)

Só a mensagem, sem aspas.
```

#### Node 5: Output
- Componente: **Chat Output**
- Mostra resultado final

### 4.3 Conecta Nodes:

```
Input → Tavily Search → Gemini Analysis → Gemini Writer → Output
```

### 4.4 Testa!

1. Click **"Run"**
2. Input: `TechCorp PT`
3. Espera 5-10 segundos
4. Deves ver:
   - Research results
   - Pain points identificados
   - Mensagem LinkedIn gerada

---

## ✅ PASSO 5: Testar com 10 Empresas (5 minutos)

### 5.1 Cria CSV de teste:

```bash
cat > test-companies.csv << 'EOF'
company_name
TechCorp PT
SaaS Portugal
InnovaSoft Lisboa
CloudTech Porto
DataFlow Braga
B2B Solutions Coimbra
Sales Automation PT
Growth Labs Lisboa
TechStartup Porto
Digital Ventures Faro
EOF
```

### 5.2 No LangFlow:

1. Adiciona node **CSV Input** antes do Input
2. Upload `test-companies.csv`
3. Connect CSV → (resto do flow)
4. Click **"Run All"**
5. Vai buscar café ☕ (2-3 minutos)

### 5.3 Resultados:

Deves ter:
- ✅ 10 companies researched
- ✅ Pain points para cada uma
- ✅ 10 mensagens LinkedIn personalizadas
- ✅ Scores de qualificação

---

## 📊 PASSO 6: Export e Review (2 minutos)

### No LangFlow:
1. Click **"Export"** → Download JSON results
2. Abre ficheiro e review:
   - Mensagens soam naturais?
   - Pain points fazem sentido?
   - Scores corretos?

### Ajusta Prompts:
Se não gostares:
- Edit system prompts nos nodes Gemini
- Re-run
- Iterate até ficarem boas!

---

## 🎯 PRÓXIMOS PASSOS (Domingo)

### Agora que tens pipeline working:

#### 1. Scrape 50 Real Leads (1h):
```bash
# LinkedIn search:
# "CEO Portugal SaaS" ou "Founder Portugal Software"
# Company size: 11-50

# Copy-paste para CSV:
company_name,contact_name,title,linkedin_url
TechCorp,João Silva,CEO,linkedin.com/in/joao
...
```

#### 2. Process com Agent (30 min):
- Upload CSV no LangFlow
- Run batch processing
- Review top 20 (score >= 7)

#### 3. Manual Outreach LinkedIn (1h):
- Copy mensagens geradas
- Personaliza ligeiramente cada uma
- Envia 20 no LinkedIn
- Espaça 3-5 min entre cada

#### 4. Track Responses (ongoing):
```bash
# Cria spreadsheet:
# Data, Company, Sent, Reply, Demo_Booked, Notes
```

---

## 💰 CUSTOS & LIMITES

### Tua Stack FREE:

| Service | Free Tier | Suficiente Para |
|---------|-----------|-----------------|
| **Gemini** | 1,500 req/dia | 750 leads/dia |
| **Groq** | 14,400 req/dia | Backup ilimitado |
| **Tavily** | 1,000 credits/mês | 500 researches/mês |
| **Gmail** | 500 emails/dia | Outreach inicial |
| **LangFlow** | Local grátis | ∞ flows |

### Leads/Dia Possível:
- **Semana 1-2**: 50 leads/dia = €0
- **Semana 3-4**: 100 leads/dia = €0
- **Mês 2**: 500 leads/dia = ainda €0!

### Quando Escalar (Primeiro Cliente):
```
Revenue: €99-299/mês
Costs: €0/mês
Profit: €99-299/mês (100% margin!) 🤑
```

---

## 🆘 TROUBLESHOOTING

### LangFlow não inicia:
```bash
# Verifica Docker
docker ps

# Restart
docker restart langflow

# Ou reinstala
docker rm langflow
docker run -d -p 7860:7860 --name langflow langflowai/langflow:latest
```

### API Key não funciona:
- Gemini: Verifica que API está enabled em console.cloud.google.com
- Groq: Confirma que key não expirou
- Tavily: Check que tens créditos restantes

### Mensagens não soam naturais:
```
Ajusta prompt Gemini Writer:

"És um CEO português a escrever para outro CEO.
Tom: casual mas profissional
Estilo: direto, sem fluff
Exemplo BOM: 'João, vi o trabalho da TechCorp. Vale conversar?'
Exemplo MAU: 'Prezado João, espero que esteja bem...'"
```

### Tavily sem resultados:
- Muda query: Adiciona "+ Portugal + B2B"
- Increase max_results: 3 → 5
- Try search_depth: "advanced" (usa 2 credits vs 1)

---

## 📈 SUCCESS METRICS - Semana 1

### Targets:
- ✅ 50 leads researched
- ✅ 20 mensagens enviadas
- ✅ 5 replies (25% response rate)
- ✅ 2 demos agendadas

### Se atingires:
🎉 **TENS PRODUCT-MARKET FIT!**

Próximo passo:
- Semana 2: Scale para 100 leads/semana
- Semana 3: 200 leads/semana
- Semana 4: **Fechar primeiro cliente €99/mês**

---

## 🔥 COMANDO ÚNICO - START NOW!

```bash
# 1. Start LangFlow
docker run -d -p 7860:7860 --name langflow langflowai/langflow:latest

# 2. Get keys
open https://makersuite.google.com/app/apikey & 
open https://console.groq.com/keys & 
open https://app.tavily.com/

# 3. Open LangFlow
sleep 30 && open http://localhost:7860

echo "✅ LangFlow started!"
echo "📋 Get 3 API keys from tabs opened"
echo "🎨 Build agent visually"
echo "🚀 Process 10 test companies"
echo "💰 Cost: €0"
```

---

## ✨ DICA PRO

**Grava tudo!** 📹

Enquanto testar o agent:
1. Abre QuickTime → Nova Gravação de Ecrã
2. Grava 2-3 min mostrando:
   - LangFlow UI
   - Agent a processar companies
   - Mensagens sendo geradas
   - "Isto qualifica 100 leads/dia automaticamente"

**Usa este vídeo** no LinkedIn outreach! 🎬

---

**PRÓXIMO PASSO**: Corre o "COMANDO ÚNICO" acima! ☝️

Qualquer dúvida, pergunta! Estou aqui para ajudar em cada node! 💪
