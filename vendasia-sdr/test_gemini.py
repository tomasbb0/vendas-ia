#!/usr/bin/env python3
"""
VendasIA - Test Script SIMPLES
Testa Gemini para gerar mensagens LinkedIn
"""

print("🚀 VendasIA - Test Rápido")
print("=" * 50)
print()

# 1. Check se tens Gemini instalado
print("📦 A verificar dependências...")
try:
    import google.generativeai as genai
    print("✅ Google Gemini instalado!")
except ImportError:
    print("❌ Gemini não instalado. A instalar agora...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'google-generativeai', '--quiet'])
    import google.generativeai as genai
    print("✅ Gemini instalado com sucesso!")

print()
print("=" * 50)
print("🔑 AGORA PRECISO DA TUA GEMINI API KEY")
print("=" * 50)
print()
print("1. Abre: https://makersuite.google.com/app/apikey")
print("2. Click 'Create API Key'")
print("3. Copia a key (começa com AIza...)")
print("4. Cola aqui:")
print()

# Get API key do user
api_key = input("👉 Cola tua Gemini API key aqui: ").strip()

if not api_key or not api_key.startswith("AIza"):
    print()
    print("❌ Key inválida! Tem de começar com 'AIza'")
    print("   Vai buscar em: https://makersuite.google.com/app/apikey")
    exit(1)

print()
print("✅ Key recebida!")
print()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

print("=" * 50)
print("🧪 A TESTAR GEMINI...")
print("=" * 50)
print()

# Test com empresa portuguesa
company = "TechCorp PT"
print(f"📊 A analisar: {company}")
print()

prompt = f"""
És um sales expert português.

Empresa: {company}
Setor: SaaS B2B

Tarefa:
1. Identifica 2 pain points prováveis desta empresa em vendas
2. Sugere 1 hook de personalização
3. Escreve 1 mensagem LinkedIn CURTA (max 120 chars)

Regras mensagem:
- Português PT natural
- Tom casual mas profissional
- CTA: "Vale conversar?"
- SEM "Prezado", "Espero que esteja bem"

Responde só com a mensagem, sem aspas.
"""

try:
    print("⏳ Gemini a processar...")
    response = model.generate_content(prompt)
    message = response.text.strip().strip('"\'')
    
    print()
    print("=" * 50)
    print("✅ SUCESSO! Mensagem gerada:")
    print("=" * 50)
    print()
    print(f"💬 {message}")
    print()
    print("=" * 50)
    print()
    print("🎉 GEMINI FUNCIONA PERFEITAMENTE!")
    print()
    print("📋 Próximos passos:")
    print("   1. Guarda esta API key num ficheiro seguro")
    print("   2. Testa com mais empresas")
    print("   3. Scrape 50 empresas do LinkedIn")
    print("   4. Process todas com este script")
    print()
    print("💰 Custo: €0 (1,500 mensagens/dia grátis)")
    print("🚀 Pronto para gerar 100s de mensagens!")
    
except Exception as e:
    print()
    print(f"❌ Erro: {e}")
    print()
    print("🔍 Troubleshooting:")
    print("   1. Verifica que a API key está certa")
    print("   2. Vai a https://makersuite.google.com/app/apikey")
    print("   3. Confirma que API está enabled")
