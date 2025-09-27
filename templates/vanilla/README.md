# 🚀 Quest Vanilla Template - Launch Pad

## What This Is
A complete template for launching new Quest platform applications with:
- **Zero broken links** through staged content creation
- **High-quality content** using Tavily, Firecrawl, and Critique Labs APIs
- **Universal schemas** from Quest CMS (Sanity project bc08ijz6)
- **Complete documentation** for rapid deployment

## 📁 Template Files (9 Documents)

1. **CLAUDE.md** - AI assistant guidelines with Trinity naming rule
2. **RESTART.md** - Quick context for new sessions
3. **CONTENT-PROMPT.md** - Staged content creation to prevent broken links
4. **CONTENT-LIST.md** - Stage 1 keyword tracking and progress
5. **CONTENT-GUIDE.md** - Editorial standards, E-E-A-T, quality scoring
6. **TEMPLATES.md** - Adaptable content templates for consistency
7. **CREDENTIALS.md** - API keys including content quality services
8. **REQUIREMENTS.md** - Product specs and operations workflows
9. **IDEATION.md** - Growth opportunities and future features

## 🎯 Key Features

### Trinity Naming Rule
```
LOCAL DIRECTORY = GITHUB REPO = VERCEL PROJECT
Example: quest-rainmaker everywhere
```

### Staged Content Creation
- **Stage 1**: Pillar pages (no internal links) - 2500+ words
- **Stage 2**: Cluster content (links to Stage 1) - 1500+ words
- **Stage 3**: Detail pages (links to 1 & 2) - 1000+ words

### Content Quality APIs
- **Tavily**: Research and current data
- **Firecrawl**: PDF parsing and documents
- **Critique Labs**: Fact-checking and citations
- **LinkUp**: Advanced search (API key needed)

### Quality Scoring (0-100)
- Stage 1 requires 85+
- Stage 2 requires 80+
- Stage 3 requires 75+

## 🚀 How to Use This Template

### 1. Copy Template
```bash
cp -r /Users/dankeegan/quest-cms/templates/vanilla /Users/dankeegan/XXX_APP_NAME
cd /Users/dankeegan/XXX_APP_NAME
```

### 2. Replace Placeholders
Search and replace all XXX_ placeholders:
- `XXX_APP_NAME` → Your app name (e.g., quest-rainmaker)
- `XXX_TARGET_MARKET` → Your audience
- `XXX_VALUE_PROP` → Your value proposition
- `XXX_DOMAIN` → Your domain
- `XXX_KEYWORD_1` → Your Stage 1 keywords

### 3. Create GitHub Repo
```bash
gh repo create XXX_APP_NAME --public
git init
git add .
git commit -m "Initial commit from Quest vanilla template"
git push -u origin main
```

### 4. Deploy to Vercel
```bash
VERCEL_TOKEN=gAYaR1sjB2NTXl4oYQ4CrmeY npx vercel --name XXX_APP_NAME --yes --prod --token gAYaR1sjB2NTXl4oYQ4CrmeY
```

### 5. Start Creating Content
Follow CONTENT-PROMPT.md for staged creation:
1. Create Stage 1 content (no internal links)
2. Validate all Stage 1 exists
3. Create Stage 2 (links to Stage 1)
4. Create Stage 3 (links to 1 & 2)

## ✅ Pre-Launch Checklist

- [ ] All XXX_ placeholders replaced
- [ ] Trinity naming verified (local = GitHub = Vercel)
- [ ] Stage 1 content complete (85+ quality)
- [ ] Zero broken internal links
- [ ] All content uses Tavily research
- [ ] Minimum 5 external links per page
- [ ] SEO metadata complete
- [ ] Mobile responsive tested
- [ ] Analytics configured

## 🎉 Success Criteria

### Launch Day
- 20+ Stage 1 pages live
- Zero broken links
- All content scores 80+
- Site loads < 2 seconds

### Month 1
- 100+ total pages
- Organic traffic growing
- User engagement tracked
- No critical issues

## 🛠️ Maintenance

After launch:
1. Continue staged content creation
2. Monitor quality scores
3. Update content quarterly
4. Track performance metrics
5. Implement ideas from IDEATION.md

## 📞 Support

- **Quest CMS Studio**: https://quest-cms.sanity.studio/
- **Universal Schemas**: Sanity project bc08ijz6
- **MCP Server**: sanity-quest
- **GitHub**: Londondannyboy/[your-project]

---

**Template Version**: 1.0
**Created**: September 26, 2025
**Purpose**: Zero-broken-link launches for Quest apps
**Key Innovation**: Staged content creation with MCP validation