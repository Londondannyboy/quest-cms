# CLAUDE AI ASSISTANT GUIDELINES - QUEST CMS

## 🎯 PROJECT IDENTITY - CRITICAL
**IMPORTANT**: This is the QUEST CMS project. Always use these exact identifiers:

### Project Names & IDs
- **Project Name**: quest-cms (NOT quest-cms-temp, NOT cms-temp)
- **Local Directory**: `/Users/dankeegan/quest-cms/` (NEVER use /tmp/ or temporary directories)
- **GitHub Repository**: `https://github.com/Londondannyboy/quest-cms`
- **Vercel Project Name**: `quest-cms`
- **Vercel Project ID**: `prj_jTiwn8BA5yRK5lMb8utwnFDlp6O5`
- **Sanity Project ID**: `bc08ijz6` (renamed to "Quest" from "relocation-quest")
- **Sanity Dataset**: `production`

### 🚨 NEVER USE
- ❌ Temporary directories (/tmp/, /var/folders/)
- ❌ Different project names (quest-cms-temp, cms-test, etc.)
- ❌ Different GitHub repositories
- ❌ Different Vercel project IDs
- ❌ Local test deployments

## Project Overview
Quest CMS is the unified content management system for ALL Quest platform applications. It provides universal schemas that work across multiple Quest websites while maintaining clean separation through contexts and categories.

### Architecture
- **Single Sanity Project**: bc08ijz6 (saves $60/month vs separate projects)
- **Multiple Workspaces**: One CMS, multiple views
- **Universal Schemas**: Write once, use everywhere
- **Context-Based Filtering**: Each app queries its own content

## Universal Schemas

### Core Schemas
1. **Company** (`schemas/universal/company.ts`)
   - Universal entity with array categories and contexts
   - Primary type + multiple categories
   - Flexible metrics object

2. **Person** (`schemas/universal/person.ts`)
   - Seniority levels from entry to C-suite
   - Expertise areas array
   - Company associations

3. **Job** (`schemas/universal/job.ts`)
   - Universal job postings
   - Department and seniority categorization
   - Compensation structure

4. **Article** (`schemas/universal/article.ts`)
   - Multi-purpose content type
   - Article types (news, guide, tutorial, etc.)
   - Category arrays for cross-app use

5. **Location** (`schemas/universal/location.ts`)
   - Geographic data with statistics
   - Living and business information
   - Featured location support

6. **Tag** (`schemas/universal/tag.ts`)
   - Flexible tagging system
   - Category-based organization
   - Color coding support

## Workspace Configuration

### Available Workspaces
- `/all` - Quest CMS All Content (everything)
- `/relocation` - Quest Relocation content
- `/placement` - Quest Placement content
- `/rainmaker` - Quest Rainmaker content
- `/chief` - Quest Chief content

## Development Commands
```bash
# ALWAYS work in this directory
cd /Users/dankeegan/quest-cms

# Development
npm run dev          # Start development server
npm run build        # Build for production
npm run deploy       # Deploy to Sanity

# Git operations - ALWAYS use this repository
git push origin main # Push to https://github.com/Londondannyboy/quest-cms

# Deployment - ALWAYS use this Vercel project
VERCEL_TOKEN=gAYaR1sjB2NTXl4oYQ4CrmeY npx vercel --prod --yes --token gAYaR1sjB2NTXl4oYQ4CrmeY
```

## Environment Variables
```env
PUBLIC_SANITY_PROJECT_ID=bc08ijz6
PUBLIC_SANITY_DATASET=production
PUBLIC_SANITY_API_VERSION=2024-01-01
SANITY_API_TOKEN=skZw5uQGgMH9HxvfdqhJzhpty93mtuaynRDkprQ4yAzBrAQOKEgb3iCYkk4dafiOTxaozS1J9apEhlPVGLMtIlYFFnQijQy0rX4WDTRuXQmPgEsPNGrc0D2EqXa3WFGgjKmYCTpMrXtGf7n2xbFM6L3lhSoJ7GYcNnL0IiUMUClYGaxo21dA
```

## Query Examples

### Context-Based Queries
```javascript
// Get companies for specific app
*[_type == "company" && "quest-relocation" in contexts]
*[_type == "company" && "quest-placement" in contexts]

// Get articles by category
*[_type == "article" && "visa-immigration" in categories]

// Get featured content
*[_type == "article" && featured == true && "quest-relocation" in contexts]
```

## Related Applications Using This CMS

1. **quest-relocation**
   - Repository: https://github.com/Londondannyboy/relocation-quest
   - Production: https://relocation.quest
   - Studio: https://relocation-quest.sanity.studio (Original blog content)
   - Integration: Hybrid approach - queries both old and universal schemas

2. **quest-placement**
   - Repository: https://github.com/Londondannyboy/placement-quest
   - Production: https://placement.quest

3. **quest-rainmaker** (future)
   - Production: https://rainmakrr.com

4. **quest-chief** (future)
   - TBD

5. **quest-auth** (future)
   - Authentication system

## MCP Server Configuration
The MCP server 'sanity-quest' is configured and working:
```json
{
  "sanity-quest": {
    "command": "npx",
    "args": ["-y", "@sanity/mcp-server@latest"],
    "env": {
      "SANITY_PROJECT_ID": "bc08ijz6",
      "SANITY_DATASET": "production",
      "SANITY_API_TOKEN": "skZw5uQGgMH9HxvfdqhJzhpty93mtuaynRDkprQ4yAzBrAQOKEgb3iCYkk4dafiOTxaozS1J9apEhlPVGLMtIlYFFnQijQy0rX4WDTRuXQmPgEsPNGrc0D2EqXa3WFGgjKmYCTpMrXtGf7n2xbFM6L3lhSoJ7GYcNnL0IiUMUClYGaxo21dA"
    }
  }
}
```

## Important Notes
1. **NEVER** create temporary projects or use /tmp directories
2. **ALWAYS** use the exact project IDs listed above
3. **ALWAYS** work in `/Users/dankeegan/quest-cms/`
4. **ALWAYS** push to the correct GitHub repository
5. **ALWAYS** deploy to the correct Vercel project

## Success Metrics
- ✅ Single Sanity project ($15/month vs $75/month)
- ✅ Universal schemas (no duplication)
- ✅ Simple architecture (no Turborepo needed)
- ✅ Flexible categorization (contexts & categories)
- ✅ Future-proof (easy to add new Quest apps)

---
**Last Updated**: September 26, 2025
**Project Status**: Active Development
**Priority**: Deploy and integrate with existing Quest apps
**GitHub**: https://github.com/Londondannyboy/quest-cms
**Vercel Project ID**: prj_jTiwn8BA5yRK5lMb8utwnFDlp6O5