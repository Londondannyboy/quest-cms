# Quest CMS - Phase 3 Restart Prompt

## Context for New Session

I'm working on Quest CMS, a unified content management system for multiple Quest platform websites. Please read the CMS-RESTART.md file in /Users/dankeegan/quest-cms/ which contains the complete project context and what we've accomplished.

## Current Status (September 26, 2025)

### ✅ Completed in Phase 2:
1. **Quest CMS deployed** with universal schemas at https://quest-cms.sanity.studio/
2. **Relocation Quest integrated** using hybrid approach (queries both old and new schemas)
3. **Studios migrated** to Sanity hosting for better MCP access
4. **MCP server working** - no more timeouts with Sanity-hosted studios
5. **Documentation complete** - All files prefixed with CMS- (except CLAUDE.md)

### 🏗️ Current Architecture:
- **Sanity Project ID**: bc08ijz6 (shared across all studios)
- **Quest CMS Studio**: https://quest-cms.sanity.studio/ (Universal schemas)
- **Relocation Quest Studio**: https://relocation-quest.sanity.studio/ (Original blog)
- **Live Sites**: relocation.quest (hybrid), placement.quest (ready for migration)

### 📁 Key Files to Review:
1. **CMS-RESTART.md** - Complete project plan and accomplishments
2. **CMS-FINAL-ARCHITECTURE.md** - Current architecture overview
3. **CMS-MIGRATION-GUIDE.md** - How to migrate other Quest apps
4. **CLAUDE.md** - Your operating instructions for this project

## Phase 3 Objectives (Next Steps)

### Option A: Content Population
Help me populate the Quest CMS with universal content:
- Create companies with 'quest-relocation' and 'quest-placement' contexts
- Add people/experts in various fields
- Create location guides for major destinations
- Build out job listings

### Option B: Placement Quest Migration
Migrate placement.quest to use universal schemas:
- Implement hybrid approach like relocation.quest
- Keep existing placement agent schemas working
- Add universal content queries
- Test cross-app content sharing

### Option C: New App Launch
Help launch quest-rainmaker or quest-chief:
- Use universal schemas from day one
- No legacy content to migrate
- Pure implementation of the universal CMS strategy

### Option D: Content Automation
Set up automated content pipelines:
- News aggregation for articles
- API integrations for job listings
- Scheduled content publishing
- AI-enhanced content generation

## Important Technical Details

### Universal Schema Query Pattern:
```groq
// Always filter by context
*[_type == "company" && "quest-relocation" in contexts]

// Categories are arrays
*[_type == "article" && "visa-immigration" in categories]
```

### MCP Server Configuration:
- Name: sanity-quest
- Project ID: bc08ijz6
- Works perfectly with Sanity-hosted studios

### GitHub Repositories:
- Quest CMS: https://github.com/Londondannyboy/quest-cms
- Relocation Quest: https://github.com/Londondannyboy/relocation-quest
- Placement Quest: https://github.com/Londondannyboy/placement-quest

### Deployment:
- All sites auto-deploy via Vercel on git push
- Vercel Token: gAYaR1sjB2NTXl4oYQ4CrmeY

## Starting the Session

Please acknowledge that you've read the context files and understand:
1. The universal schema structure with contexts and categories
2. The hybrid approach for migrations
3. The current architecture with Sanity-hosted studios
4. The MCP server is working correctly

Then ask me which Phase 3 objective (A, B, C, or D) I'd like to focus on, or if there's something else I need help with.

---

**Note**: The /studio routes on websites are deprecated. We use Sanity-hosted studios now:
- ❌ relocation.quest/studio (broken, ignore)
- ✅ relocation-quest.sanity.studio (use this)
- ✅ quest-cms.sanity.studio (use this)