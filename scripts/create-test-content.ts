import { createClient } from '@sanity/client'

// Initialize Sanity client
const client = createClient({
  projectId: 'bc08ijz6',
  dataset: 'production',
  useCdn: false,
  apiVersion: '2024-01-01',
  token: process.env.SANITY_API_TOKEN || 'skZw5uQGgMH9HxvfdqhJzhpty93mtuaynRDkprQ4yAzBrAQOKEgb3iCYkk4dafiOTxaozS1J9apEhlPVGLMtIlYFFnQijQy0rX4WDTRuXQmPgEsPNGrc0D2EqXa3WFGgjKmYCTpMrXtGf7n2xbFM6L3lhSoJ7GYcNnL0IiUMUClYGaxo21dA',
})

async function createTestContent() {
  console.log('Creating test content for Quest CMS...')

  try {
    // Create test locations
    const london = await client.create({
      _type: 'location',
      name: 'London, United Kingdom',
      slug: { current: 'london-uk' },
      city: 'London',
      country: 'United Kingdom',
      countryCode: 'GB',
      region: 'europe',
      description: 'Capital city of the United Kingdom and major global financial center',
      businessHub: true,
      techHub: true,
      contexts: ['quest-relocation', 'quest-placement', 'quest-rainmaker'],
      featured: true,
      status: 'active',
    })

    const newYork = await client.create({
      _type: 'location',
      name: 'New York, USA',
      slug: { current: 'new-york-usa' },
      city: 'New York',
      state: 'New York',
      country: 'United States',
      countryCode: 'US',
      region: 'north-america',
      description: 'Global financial capital and largest city in the United States',
      businessHub: true,
      techHub: true,
      contexts: ['quest-relocation', 'quest-placement', 'quest-rainmaker'],
      featured: true,
      status: 'active',
    })

    console.log('✅ Created locations:', london._id, newYork._id)

    // Create test companies
    const campbellLutyens = await client.create({
      _type: 'company',
      name: 'Campbell Lutyens',
      slug: { current: 'campbell-lutyens' },
      website: 'https://www.campbelllutyens.com',
      description: 'Leading global placement agent for private equity, infrastructure, and real estate funds',
      primaryType: 'placement-agent',
      categories: ['fund-placement', 'capital-raising', 'ma-advisory'],
      contexts: ['quest-placement', 'quest-rainmaker'],
      locations: [{ _ref: london._id }, { _ref: newYork._id }],
      metrics: {
        aumRaised: 150,
        dealsCompleted: 500,
        yearsInBusiness: 35,
      },
      status: 'active',
    })

    const pwc = await client.create({
      _type: 'company',
      name: 'PwC',
      slug: { current: 'pwc' },
      website: 'https://www.pwc.com',
      description: 'Global professional services network offering tax, immigration, and advisory services',
      primaryType: 'accounting-firm',
      categories: ['tax-advisory', 'immigration-services', 'consulting'],
      contexts: ['quest-relocation', 'quest-placement'],
      locations: [{ _ref: london._id }, { _ref: newYork._id }],
      metrics: {
        teamSize: 364000,
        yearsInBusiness: 175,
      },
      status: 'active',
    })

    console.log('✅ Created companies:', campbellLutyens._id, pwc._id)

    // Create test people
    const johndoe = await client.create({
      _type: 'person',
      name: 'John Doe',
      slug: { current: 'john-doe' },
      title: 'Managing Partner',
      bio: 'Senior placement agent with 20+ years experience in private equity fundraising',
      company: { _ref: campbellLutyens._id },
      seniority: 'partner',
      expertise: ['private-equity', 'fund-placement', 'capital-markets'],
      contexts: ['quest-placement', 'quest-rainmaker'],
      location: { _ref: london._id },
      metrics: {
        yearsExperience: 20,
        dealsCompleted: 100,
        totalValueManaged: 5000,
      },
      status: 'active',
    })

    const janesmith = await client.create({
      _type: 'person',
      name: 'Jane Smith',
      slug: { current: 'jane-smith' },
      title: 'Immigration Partner',
      bio: 'Expert in global mobility and corporate immigration',
      company: { _ref: pwc._id },
      seniority: 'partner',
      expertise: ['immigration-law', 'tax-advisory', 'corporate-law'],
      contexts: ['quest-relocation'],
      location: { _ref: newYork._id },
      metrics: {
        yearsExperience: 15,
        clientsServed: 500,
      },
      status: 'active',
    })

    console.log('✅ Created people:', johndoe._id, janesmith._id)

    // Create test job
    const job = await client.create({
      _type: 'job',
      title: 'Senior Placement Agent',
      slug: { current: 'senior-placement-agent-campbell-lutyens' },
      company: { _ref: campbellLutyens._id },
      description: [
        {
          _type: 'block',
          children: [
            {
              _type: 'span',
              text: 'We are seeking an experienced placement agent to join our London team.',
            },
          ],
        },
      ],
      jobType: 'full-time',
      workMode: 'hybrid',
      seniorityLevel: 'senior',
      department: 'sales',
      location: { _ref: london._id },
      compensation: {
        salaryMin: 150000,
        salaryMax: 250000,
        currency: 'GBP',
        salaryPeriod: 'year',
        equity: true,
      },
      contexts: ['quest-placement', 'quest-chief'],
      status: 'active',
    })

    console.log('✅ Created job:', job._id)

    // Create test article
    const article = await client.create({
      _type: 'article',
      title: 'The Ultimate Guide to UK Visa Applications',
      slug: { current: 'uk-visa-guide' },
      excerpt: 'Everything you need to know about applying for a UK visa, from skilled worker to investor visas.',
      articleType: 'guide',
      categories: ['visa-immigration', 'living-abroad'],
      contexts: ['quest-relocation'],
      author: { _ref: janesmith._id },
      relatedCompanies: [{ _ref: pwc._id }],
      relatedLocations: [{ _ref: london._id }],
      content: [
        {
          _type: 'block',
          children: [
            {
              _type: 'span',
              text: 'This comprehensive guide covers all aspects of UK visa applications for professionals and investors.',
            },
          ],
        },
      ],
      featured: true,
      status: 'published',
      publishedAt: new Date().toISOString(),
    })

    console.log('✅ Created article:', article._id)

    // Create test tags
    const tags = await Promise.all([
      client.create({
        _type: 'tag',
        name: 'Private Equity',
        slug: { current: 'private-equity' },
        category: 'industry',
        contexts: ['quest-placement', 'quest-rainmaker'],
        color: '#3B82F6',
        priority: 10,
        status: 'active',
      }),
      client.create({
        _type: 'tag',
        name: 'Immigration',
        slug: { current: 'immigration' },
        category: 'topic',
        contexts: ['quest-relocation'],
        color: '#10B981',
        priority: 8,
        status: 'active',
      }),
      client.create({
        _type: 'tag',
        name: 'London',
        slug: { current: 'london' },
        category: 'location',
        contexts: ['all'],
        color: '#EF4444',
        priority: 5,
        status: 'active',
      }),
    ])

    console.log('✅ Created tags:', tags.map(t => t._id).join(', '))

    console.log('\n🎉 Test content created successfully!')
    console.log('You can view it at: https://quest-cms.sanity.studio/all')
  } catch (error) {
    console.error('❌ Error creating test content:', error)
    process.exit(1)
  }
}

// Run the script
createTestContent()