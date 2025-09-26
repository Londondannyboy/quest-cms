# Quest CMS Migration Guide

## Overview
This guide explains how to migrate existing Quest applications to use the universal schemas from Quest CMS.

## Current Status

### ✅ Completed
- **Quest CMS**: Fully deployed with universal schemas at https://quest-cms.sanity.studio/
- **Relocation Quest**: Successfully integrated with universal schemas (hybrid approach)
- **MCP Server**: Working perfectly with Sanity-hosted studios

### 🚧 Pending Migration
- placement-quest
- quest-rainmaker (future)
- quest-chief (future)

## Migration Strategy

### Option 1: Hybrid Approach (Recommended)
**Used in relocation.quest** - Keep existing content working while adding universal content

1. **Keep existing schemas** - Don't delete current content types
2. **Add universal queries** - Query new content types alongside old ones
3. **Gradual transition** - Move content to universal schemas over time
4. **No breaking changes** - Site continues working throughout migration

### Option 2: Full Migration
Complete replacement of existing schemas with universal ones

1. **Export existing content** - Backup all current data
2. **Map to universal schemas** - Transform data to new structure
3. **Import to Quest CMS** - Use universal content types
4. **Update all queries** - Replace old queries with universal ones

## Implementation Steps (Hybrid Approach)

### 1. Create Query Helper
```typescript
// src/lib/universalQueries.ts
import { sanityClient } from 'sanity:client';

export async function getUniversalContent(type: string, context: string) {
  return await sanityClient.fetch(`
    *[_type == "${type}" && "${context}" in contexts]
  `);
}
```

### 2. Add Universal Component
```astro
// src/components/UniversalContent.astro
---
import { hasUniversalContent } from '../lib/universalQueries';
const hasContent = await hasUniversalContent();
---

{hasContent && (
  <!-- Display universal content -->
)}
```

### 3. Update Pages
Add UniversalContent component to existing pages:
```astro
import UniversalContent from '../components/UniversalContent.astro';

<!-- Existing content -->
<ExistingContent />

<!-- Universal content -->
<UniversalContent />
```

## Context Mapping

### For placement-quest
- Set context: `['quest-placement']`
- Primary types: `placement-agent`, `vc-firm`, `private-equity`
- Focus on: company, person, job schemas

### For quest-rainmaker
- Set context: `['quest-rainmaker']`
- Primary types: `vc-firm`, `private-equity`, `consultancy`
- Focus on: company, person, article schemas

### For quest-chief
- Set context: `['quest-chief']`
- Primary types: All types relevant
- Focus on: person, job, article schemas

## Query Examples

### Get Companies by Context
```groq
*[_type == "company" && "quest-placement" in contexts] {
  name,
  slug,
  primaryType,
  categories
}
```

### Get Articles by Category
```groq
*[_type == "article" && "fund-placement" in categories] {
  title,
  slug,
  excerpt,
  publishedAt
}
```

### Get People by Expertise
```groq
*[_type == "person" && "private-equity" in expertise] {
  name,
  title,
  company->
}
```

## Benefits of Universal Schemas

### 1. Content Reusability
- Same company can appear in multiple apps
- Articles can be shared across platforms
- People profiles work everywhere

### 2. Centralized Management
- Single source of truth
- Update once, reflect everywhere
- Consistent data structure

### 3. Cost Efficiency
- One Sanity project ($15/month)
- Shared infrastructure
- Reduced maintenance

### 4. Flexibility
- Easy to add new apps
- Simple to adjust contexts
- Categories can evolve

## Testing Checklist

- [ ] Universal queries return data
- [ ] Context filtering works correctly
- [ ] Existing content still displays
- [ ] No broken pages or queries
- [ ] Performance is acceptable

## Troubleshooting

### No Universal Content Showing
1. Check context is set correctly in content
2. Verify query includes correct context filter
3. Ensure content status is 'published' or 'active'

### Query Errors
1. Check schema name matches exactly
2. Verify field names are correct
3. Test query in Sanity Vision tool first

### Performance Issues
1. Add pagination to queries
2. Use projection to limit fields
3. Implement caching strategy

## Support

For questions or issues:
1. Check Quest CMS studio: https://quest-cms.sanity.studio/
2. Test queries in Vision tool
3. Review this migration guide

---
**Last Updated**: September 26, 2025
**Status**: Active Migration