# 🚀 LAUNCH-PROMPT.md - Quest App Launch System

**The Master Guide for Launching New Quest Apps with Zero Broken Links**

## Quick Launch Command
```
"I want to create a new app called [APP-NAME-QUEST] for the [INDUSTRY] market in [LOCATION]. Execute LAUNCH-PROMPT.md"
```

Example:
```
"I want to create a new app called Tractor-Insurance-Quest for the UK tractor insurance market. Execute LAUNCH-PROMPT.md"
```

## 🎯 CRITICAL REQUIREMENTS - READ FIRST

### The Four Pillars of Quest App Launch
1. **SANITY FIRST** - All content MUST be created in Sanity CMS
2. **PREFIX EVERYTHING** - All docs must be prefixed with APP-NAME-
3. **ZERO BROKEN LINKS** - Use staged content approach
4. **TRINITY NAMING** - Local = GitHub = Vercel (always same name)

### NEVER DO THIS ❌
- Create static content in Astro pages
- Skip Sanity workspace setup
- Forget to prefix documentation
- Create internal links without MCP validation
- Launch with broken footer links

## 📋 PHASE 1: Research & Planning (15 minutes)

### 1.1 Keyword Research
Using Tavily/WebSearch, research:
```
"[INDUSTRY] [LOCATION] high ranking keywords"
"[INDUSTRY] [LOCATION] search volume"
"[INDUSTRY] competitors [LOCATION]"
"[INDUSTRY] regulations [LOCATION]"
```

Example for Tractor Insurance:
```
"tractor insurance UK high ranking keywords"
"agricultural vehicle insurance UK competitors"
"tractor insurance UK regulations 2025"
```

### 1.2 Identify Stage 1 Content Targets
Based on research, identify:
- 5-10 primary keyword pages (pillar content)
- 3-5 company/provider profiles
- 2-3 guide/resource pages
- Legal pages (Privacy, Terms, Disclaimer)
- About and Sitemap pages

### 1.3 Define Variables
| Variable | Example Value |
|----------|--------------|
| APP_NAME | tractor-insurance-quest |
| BRAND_NAME | Tractor Insurance Quest |
| DOMAIN | tractor-insurance.quest |
| TAGLINE | UK's Leading Tractor Insurance Platform |
| TARGET_MARKET | UK farmers, contractors, dealers |
| VALUE_PROP | Compare tractor insurance quotes |
| PRIMARY_KEYWORDS | [From Tavily research] |

## 📋 PHASE 2: Sanity CMS Setup (CRITICAL - DO NOT SKIP!)

### 2.1 Create Workspace in quest-cms
Navigate to `/Users/dankeegan/quest-cms/` and update `sanity.config.ts`:

```typescript
// Add new workspace configuration
{
  name: 'tractor-insurance', // lowercase, hyphenated
  title: 'Tractor Insurance Quest',
  projectId: 'bc08ijz6', // Always use universal project
  dataset: 'production',
  basePath: '/tractor-insurance', // URL path in Studio
  plugins: [structureTool(), visionTool()],
  schema: {
    types: allSchemas, // Use universal schemas
  }
}
```

### 2.2 Deploy Sanity Changes
```bash
cd /Users/dankeegan/quest-cms
npm run deploy
```

### 2.3 Verify Workspace
Check that workspace appears at:
`https://quest-cms.sanity.studio/tractor-insurance`

## 📋 PHASE 3: Project Setup (10 minutes)

### 3.1 Create Project Directory
```bash
# Copy vanilla template
cp -r /Users/dankeegan/quest-cms/templates/vanilla /Users/dankeegan/tractor-insurance-quest
cd /Users/dankeegan/tractor-insurance-quest
```

### 3.2 Prefix All Documentation
Rename all documentation files with APP-NAME prefix:
```bash
mv CLAUDE.md TRACTOR-INSURANCE-QUEST-CLAUDE.md
mv RESTART.md TRACTOR-INSURANCE-QUEST-RESTART.md
mv CONTENT-LIST.md TRACTOR-INSURANCE-QUEST-CONTENT-LIST.md
mv CONTENT-PROMPT.md TRACTOR-INSURANCE-QUEST-CONTENT-PROMPT.md
mv REQUIREMENTS.md TRACTOR-INSURANCE-QUEST-REQUIREMENTS.md
mv CREDENTIALS.md TRACTOR-INSURANCE-QUEST-CREDENTIALS.md
mv IDEATION.md TRACTOR-INSURANCE-QUEST-IDEATION.md
mv TEMPLATES.md TRACTOR-INSURANCE-QUEST-TEMPLATES.md
mv FOOTER-CHECKLIST.md TRACTOR-INSURANCE-QUEST-FOOTER-CHECKLIST.md
```

### 3.3 Replace All Placeholders
In each prefixed document, replace:
- XXX_APP_NAME → tractor-insurance-quest
- XXX_BRAND_NAME → Tractor Insurance Quest
- XXX_DOMAIN → tractor-insurance.quest
- XXX_TAGLINE → [Your tagline]
- XXX_TARGET_MARKET → [Your market]
- XXX_VALUE_PROP → [Your value prop]
- XXX_KEYWORDS → [From research]

## 📋 PHASE 4: Content Creation in Sanity (30 minutes)

### 4.1 Create Stage 1 Content via MCP
**CRITICAL: All content MUST be created in Sanity, NOT in static files!**

Using the MCP (sanity-quest), create content with context `["tractor-insurance-quest"]`:

#### Company Profiles
```groq
// Create company schema entries
{
  _type: "company",
  name: "NFU Mutual",
  slug: "nfu-mutual",
  contexts: ["tractor-insurance-quest"],
  categories: ["insurance", "agricultural"],
  description: "Leading UK agricultural insurer...",
  // etc.
}
```

#### Article Pages
```groq
// Create article schema entries
{
  _type: "article",
  title: "Tractor Insurance Guide 2025",
  slug: "tractor-insurance-guide",
  contexts: ["tractor-insurance-quest"],
  categories: ["guide", "insurance"],
  content: "Comprehensive guide content...",
  articleType: "guide",
  // etc.
}
```

#### Legal Pages
Create these as articles with articleType: "legal":
- Privacy Policy (slug: "privacy-policy")
- Terms of Service (slug: "terms-of-service")
- Disclaimer (slug: "disclaimer")
- About (slug: "about")
- Sitemap (slug: "sitemap")

### 4.2 Validate Content Creation
Query via MCP to ensure content exists:
```groq
*[_type in ["company", "article"] && "tractor-insurance-quest" in contexts] {
  title,
  slug
}
```

## 📋 PHASE 5: Astro Setup (20 minutes)

### 5.1 Initialize Astro Project
```bash
npm create astro@latest . -- --template minimal --yes
npm install @sanity/client @astrojs/react react react-dom
npx astro add tailwind --yes
```

### 5.2 Configure Sanity Client
Create `/src/lib/sanity.ts`:
```typescript
import { createClient } from '@sanity/client'

export const sanityClient = createClient({
  projectId: 'bc08ijz6',
  dataset: 'production',
  apiVersion: '2024-01-01',
  useCdn: false,
})
```

### 5.3 Create Dynamic Pages
**NEVER CREATE STATIC CONTENT!** Always query from Sanity:

```astro
---
// src/pages/[slug].astro
import { sanityClient } from '../lib/sanity'
import Layout from '../layouts/Layout.astro'

const { slug } = Astro.params

const page = await sanityClient.fetch(
  `*[_type in ["article", "company"] && 
    slug.current == $slug && 
    "tractor-insurance-quest" in contexts][0]`,
  { slug }
)

if (!page) {
  return Astro.redirect('/404')
}
---

<Layout title={page.title}>
  <!-- Render content from Sanity -->
  <article>{page.content}</article>
</Layout>
```

### 5.4 Create Footer Component
Use template from vanilla but ensure all links point to Sanity content:
```astro
---
// Query footer links from Sanity
const footerLinks = await sanityClient.fetch(
  `*[_type == "article" && 
    "tractor-insurance-quest" in contexts && 
    articleType in ["legal", "page"]] {
    title,
    "url": "/" + slug.current
  }`
)
---

<footer>
  <!-- Only show links that exist in Sanity -->
  {footerLinks.map(link => (
    <a href={link.url}>{link.title}</a>
  ))}
</footer>
```

## 📋 PHASE 6: Deployment (10 minutes)

### 6.1 Environment Variables
Create `.env`:
```env
PUBLIC_SANITY_PROJECT_ID=bc08ijz6
PUBLIC_SANITY_DATASET=production
PUBLIC_SANITY_API_VERSION=2024-01-01
SANITY_API_TOKEN=[Your token]
```

### 6.2 Git Setup
```bash
git init
git add .
git commit -m "Initial tractor-insurance-quest setup with Sanity CMS"
```

### 6.3 GitHub Repository
```bash
# Create repo (must match local name)
gh repo create tractor-insurance-quest --public --source=. --remote=origin --push
```

### 6.4 Vercel Deployment
```bash
VERCEL_TOKEN=gAYaR1sjB2NTXl4oYQ4CrmeY npx vercel --yes --prod --token gAYaR1sjB2NTXl4oYQ4CrmeY
```

## 📋 PHASE 7: Validation (5 minutes)

### 7.1 Content Checklist
- [ ] All content exists in Sanity (query via MCP)
- [ ] Workspace visible in Sanity Studio
- [ ] No static content in Astro files
- [ ] All pages query from Sanity

### 7.2 Link Validation
- [ ] Click every navigation link
- [ ] Click every footer link
- [ ] Test on mobile
- [ ] Check sitemap page

### 7.3 Documentation Check
- [ ] All docs prefixed with APP-NAME-
- [ ] All placeholders replaced
- [ ] RESTART.md has correct info
- [ ] CLAUDE.md has project specifics

### 7.4 Deployment Check
- [ ] Site live on Vercel
- [ ] Custom domain configured (if available)
- [ ] Environment variables set
- [ ] GitHub repo connected

## 🚨 COMMON MISTAKES TO AVOID

### Mistake #1: Creating Static Content
❌ WRONG:
```astro
<!-- src/pages/about.astro -->
<h1>About Us</h1>
<p>We are a tractor insurance company...</p>
```

✅ CORRECT:
```astro
<!-- src/pages/about.astro -->
const about = await sanityClient.fetch(
  `*[_type == "article" && slug.current == "about"][0]`
)
```

### Mistake #2: Forgetting Sanity Workspace
❌ WRONG: Jump straight to creating Astro pages
✅ CORRECT: Set up Sanity workspace FIRST

### Mistake #3: Not Prefixing Documentation
❌ WRONG: CLAUDE.md, RESTART.md
✅ CORRECT: TRACTOR-INSURANCE-QUEST-CLAUDE.md

### Mistake #4: Broken Footer Links
❌ WRONG: Hardcoded footer with non-existent pages
✅ CORRECT: Query footer links from Sanity

## 📊 Success Metrics

A successful Quest app launch has:
- ✅ Zero broken links
- ✅ All content in Sanity CMS
- ✅ Workspace in quest-cms Studio
- ✅ Prefixed documentation
- ✅ Dynamic content queries
- ✅ Working footer on every page
- ✅ Legal pages present
- ✅ Stage 1 content complete
- ✅ Deployed and live

## 💡 Time Estimates

- Research & Planning: 15 minutes
- Sanity Setup: 10 minutes
- Project Setup: 10 minutes
- Content Creation: 30 minutes
- Astro Setup: 20 minutes
- Deployment: 10 minutes
- Validation: 5 minutes
- **Total: ~100 minutes**

Compare to old method: 3-4 hours with high risk of broken links

## 🎯 Final Checklist

Before considering the app launched:
- [ ] I can edit all content in Sanity Studio
- [ ] No content is hardcoded in Astro files
- [ ] Every link on the site works
- [ ] Documentation is prefixed
- [ ] Site is deployed and live
- [ ] I can add new content via Sanity without touching code

---

**Remember: Content in Sanity FIRST, Astro queries SECOND. Never the other way around!**