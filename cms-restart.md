# 🎯 Quest CMS - Unified Content Management System

## Project Overview
Quest CMS is the centralized content management system for all Quest platform applications. It provides universal schemas that can be used across multiple Quest websites while maintaining clean separation and smart categorization.

## 📁 CRITICAL: Project Location
**Local Directory**: `/Users/dankeegan/quest-cms/`
**Sanity Project ID**: `bc08ijz6` (formerly relocation-quest, now renamed to "Quest")
**Dataset**: `production`
**MCP Server Name**: `sanity-quest`

## 🏗️ Architecture Decisions

### Why This Architecture?
- **Single Sanity Project** = $15/month instead of $75/month for 5 projects
- **Universal Schemas** = Write once, use everywhere
- **Flexible Categorization** = Same company can serve different contexts
- **Simple Maintenance** = 5 apps × 2 schema changes/year = 50 minutes/year of updates
- **No Over-Engineering** = No Turborepo, no complex monorepo, just simple and clean

### Key Design Principles
1. **Universal First**: Every schema is designed to work across all apps
2. **Categories as Arrays**: Companies/people can have multiple categories
3. **Context-Aware**: Each entity knows which apps use it
4. **Query-Based Separation**: Apps filter content via queries, not separate schemas

## 📋 Universal Schema Structure

### Core Entities (Used Everywhere)
```
schemas/
├── universal/
│   ├── company.ts      # Universal company with categories
│   ├── person.ts       # Universal person with seniority
│   ├── job.ts          # Universal job postings
│   ├── article.ts      # Universal content/news
│   ├── location.ts     # Geographic data
│   └── tag.ts          # Flexible tagging
```

### Company Schema (Master Entity)
```typescript
{
  name: 'company',
  fields: [
    // Core
    name: string (required)
    slug: slug
    website: url
    description: text
    
    // Categorization (THE KEY!)
    primaryType: string (dropdown)
      - Placement Agent, VC Firm, Law Firm, etc.
    
    categories: array (multiple selections)
      - M&A Advisory, Immigration Services, Property Services, etc.
    
    contexts: array (which apps use this)
      - quest-relocation, quest-placement, quest-rainmaker, etc.
    
    // Metrics (flexible)
    metrics: {
      aumRaised: number
      dealsCompleted: number
      fundSize: number
      successRate: number
    }
  ]
}
```

### Person Schema (Universal)
```typescript
{
  name: 'person',
  fields: [
    name: string
    title: string
    company: reference(Company)
    seniority: string (Junior/Senior/Executive/C-Suite)
    contexts: array (which apps)
    linkedinUrl: url
  ]
}
```

## 🔧 Workspace Configuration

### Sanity Workspaces (One Project, Multiple Views)
```javascript
// sanity.config.ts
[
  { name: 'quest-relocation', schemas: [company, person, article, location] },
  { name: 'quest-placement', schemas: [company, person, job, article] },
  { name: 'quest-rainmaker', schemas: [company, person, article] },
  { name: 'quest-chief', schemas: [person, job, article] },
  { name: 'quest-all', schemas: [...allSchemas] }
]
```

### How Apps Query Their Content
```javascript
// quest-relocation:
*[_type == "company" && "quest-relocation" in contexts]

// quest-placement:
*[_type == "company" && primaryType in ["Placement Agent", "VC Firm"]]

// quest-rainmaker:
*[_type == "company" && categories[] match "Investment*"]
```

## 🚀 Implementation Plan

### Phase 1: Setup Quest CMS (Current)
1. ✅ Create `/Users/dankeegan/quest-cms/` directory
2. ✅ Create this cms-restart.md file
3. Move existing schemas from relocation-quest
4. Create universal schemas

### Phase 2: Create Universal Schemas
1. Company schema with array categories
2. Person schema with seniority levels
3. Job, Article, Location schemas
4. Configure all with contexts field

### Phase 3: Configure Workspaces
1. Setup sanity.config.ts with all workspaces
2. Each workspace shows relevant schemas
3. Deploy to existing bc08ijz6 project

### Phase 4: Update Existing Apps
1. Update relocation-quest to use universal schemas
2. Update placement-quest to use universal schemas
3. Remove local schema definitions from apps

### Phase 5: Documentation & Testing
1. Create batch-prompt templates per workspace
2. Document categorization standards
3. Test cross-app content queries

## 💡 Key Insights from Planning

### What We Learned:
1. **Schemas rarely change** - CMS content schemas are stable unlike database tables
2. **Everything is universal** - No need for app-specific schemas, just use categories
3. **Simple beats complex** - Manual sync 2x/year beats Turborepo complexity
4. **Arrays solve everything** - Multiple categories per company solves context problem

### What We Avoided:
- ❌ Turborepo (unnecessary for 5 apps)
- ❌ Separate Sanity projects ($$$)
- ❌ Complex monorepo (cognitive overload)
- ❌ Over-specialized schemas

## 📊 Current Status

### ✅ Completed
- Project directory created
- Architecture decisions finalized
- Universal schema design complete
- Workspace strategy defined

### 🚧 Next Steps
1. Initialize npm project
2. Install Sanity dependencies
3. Create universal schemas
4. Configure workspaces
5. Deploy to bc08ijz6

## 🔑 Important Information

### Sanity Project
- **Project Name**: Quest (renamed from relocation-quest)
- **Project ID**: `bc08ijz6`
- **Dataset**: `production`
- **Studio URL**: Will be at quest-cms.vercel.app/studio

### MCP Configuration
```json
{
  "sanity-quest": {
    "command": "npx",
    "args": ["-y", "@sanity/mcp-server@latest"],
    "env": {
      "SANITY_PROJECT_ID": "bc08ijz6",
      "SANITY_DATASET": "production",
      "SANITY_API_TOKEN": "[TOKEN]"
    }
  }
}
```

### Related Apps Using This CMS
1. **quest-relocation** (formerly relocation-quest) - Visa/relocation content
2. **quest-placement** (formerly placement-quest) - Placement agent content
3. **quest-rainmaker** (future) - VC/PE content
4. **quest-chief** (future) - Executive/EA content
5. **quest-auth** (future) - Authentication/user management

## 📝 Quick Commands

```bash
# Start fresh
cd /Users/dankeegan/quest-cms
npm init -y
npm install sanity@latest @sanity/vision@latest

# Deploy schemas
npx sanity deploy

# Start development
npm run dev
```

## 🎯 Success Metrics
- ✅ One Sanity project for all apps ($15/month)
- ✅ Universal schemas (no duplication)
- ✅ Simple architecture (easy to understand)
- ✅ Flexible categorization (contexts & categories)
- ✅ Future-proof (easy to add quest-voice, quest-calculator, etc.)

---
**Document Created**: September 26, 2025
**Project Phase**: Initial Setup
**Next Action**: Initialize npm and create universal schemas