#!/usr/bin/env python3
import google.generativeai as genai

api_key = "AIzaSyBfFm4DwCBxsIZNYt9MyLexNo376DEGAtU"
genai.configure(api_key=api_key)

print("📋 Modelos disponíveis na tua API key:")
print("=" * 60)
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name}")
print("=" * 60)
