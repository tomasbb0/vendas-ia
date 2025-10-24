#!/bin/bash
# VendasIA - Quick Setup Script

echo "🚀 VendasIA Setup Assistant"
echo "=========================="
echo ""

# Check if tools are available
echo "Checking requirements..."
echo ""

# Open necessary signup pages
echo "📋 Step 1: Create Accounts (if needed)"
echo "Opening signup pages..."
echo ""

# Make.com
echo "1️⃣ Make.com - Opening..."
open "https://www.make.com/en/register"
sleep 2

# OpenAI
echo "2️⃣ OpenAI API - Opening..."
open "https://platform.openai.com/signup"
sleep 2

# Carrd
echo "3️⃣ Carrd.co - Opening..."
open "https://carrd.co/"
sleep 2

echo ""
echo "✅ All signup pages opened!"
echo ""
echo "📝 Next Steps:"
echo "1. Create accounts on all platforms"
echo "2. Get your OpenAI API key from: https://platform.openai.com/api-keys"
echo "3. Follow the setup guide in workflows/make-setup.md"
echo ""
echo "💡 Tip: Keep this terminal open for reference"
