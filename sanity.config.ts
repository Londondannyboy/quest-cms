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
export default defineConfig([
  {
    name: 'quest-all',
    title: 'Quest CMS - All Content',
    projectId: 'bc08ijz6',
    dataset: 'production',
    basePath: '/all',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: allSchemas,
    },
    document: {
      newDocumentOptions: (prev, { creationContext }) => {
        return prev
      },
    },
  },
  {
    name: 'quest-relocation',
    title: 'Quest Relocation',
    projectId: 'bc08ijz6',
    dataset: 'production',
    basePath: '/relocation',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: [company, person, article, location, tag],
    },
    document: {
      newDocumentOptions: (prev, { creationContext }) => {
        // Filter to show only relevant document types
        return prev.filter((templateItem) => 
          ['company', 'person', 'article', 'location', 'tag'].includes(templateItem.templateId)
        )
      },
    },
  },
  {
    name: 'quest-placement',
    title: 'Quest Placement',
    projectId: 'bc08ijz6',
    dataset: 'production',
    basePath: '/placement',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: [company, person, job, article, tag],
    },
    document: {
      newDocumentOptions: (prev, { creationContext }) => {
        return prev.filter((templateItem) => 
          ['company', 'person', 'job', 'article', 'tag'].includes(templateItem.templateId)
        )
      },
    },
  },
  {
    name: 'quest-rainmaker',
    title: 'Quest Rainmaker',
    projectId: 'bc08ijz6',
    dataset: 'production',
    basePath: '/rainmaker',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: [company, person, article, tag],
    },
    document: {
      newDocumentOptions: (prev, { creationContext }) => {
        return prev.filter((templateItem) => 
          ['company', 'person', 'article', 'tag'].includes(templateItem.templateId)
        )
      },
    },
  },
  {
    name: 'quest-chief',
    title: 'Quest Chief',
    projectId: 'bc08ijz6',
    dataset: 'production',
    basePath: '/chief',
    plugins: [structureTool(), visionTool()],
    schema: {
      types: [person, job, article, tag],
    },
    document: {
      newDocumentOptions: (prev, { creationContext }) => {
        return prev.filter((templateItem) => 
          ['person', 'job', 'article', 'tag'].includes(templateItem.templateId)
        )
      },
    },
  },
])