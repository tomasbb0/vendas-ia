# VendasIA - GitHub Setup

## ✅ Git Repository Initialized!

Your local git repository is ready. Now let's push it to GitHub.

## 🚀 Push to GitHub (2 minutes)

### Option 1: Using GitHub CLI (Fastest)
```bash
# Install GitHub CLI if you don't have it
brew install gh

# Login to GitHub
gh auth login

# Create repo and push
gh repo create vendas-ia --public --source=. --remote=origin --push
```

### Option 2: Manual Setup (3 steps)

#### Step 1: Create GitHub Repository
1. Go to: https://github.com/new
2. Repository name: `vendas-ia`
3. Description: `🇵🇹 VendasIA - AI-powered B2B lead qualification for Portuguese companies`
4. Make it **Public** (or Private if you prefer)
5. **DON'T** initialize with README, .gitignore, or license
6. Click "Create repository"

#### Step 2: Connect Local Repo to GitHub
```bash
# Add GitHub as remote (replace with your actual repo URL)
git remote add origin https://github.com/tomasbb0/vendas-ia.git

# Verify remote was added
git remote -v
```

#### Step 3: Push to GitHub
```bash
# Push to main branch
git branch -M main
git push -u origin main
```

## 📋 Your Repository Details

- **GitHub Username**: tomasbb0
- **Repository Name**: vendas-ia
- **Repository URL**: https://github.com/tomasbb0/vendas-ia
- **Git User**: tomasbb0
- **Git Email**: tomasbb0@users.noreply.github.com

## 🎯 Repository Description (for GitHub)

**Short Description**:
```
🇵🇹 AI-powered B2B lead qualification assistant for Portuguese companies. Save 20-40h/month on manual lead qualification.
```

**Topics** (add these tags):
```
ai, sales, b2b, portugal, lead-qualification, gpt4, automation, saas, portuguese, startup
```

## 📝 Future Git Workflow

### Daily Commits
```bash
# See what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "feat: add new feature"

# Push to GitHub
git push
```

### Commit Message Guidelines
```bash
# New features
git commit -m "feat: add LinkedIn automation"

# Bug fixes
git commit -m "fix: correct GPT prompt scoring"

# Documentation
git commit -m "docs: update setup guide"

# Performance
git commit -m "perf: optimize webhook response time"

# Updates
git commit -m "chore: update dependencies"
```

## 🔒 Keep Secrets Safe

Already configured in `.gitignore`:
- ✅ API keys
- ✅ Environment variables
- ✅ Customer data
- ✅ Personal prospect lists

**Never commit**:
- OpenAI API keys
- Make.com webhook URLs
- Customer emails/data
- Personal contact lists

## 🌟 Make it Shine on GitHub

### Add a Professional README Badge
```markdown
![Launch Status](https://img.shields.io/badge/status-launching-brightgreen)
![MRR](https://img.shields.io/badge/MRR-€0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
```

### Add a Screenshot
Once your landing page is live:
1. Take screenshot
2. Add to repo: `screenshots/landing-page.png`
3. Add to README: `![VendasIA Landing Page](screenshots/landing-page.png)`

## 🎯 Quick Commands

```bash
# Check repository status
git status

# View commit history
git log --oneline --graph

# See what's different
git diff

# Push all changes
git add . && git commit -m "update" && git push

# Create a new branch for experiments
git checkout -b feature/new-idea
```

## 🚀 Ready to Push!

Your code is committed locally. Now choose one of the options above to push to GitHub.

**Recommended**: Use GitHub CLI (Option 1) - it's the fastest!

---

**Next Steps**:
1. Push to GitHub using one of the methods above
2. Add repository description and topics
3. Star your own repo (for motivation! ⭐)
4. Share with potential investors/customers when you get traction
