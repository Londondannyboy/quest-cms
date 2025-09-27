# 🚀 CONTENT CREATION PROMPT - STAGED APPROACH

## Purpose
This document provides the exact process for creating content that has ZERO broken links through a staged creation approach with MCP validation.

## 🚨 CRITICAL WORKFLOW ORDER

### 1. IMAGES FIRST - Before Creating Any Content!
```javascript
// STEP 1: Check Media Library for existing image
const existing = await checkMediaLibrary('topic-name');

// STEP 2: If not found, create new
const image = existing || await createFromUnsplash('topic-name');

// STEP 3: THEN create content with image ready
const article = {
  featuredImage: image, // Already have it!
  // ... rest of content
}
```

### 2. MANDATORY FIELDS - Never Leave Empty
```javascript
{
  contexts: ['APP-NAME-quest'],  // CRITICAL - Never empty
  featuredImage: { ... },  // REQUIRED - Get image first
  thumbnailVideo: 'mux-playback-id',  // Optional - For video thumbnails
  categories: ['cat1', 'cat2'],  // Minimum 2 categories
  tags: ['tag1', 'tag2', 'tag3'],  // Minimum 3 tags
  publishedAt: new Date().toISOString(),  // Always set
  author: { _ref: 'editorial-team' },  // Create author first
  focusKeyword: 'primary keyword',  // Primary SEO keyword
  seoTitle: 'SEO Title - 60 chars max',
  metaDescription: 'Meta description - 160 chars max',
  excerpt: 'Summary - 200-300 chars'
}
```

### 3. PUBLISH IMMEDIATELY
- No drafts needed
- Click "Publish" right away
- Can always edit later

## 🎯 Content Creation Stages

### Stage 1: Foundation Pillar Content
**NO INTERNAL LINKS ALLOWED**

#### What to Create:
- Primary keyword target pages
- Comprehensive pillar content (2500+ words)
- Company profiles
- Main category pages
- Location guides

#### Rules for Stage 1:
1. **NO internal links** - Not a single one
2. **External links only** - Government, academic, authoritative sources
3. **Minimum 5 external citations** per piece
4. **Use Tavily for research** - Current data and statistics
5. **Use Critique Labs** - Fact-check all claims
6. **Quality score 85+** required

#### Stage 1 Creation Process:
```
1. Research with Tavily:
   - Search: "XXX_KEYWORD 2025 latest updates"
   - Search: "XXX_KEYWORD statistics data"
   - Search: "XXX_KEYWORD government regulations"

2. Create comprehensive content:
   - 2500+ words minimum
   - Multiple sections with headers
   - Data tables where relevant
   - External citations throughout

3. Validate with Critique Labs:
   - Fact-check all statistics
   - Verify government sources
   - Add inline citations

4. Set context in Sanity:
   contexts: ["XXX_APP_NAME"]
```

### Stage 2: Cluster Content
**ONLY LINKS TO STAGE 1**

#### What to Create:
- Supporting articles that expand on Stage 1
- Comparison pages
- How-to guides
- Industry overviews

#### Rules for Stage 2:
1. **Query MCP first** to get all Stage 1 slugs:
   ```groq
   *[_type in ["company", "article", "location"] 
     && "XXX_APP_NAME" in contexts] {
     slug,
     title
   }
   ```

2. **Only link to verified Stage 1 content**
3. **If slug doesn't exist, don't create the link**
4. **Can have multiple links to Stage 1**
5. **Still need external citations**

#### Stage 2 Link Validation:
```javascript
// Before creating any link to Stage 1:
const validSlugs = await mcp.query(
  '*[_type == "article" && "XXX_APP_NAME" in contexts].slug.current'
);

// Only create links to slugs in validSlugs array
if (validSlugs.includes("target-slug")) {
  // Safe to create link
  createLink("/target-slug");
} else {
  // Just mention without link
  createTextMention("See our guide on Topic X");
}
```

### Stage 3: Detail & News Content
**LINKS TO STAGES 1 & 2**

#### What to Create:
- News and updates
- Detailed case studies
- Blog posts
- FAQ pages
- Glossary entries

#### Rules for Stage 3:
1. **Query both Stage 1 and Stage 2 content**
2. **Can link freely to verified content**
3. **Shorter content acceptable** (1000+ words)
4. **Focus on long-tail keywords**

## 📊 Quality Scoring Formula

Every piece of content must score 80+ before publishing:

### Scoring Breakdown (0-100 points):

#### Content Depth (40 points max)
- 3000+ words: 40 points
- 2500+ words: 35 points
- 2000+ words: 30 points
- 1500+ words: 20 points
- 1000+ words: 10 points
- <1000 words: 0 points

#### Research Quality (25 points max)
- Tavily research used: +20 points
- 8+ external links: +5 points
- 5-7 external links: +3 points
- 1-4 external links: +1 point

#### AI Enhancement (20 points max)
- Critique Labs verification: +10 points
- Firecrawl PDF sources: +5 points
- LinkUp advanced search: +5 points

#### Currency/Freshness (15 points max)
- Current year data: +15 points
- Last year data: +10 points
- 2+ years old: +5 points

### Minimum Scores by Stage:
- **Stage 1**: 85+ required
- **Stage 2**: 80+ required
- **Stage 3**: 75+ acceptable

## 🔄 Batch Processing Instructions

### Daily Content Goals by Stage:

#### If Working on Stage 1:
- Create 3-5 pillar pages per day
- Each must be 2500+ words
- Full Tavily research required
- No internal links whatsoever

#### If Working on Stage 2:
- Create 5-7 cluster pages per day
- Query Stage 1 content first
- Link only to verified Stage 1
- 1500-2000 words each

#### If Working on Stage 3:
- Create 8-10 detail pages per day
- Can be shorter (1000+ words)
- Link to Stages 1 & 2 freely

## 📝 MCP Validation Queries

### Essential Queries for Safe Linking:

```groq
// Get all Stage 1 content (before creating Stage 2)
*[_type in ["company", "article", "location"] 
  && "XXX_APP_NAME" in contexts
  && defined(slug)] {
  _id,
  _type,
  title,
  "url": slug.current
}

// Check if specific slug exists (before creating any link)
*[_type == "article" 
  && slug.current == "your-target-slug"
  && "XXX_APP_NAME" in contexts][0]

// Get all content with quality scores
*[_type == "article" 
  && "XXX_APP_NAME" in contexts] {
  title,
  "score": qualityMetrics.qualityScore,
  "stage": metadata.contentStage
}
```

## 🛠️ Tool Usage Priority

### For Stage 1 Content:
1. **Tavily** - MANDATORY for research
2. **Critique Labs** - MANDATORY for fact-checking
3. **Firecrawl** - If PDF sources needed
4. **LinkUp** - For deep research (when available)

### For Stage 2 Content:
1. **MCP Queries** - MANDATORY to verify Stage 1
2. **Tavily** - For additional research
3. **Critique Labs** - For verification

### For Stage 3 Content:
1. **MCP Queries** - To verify Stages 1 & 2
2. **Tavily** - For news/updates
3. **AI Enhancement** - For content expansion

## ✅ Quality Checklist

### Before Publishing Any Content:

#### Stage 1 Checklist:
- [ ] Zero internal links
- [ ] 2500+ words
- [ ] 5+ external authoritative links
- [ ] Tavily research incorporated
- [ ] Critique Labs verification done
- [ ] Quality score 85+
- [ ] Context set to ["XXX_APP_NAME"]

#### Stage 2 Checklist:
- [ ] All Stage 1 links validated via MCP
- [ ] No links to non-existent content
- [ ] 1500+ words
- [ ] 3+ external links
- [ ] Quality score 80+
- [ ] Links only to Stage 1

#### Stage 3 Checklist:
- [ ] All links validated via MCP
- [ ] 1000+ words
- [ ] Quality score 75+
- [ ] Proper categorization

## 🚨 Critical Warnings

### NEVER:
- Create links without MCP validation
- Skip stages (no Stage 2 before Stage 1)
- Assume URL patterns exist
- Create placeholder links
- Link to content you haven't verified

### ALWAYS:
- Query MCP before any internal link
- Create content in stage order
- Use Tavily for Stage 1 research
- Track quality scores
- Validate, validate, validate

## 📊 Progress Tracking

### After Each Session Report:

```markdown
## Content Creation Report - [Date]

### Stage 1 Progress
- Created: X pillar pages
- Average quality score: XX
- Total Stage 1 pages: XX

### Stage 2 Progress
- Created: X cluster pages
- Links validated: 100%
- Total Stage 2 pages: XX

### Stage 3 Progress
- Created: X detail pages
- Total content pieces: XX

### Quality Metrics
- Average score all content: XX
- Lowest score: XX
- Content needing improvement: X pages
```

## 🎯 Success Metrics

- **Zero broken links** - Primary goal
- **Stage 1 average 85+** - SEO foundation
- **All content 80+** - Quality standard
- **100% link validation** - No assumptions
- **Full API usage** - Maximum quality

---

**Last Updated**: September 26, 2025
**Version**: 1.0 - Staged Content Creation
**Critical**: Follow stages exactly to prevent broken links