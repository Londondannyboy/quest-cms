# CLAUDE AI ASSISTANT GUIDELINES

## 🚨 UNIVERSAL NAMING CONVENTION - CRITICAL
**THIS RULE IS ABSOLUTE - NO EXCEPTIONS**

### The Trinity Rule:
```
LOCAL DIRECTORY = GITHUB REPO = VERCEL PROJECT
```

### Example:
- Local: `/Users/dankeegan/XXX_APP_NAME/`
- GitHub: `github.com/Londondannyboy/XXX_APP_NAME`
- Vercel: `XXX_APP_NAME`

### Document Prefixing Rule:
```
ALL DOCUMENTATION MUST BE PREFIXED WITH APP-NAME-
```

### Example:
- XXX_APP_NAME-CLAUDE.md (NOT just CLAUDE.md)
- XXX_APP_NAME-RESTART.md (NOT just RESTART.md)
- XXX_APP_NAME-CONTENT-LIST.md (NOT just CONTENT-LIST.md)

### NEVER:
- ❌ Use different names (quest-rainmaker vs rainmaker-app)
- ❌ Add suffixes (-temp, -test, -new, -v2, -tmp)
- ❌ Use /tmp/ or temporary directories
- ❌ Create variations across platforms
- ❌ Forget to prefix documentation files
- ❌ Create static content - ALL CONTENT MUST BE IN SANITY

### ALWAYS:
- ✅ Check all three match before starting
- ✅ Use exact same name everywhere
- ✅ Lowercase with hyphens only (e.g., quest-rainmaker)
- ✅ Verify directory exists before working

## 🎯 Project Overview

**Project**: XXX_APP_NAME
**Target Market**: XXX_TARGET_MARKET
**Value Proposition**: XXX_VALUE_PROP
**Local Directory**: `/Users/dankeegan/XXX_APP_NAME/`
**GitHub Repository**: `https://github.com/Londondannyboy/XXX_APP_NAME`
**Production URL**: `https://XXX_DOMAIN`

## 📋 Technical Stack

- **Frontend**: Astro 5+ with React components
- **CMS**: Sanity Studio (Universal Project: bc08ijz6)
- **Styling**: Tailwind CSS
- **Deployment**: Vercel (auto-deploy on git push)
- **Content**: Universal schemas from Quest CMS

## 🔧 Universal Schema Access

This app uses the universal Quest CMS schemas:
- **Sanity Project ID**: bc08ijz6
- **Dataset**: production
- **API Version**: 2024-01-01

### CRITICAL: Sanity Workspace Setup
**BEFORE CREATING ANY CONTENT:**
1. Navigate to `/Users/dankeegan/quest-cms/`
2. Add workspace to `sanity.config.ts`
3. Deploy with `npm run deploy`
4. Verify workspace at `https://quest-cms.sanity.studio/XXX_WORKSPACE_NAME`

### Content Creation Rules:
**ALL CONTENT MUST BE CREATED IN SANITY VIA MCP**
- ❌ NEVER create static content in Astro pages
- ❌ NEVER hardcode content in components
- ✅ ALWAYS create content in Sanity first
- ✅ ALWAYS query content dynamically
- ✅ ALWAYS use MCP for content operations

### Query Pattern:
```groq
// Always filter by context
*[_type in ["company", "person", "job", "article", "location"] 
  && "XXX_APP_NAME" in contexts]
```

## 🚀 Content Creation Rules - STAGED APPROACH

### CRITICAL: Prevent Broken Links
Content MUST be created in stages to ensure zero broken links:

#### Stage 1: Foundation Content (No Internal Links)
- Create pillar pages for primary keywords
- NO internal links allowed
- External links to authoritative sources only
- Verify via MCP that content exists

#### Stage 2: Cluster Content (Links to Stage 1)
- Create supporting content
- ONLY link to Stage 1 content that exists
- Query MCP first to get valid slugs
- Never assume a URL pattern

#### Stage 3: Detail Content (Links to Stages 1 & 2)
- Create detailed/news content
- Can link to Stage 1 and Stage 2
- Always validate links before creating

### Link Validation Process:
```javascript
// Before creating any internal link:
1. Query via MCP: *[_type == "article" && slug.current == "target-slug"]
2. If result exists → Create link
3. If no result → Don't create link (use text mention instead)
```

## 🧪 Content Quality APIs

### Required for High-Quality Content:
1. **Tavily** (`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`)
   - Use for current research and statistics
   - Always use for Stage 1 pillar content

2. **Firecrawl** (`fc-fcc00e00206d4c1db2653d3815a2b0b0`)
   - PDF parsing and document extraction
   - Government site monitoring

3. **Critique Labs** (`4W8L4b9IY0xIzPBsFHRngwQ0M-9v9TcAysgauLqh6s4`)
   - Fact-checking and citations
   - Verify all statistics and claims

4. **LinkUp** (API key needed)
   - Advanced contextual search
   - Better than Tavily for specific queries

### Content Quality Score (0-100)
Every piece of content must achieve minimum 80/100:
- Content Depth (40 pts): 2500+ words for pillar pages
- Research Quality (25 pts): Use Tavily + 5+ external links
- AI Enhancement (20 pts): Use all APIs
- Currency (15 pts): Include current year data

## 📁 Development Commands

```bash
# Navigate to project (ALWAYS use full path)
cd /Users/dankeegan/XXX_APP_NAME

# Development
npm run dev           # Start development server
npm run build         # Build for production
npm run preview       # Preview production build

# Content Management
# Use MCP (sanity-quest) for all content operations

# Deployment
git add .
git commit -m "Description"
git push origin main  # Auto-deploys to Vercel
```

## 🔐 Environment Variables

```env
# Sanity CMS (Universal Project)
PUBLIC_SANITY_PROJECT_ID=bc08ijz6
PUBLIC_SANITY_DATASET=production
PUBLIC_SANITY_API_VERSION=2024-01-01
SANITY_API_TOKEN=[Use from CREDENTIALS.md]

# Deployment
VERCEL_TOKEN=gAYaR1sjB2NTXl4oYQ4CrmeY

# Content Quality APIs
TAVILY_API_KEY=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
FIRECRAWL_API_KEY=fc-fcc00e00206d4c1db2653d3815a2b0b0
CRITIQUE_LABS_API_KEY=4W8L4b9IY0xIzPBsFHRngwQ0M-9v9TcAysgauLqh6s4
LINKUP_API_KEY=[When available]
```

## ⚠️ Critical Rules

1. **Trinity Rule**: Local = GitHub = Vercel (always same name)
2. **No /tmp**: Never use temporary directories
3. **Staged Content**: Create in stages to prevent broken links
4. **MCP Validation**: Always verify content exists before linking
5. **Quality Score**: Minimum 80/100 for all content
6. **Use APIs**: Tavily for research, Firecrawl for docs, Critique for facts
7. **Footer Pages**: ALWAYS create About, Privacy, Terms, Disclaimer, Sitemap pages
8. **Zero Broken Links**: Footer must only link to existing pages (Stage 1)

## 📚 Key Documentation Files

- `RESTART.md` - Quick context for new sessions
- `CONTENT-PROMPT.md` - Staged content creation guide
- `CONTENT-LIST.md` - Stage 1 keyword tracking
- `CONTENT-GUIDE.md` - Editorial standards
- `TEMPLATES.md` - Content templates
- `CREDENTIALS.md` - API keys and tokens
- `REQUIREMENTS.md` - Product and operations specs
- `IDEATION.md` - Future opportunities

## 🎯 Success Metrics

- Zero broken links at launch
- All content scores 80+ quality
- Stage 1 content = SEO pillar pages
- Trinity naming prevents confusion
- APIs ensure authoritative content

---

**Last Updated**: September 26, 2025
**Template Version**: 1.0
**For**: Quest platform applications using universal schemas