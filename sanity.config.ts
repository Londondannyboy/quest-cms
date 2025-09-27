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

// Shared configuration
const sharedConfig = {
  projectId: 'bc08ijz6',
  dataset: 'production',
  plugins: [structureTool(), visionTool()],
  schema: {
    types: allSchemas,
  }
}

// Multiple workspace configurations
export default defineConfig([
  {
    ...sharedConfig,
    name: 'default',
    title: 'Quest CMS - All Content',
    basePath: '/all',
  },
  {
    ...sharedConfig,
    name: 'relocation',
    title: 'Quest Relocation',
    basePath: '/relocation',
  },
  {
    ...sharedConfig,
    name: 'placement',
    title: 'Quest Placement',
    basePath: '/placement',
  },
  {
    ...sharedConfig,
    name: 'rainmaker',
    title: 'Quest Rainmaker',
    basePath: '/rainmaker',
  },
  {
    ...sharedConfig,
    name: 'chief',
    title: 'Quest Chief',
    basePath: '/chief',
  }
])