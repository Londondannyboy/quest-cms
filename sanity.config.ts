import { defineConfig } from 'sanity'
import { structureTool } from 'sanity/structure'
import { visionTool } from '@sanity/vision'

// Import schemas
import company from './schemas/universal/company'
import person from './schemas/universal/person'
import job from './schemas/universal/job'
import article from './schemas/universal/article'
import location from './schemas/universal/location'
import tag from './schemas/universal/tag'

// All schemas
const allSchemas = [company, person, job, article, location, tag]

// Workspace configurations
export default defineConfig({
    name: 'default',
    title: 'Quest CMS',
    projectId: 'bc08ijz6',
    dataset: 'production',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: allSchemas,
    }
})