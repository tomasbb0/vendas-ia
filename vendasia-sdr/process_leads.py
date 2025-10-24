#!/usr/bin/env python3
"""
VendasIA - Batch Lead Processor
Processa CSV de leads e gera mensagens LinkedIn
"""

import google.generativeai as genai
import csv
import json
from datetime import datetime

# Configure Gemini
API_KEY = "AIzaSyBfFm4DwCBxsIZNYt9MyLexNo376DEGAtU"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

print("🚀 VendasIA - Batch Lead Processor")
print("=" * 70)
print()

# Read CSV
leads = []
with open('leads-manual.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    leads = list(reader)

print(f"📊 {len(leads)} leads carregados")
print()

results = []

for i, lead in enumerate(leads[:10], 1):  # Process first 10
    print(f"[{i}/10] 🔍 A processar: {lead['name']} - {lead['company']}")
    
    prompt = f"""
És um sales expert português especializado em B2B SaaS.

Lead:
- Nome: {lead['name']}
- Empresa: {lead['company']}
- Cargo: {lead['title']}

Tarefa:
1. Identifica 2 pain points prováveis em vendas/marketing
2. Sugere 1 hook de personalização
3. Score 1-10 de fit para automação de vendas
4. Escreve mensagem LinkedIn CURTA (max 150 chars)

Regras mensagem:
- Português PT natural e casual
- Menciona pain point específico
- CTA: "Vale conversar?" ou similar
- SEM "Prezado", "Espero que esteja bem", formalidades

Responde APENAS JSON:
{{
  "pain_points": ["pain1", "pain2"],
  "hook": "texto personalizado",
  "fit_score": 8,
  "message": "mensagem aqui"
}}
"""
    
    try:
        response = model.generate_content(prompt)
        # Extract JSON from response (may have markdown formatting)
        text = response.text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        
        data = json.loads(text)
        
        result = {
            **lead,
            **data,
            'processed_at': datetime.now().isoformat()
        }
        results.append(result)
        
        print(f"   ✅ Fit Score: {data['fit_score']}/10")
        print(f"   💬 {data['message'][:80]}...")
        print()
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        print()

# Save results
output_file = 'leads_processed.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("=" * 70)
print(f"✅ Processamento completo!")
print(f"📄 Resultados guardados em: {output_file}")
print()
print("📊 Estatísticas:")
print(f"   Total processados: {len(results)}")
high_fit = [r for r in results if r.get('fit_score', 0) >= 7]
print(f"   High-fit leads (≥7): {len(high_fit)}")
print()
print("🎯 Próximo passo:")
print("   1. Review leads_processed.json")
print("   2. Envia mensagens aos top 20")
print("   3. Track responses")
print()
print("💰 Custo desta run: €0 (free tier)")
