import { defineCliConfig } from 'sanity/cli'

export default defineCliConfig({
  api: {
    projectId: 'bc08ijz6',
    dataset: 'production',
  },
  studioHost: 'quest-cms',
  deployment: {
    appId: 'u1qnqwsivscba8morgwpkzv1',
  },
})