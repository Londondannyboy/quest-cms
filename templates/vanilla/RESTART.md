# 🚀 XXX_APP_NAME - QUICK RESTART CONTEXT

## 🎯 IMMEDIATE CONTEXT
**Project**: XXX_APP_NAME - XXX_BRIEF_DESCRIPTION
**Directory**: `/Users/dankeegan/XXX_APP_NAME/`
**Live Site**: https://XXX_DOMAIN
**GitHub**: https://github.com/Londondannyboy/XXX_APP_NAME
**Tech Stack**: Astro + Sanity CMS + Tailwind CSS

## 🚨 CRITICAL RULES - READ FIRST

### Trinity Naming Rule
```
LOCAL DIRECTORY = GITHUB REPO = VERCEL PROJECT
All must be: XXX_APP_NAME
```

### NEVER:
- Use /tmp/ or temporary directories
- Create different names across platforms
- Create internal links without MCP validation
- Skip the staged content approach

### ALWAYS:
- Work in `/Users/dankeegan/XXX_APP_NAME/`
- Verify content exists before linking
- Use Stage 1 → 2 → 3 content creation
- Check quality score (min 80/100)

## 📋 Current Status

### ✅ Completed
- [ ] Project setup
- [ ] Sanity integration 
- [ ] Stage 1 content (pillar pages)
- [ ] Stage 2 content (cluster pages)
- [ ] Stage 3 content (detail pages)

### 🔧 In Progress
- [ ] XXX_CURRENT_TASK

### 📝 Next Steps
- [ ] XXX_NEXT_TASK_1
- [ ] XXX_NEXT_TASK_2
- [ ] XXX_NEXT_TASK_3

## 🗂️ Key Files to Reference

### Documentation
- `CLAUDE.md` - Complete AI guidelines and rules
- `CONTENT-PROMPT.md` - Staged content creation process
- `CONTENT-LIST.md` - Stage 1 keyword targets and progress
- `CONTENT-GUIDE.md` - Editorial standards and quality metrics
- `TEMPLATES.md` - Content templates for consistency
- `CREDENTIALS.md` - API keys and authentication
- `REQUIREMENTS.md` - Product specs and operations
- `IDEATION.md` - Future features and opportunities

### Code Structure
```
XXX_APP_NAME/
├── src/
│   ├── pages/          # Astro pages
│   ├── components/     # Reusable components
│   ├── layouts/        # Page layouts
│   └── lib/            # Utilities and queries
├── public/             # Static assets
└── package.json        # Dependencies
```

## 🔑 Quick Commands

```bash
# Start development
cd /Users/dankeegan/XXX_APP_NAME
npm run dev

# Deploy to production
git add .
git commit -m "Update description"
git push origin main

# Check deployment
VERCEL_TOKEN=gAYaR1sjB2NTXl4oYQ4CrmeY npx vercel list --token gAYaR1sjB2NTXl4oYQ4CrmeY
```

## 📊 Content Status

### Stage 1: Pillar Content (No Internal Links)
| Keyword | URL | Status | Quality Score |
|---------|-----|--------|---------------|
| XXX_KEYWORD_1 | /XXX_SLUG_1 | [ ] Draft | 0/100 |
| XXX_KEYWORD_2 | /XXX_SLUG_2 | [ ] Draft | 0/100 |
| XXX_KEYWORD_3 | /XXX_SLUG_3 | [ ] Draft | 0/100 |

### Stage 2: Cluster Content (Links to Stage 1)
*Only create after Stage 1 is complete*

### Stage 3: Supporting Content (Links to 1 & 2)
*Only create after Stage 2 is complete*

## 🎬 Sanity MCP Integration

### Connection
- **MCP Server**: sanity-quest
- **Project ID**: bc08ijz6 (Universal Quest schemas)
- **Dataset**: production

### Query Examples
```groq
// Get all content for this app
*[_type in ["company", "person", "job", "article", "location"] 
  && "XXX_APP_NAME" in contexts]

// Check if slug exists (before creating link)
*[_type == "article" && slug.current == "target-slug"][0]
```

## 🧪 Content Quality Tools

### Active APIs:
- **Tavily**: Research and current data
- **Firecrawl**: PDF and document parsing
- **Critique Labs**: Fact-checking and citations
- **LinkUp**: [Pending API key]

### Quality Requirements:
- Minimum score: 80/100
- Stage 1 pages: 2500+ words
- External links: 5+ authoritative sources
- Research: Must use Tavily for current data

## 🚨 Common Issues & Solutions

### Broken Links
**Problem**: Links to non-existent content
**Solution**: Always validate via MCP before creating links

### Low Quality Score
**Problem**: Content scores below 80
**Solution**: Use Tavily research, add external links, expand to 2500+ words

### Naming Confusion
**Problem**: Different names across platforms
**Solution**: Follow Trinity Rule - same name everywhere

## 💡 Quick Tips

1. **Always start with Stage 1** - No internal links
2. **Validate before linking** - Query MCP for slug existence
3. **Use all APIs** - Better content quality
4. **Check quality score** - Must be 80+
5. **Follow Trinity Rule** - Same name everywhere

## 📞 Resources

- **Quest CMS Studio**: https://quest-cms.sanity.studio/
- **Universal Schemas**: bc08ijz6 project in Sanity
- **Vercel Dashboard**: Check deployment status
- **GitHub**: https://github.com/Londondannyboy/XXX_APP_NAME

---

**Session Started**: [Current Date]
**Template Version**: 1.0
**Priority**: XXX_CURRENT_PRIORITY