const { createClient } = require('@sanity/client')

// Configure the client
const client = createClient({
  projectId: 'bc08ijz6',
  dataset: 'production',
  token: 'skZw5uQGgMH9HxvfdqhJzhpty93mtuaynRDkprQ4yAzBrAQOKEgb3iCYkk4dafiOTxaozS1J9apEhlPVGLMtIlYFFnQijQy0rX4WDTRuXQmPgEsPNGrc0D2EqXa3WFGgjKmYCTpMrXtGf7n2xbFM6L3lhSoJ7GYcNnL0IiUMUClYGaxo21dA',
  apiVersion: '2024-01-01',
  useCdn: false
})

async function createTestContent() {
  console.log('Starting to create test content...')
  
  try {
    // 1. Create Locations
    console.log('Creating locations...')
    
    const londonLocation = await client.create({
      _type: 'location',
      name: 'London, United Kingdom',
      slug: { current: 'london-uk' },
      city: 'London',
      country: 'United Kingdom',
      countryCode: 'GB',
      region: 'europe',
      coordinates: {
        lat: 51.5074,
        lng: -0.1278
      },
      timezone: 'Europe/London',
      description: 'Capital city of the United Kingdom and a major global financial center.',
      locationType: 'capital',
      businessHub: true,
      techHub: true,
      statistics: {
        population: 9000000,
        averageSalary: 55000,
        costOfLivingIndex: 85,
        qualityOfLifeIndex: 8.2,
        safetyIndex: 75,
        englishProficiency: 100
      },
      livingInfo: {
        averageRent: 2500,
        publicTransport: 'excellent',
        internationalSchools: 50,
        hospitals: 15,
        expatCommunity: 'very-large'
      },
      businessInfo: {
        corporateTaxRate: 25,
        personalTaxRate: 45,
        easeOfBusiness: 85,
        startupEcosystem: 'world-class'
      },
      contexts: ['quest-relocation', 'quest-placement'],
      seo: {
        metaTitle: 'London, UK - Relocation Guide',
        metaDescription: 'Complete guide to relocating to London, UK with visa information, housing, and more.',
        keywords: ['London', 'UK relocation', 'visa', 'housing']
      },
      featured: true,
      status: 'active'
    })
    
    const newYorkLocation = await client.create({
      _type: 'location',
      name: 'New York, USA',
      slug: { current: 'new-york-usa' },
      city: 'New York',
      state: 'New York',
      country: 'United States',
      countryCode: 'US',
      region: 'north-america',
      coordinates: {
        lat: 40.7128,
        lng: -74.0060
      },
      timezone: 'America/New_York',
      description: 'The most populous city in the United States and a global financial center.',
      locationType: 'major-city',
      businessHub: true,
      techHub: true,
      statistics: {
        population: 8400000,
        averageSalary: 75000,
        costOfLivingIndex: 100,
        qualityOfLifeIndex: 7.8,
        safetyIndex: 70,
        englishProficiency: 100
      },
      livingInfo: {
        averageRent: 3500,
        publicTransport: 'good',
        internationalSchools: 25,
        hospitals: 20,
        expatCommunity: 'very-large'
      },
      businessInfo: {
        corporateTaxRate: 21,
        personalTaxRate: 37,
        easeOfBusiness: 90,
        startupEcosystem: 'world-class'
      },
      contexts: ['quest-relocation', 'quest-placement'],
      seo: {
        metaTitle: 'New York, USA - Relocation Guide',
        metaDescription: 'Complete guide to relocating to New York, USA with visa information, housing, and more.',
        keywords: ['New York', 'USA relocation', 'visa', 'housing']
      },
      featured: true,
      status: 'active'
    })
    
    console.log('✅ Created locations:', londonLocation._id, newYorkLocation._id)
    
    // 2. Create Companies
    console.log('Creating companies...')
    
    const campbellLutyens = await client.create({
      _type: 'company',
      name: 'Campbell Lutyens',
      slug: { current: 'campbell-lutyens' },
      website: 'https://www.campbelllutyens.com',
      description: 'Leading global investment banking boutique specializing in fund placement and secondary transactions.',
      primaryType: 'placement-agent',
      categories: ['fund-placement', 'capital-raising', 'investment-banking'],
      contexts: ['quest-placement', 'quest-rainmaker'],
      contactInfo: {
        email: 'info@campbelllutyens.com',
        phone: '+44 20 7292 4200',
        address: '1 King William Street, London, EC4N 7AF, UK',
        linkedinUrl: 'https://www.linkedin.com/company/campbell-lutyens'
      },
      locations: [londonLocation._id],
      metrics: {
        aumRaised: 150,
        dealsCompleted: 250,
        yearsInBusiness: 25,
        teamSize: 180,
        clientsServed: 500
      },
      seo: {
        metaTitle: 'Campbell Lutyens - Placement Agent',
        metaDescription: 'Leading global placement agent specializing in fund placement and secondary transactions.',
        keywords: ['Campbell Lutyens', 'placement agent', 'fund placement', 'private equity']
      },
      status: 'active'
    })
    
    const pwc = await client.create({
      _type: 'company',
      name: 'PwC',
      slug: { current: 'pwc' },
      website: 'https://www.pwc.com',
      description: 'Global professional services network providing audit, consulting, tax and immigration services.',
      primaryType: 'accounting-firm',
      categories: ['tax-advisory', 'immigration-services', 'legal-services', 'consulting'],
      contexts: ['quest-relocation', 'quest-placement'],
      contactInfo: {
        email: 'info@pwc.com',
        phone: '+44 20 7583 5000',
        address: '1 Embankment Place, London, WC2N 6RH, UK',
        linkedinUrl: 'https://www.linkedin.com/company/pwc'
      },
      locations: [londonLocation._id, newYorkLocation._id],
      metrics: {
        yearsInBusiness: 175,
        teamSize: 328000,
        clientsServed: 100000
      },
      seo: {
        metaTitle: 'PwC - Professional Services',
        metaDescription: 'Global professional services network providing audit, consulting, tax and immigration services.',
        keywords: ['PwC', 'accounting', 'tax', 'immigration', 'consulting']
      },
      status: 'active'
    })
    
    console.log('✅ Created companies:', campbellLutyens._id, pwc._id)
    
    // 3. Create People
    console.log('Creating people...')
    
    const johnDoe = await client.create({
      _type: 'person',
      name: 'John Doe',
      slug: { current: 'john-doe' },
      title: 'Managing Director',
      bio: 'John Doe is a Managing Director at Campbell Lutyens with over 15 years of experience in fund placement and capital raising for private equity and venture capital funds.',
      company: { _ref: campbellLutyens._id },
      seniority: 'executive',
      expertise: ['fund-placement', 'private-equity', 'venture-capital', 'europe'],
      contexts: ['quest-placement', 'quest-rainmaker'],
      contactInfo: {
        email: 'john.doe@campbelllutyens.com',
        linkedinUrl: 'https://www.linkedin.com/in/johndoe'
      },
      location: { _ref: londonLocation._id },
      credentials: {
        education: [{
          degree: 'MBA',
          institution: 'London Business School',
          year: 2008
        }],
        certifications: ['CFA'],
        awards: ['Fund Placement Professional of the Year 2022']
      },
      metrics: {
        yearsExperience: 15,
        dealsCompleted: 85,
        totalValueManaged: 2500,
        clientsServed: 150
      },
      status: 'active'
    })
    
    const janeSmith = await client.create({
      _type: 'person',
      name: 'Jane Smith',
      slug: { current: 'jane-smith' },
      title: 'Immigration Partner',
      bio: 'Jane Smith is an Immigration Partner at PwC with extensive experience in UK visa applications and corporate immigration services.',
      company: { _ref: pwc._id },
      seniority: 'partner',
      expertise: ['immigration-law', 'tax-advisory', 'europe'],
      contexts: ['quest-relocation'],
      contactInfo: {
        email: 'jane.smith@pwc.com',
        linkedinUrl: 'https://www.linkedin.com/in/janesmith'
      },
      location: { _ref: londonLocation._id },
      credentials: {
        education: [{
          degree: 'LLB Law',
          institution: 'University of Cambridge',
          year: 2005
        }],
        certifications: ['Immigration Law Society Member'],
        awards: ['Immigration Lawyer of the Year 2023']
      },
      metrics: {
        yearsExperience: 18,
        clientsServed: 500
      },
      status: 'active'
    })
    
    console.log('✅ Created people:', johnDoe._id, janeSmith._id)
    
    // 4. Create Job Posting
    console.log('Creating job posting...')
    
    const jobPosting = await client.create({
      _type: 'job',
      title: 'Associate Director - Fund Placement',
      slug: { current: 'associate-director-fund-placement' },
      company: { _ref: campbellLutyens._id },
      description: [
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'We are seeking an experienced Associate Director to join our Fund Placement team in London.'
          }],
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Key Responsibilities:'
          }],
          markDefs: [],
          style: 'h3'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Lead placement processes for private equity and venture capital funds'
          }],
          listItem: 'bullet',
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Build and maintain relationships with institutional investors'
          }],
          listItem: 'bullet',
          markDefs: [],
          style: 'normal'
        }
      ],
      jobType: 'full-time',
      workMode: 'onsite',
      seniorityLevel: 'senior',
      department: 'finance',
      location: { _ref: londonLocation._id },
      locationDetails: 'Central London office',
      compensation: {
        salaryMin: 120000,
        salaryMax: 180000,
        currency: 'GBP',
        salaryPeriod: 'year',
        equity: true,
        bonus: 'Performance-based bonus up to 100% of base salary'
      },
      requirements: {
        skills: ['Private Equity', 'Fund Placement', 'Investor Relations', 'Financial Modeling'],
        experience: '5-8 years in investment banking, fund placement, or related field',
        education: 'Bachelor\'s degree required, MBA preferred'
      },
      benefits: ['health-insurance', 'dental-insurance', '401k', 'flexible-hours', 'professional-development'],
      contexts: ['quest-placement'],
      applicationEmail: 'careers@campbelllutyens.com',
      postedDate: new Date().toISOString(),
      status: 'active'
    })
    
    console.log('✅ Created job posting:', jobPosting._id)
    
    // 5. Create Article
    console.log('Creating article...')
    
    const article = await client.create({
      _type: 'article',
      title: 'Complete Guide to UK Visa Applications in 2024',
      slug: { current: 'uk-visa-guide-2024' },
      excerpt: 'Everything you need to know about applying for UK visas, from work permits to investor visas, including recent changes and requirements.',
      content: [
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Navigating the UK visa system can be complex, but understanding the different types of visas and their requirements is crucial for a successful application.'
          }],
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Popular UK Visa Categories'
          }],
          markDefs: [],
          style: 'h2'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Skilled Worker Visa - For individuals with a job offer from a UK employer'
          }],
          listItem: 'bullet',
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Global Talent Visa - For leaders and emerging leaders in specific fields'
          }],
          listItem: 'bullet',
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Innovator Founder Visa - For experienced businesspeople seeking to establish innovative businesses'
          }],
          listItem: 'bullet',
          markDefs: [],
          style: 'normal'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'Application Process'
          }],
          markDefs: [],
          style: 'h2'
        },
        {
          _type: 'block',
          children: [{
            _type: 'span',
            text: 'The UK visa application process typically involves online applications, document submission, and biometric appointments. Processing times vary by visa type and can range from 3 weeks to several months.'
          }],
          markDefs: [],
          style: 'normal'
        }
      ],
      articleType: 'guide',
      categories: ['visa-immigration', 'living-abroad'],
      contexts: ['quest-relocation'],
      author: { _ref: janeSmith._id },
      relatedCompanies: [{ _ref: pwc._id }],
      relatedLocations: [{ _ref: londonLocation._id }],
      seo: {
        metaTitle: 'UK Visa Guide 2024 - Complete Application Guide',
        metaDescription: 'Complete guide to UK visa applications including work permits, investor visas, and recent changes in 2024.',
        keywords: ['UK visa', 'immigration', 'work permit', 'visa application', 'UK immigration']
      },
      publishedAt: new Date().toISOString(),
      featured: true,
      status: 'published'
    })
    
    console.log('✅ Created article:', article._id)
    
    console.log('\n🎉 All test content created successfully!')
    console.log('\nSummary:')
    console.log(`- Locations: London (${londonLocation._id}), New York (${newYorkLocation._id})`)
    console.log(`- Companies: Campbell Lutyens (${campbellLutyens._id}), PwC (${pwc._id})`)
    console.log(`- People: John Doe (${johnDoe._id}), Jane Smith (${janeSmith._id})`)
    console.log(`- Job: Associate Director (${jobPosting._id})`)
    console.log(`- Article: UK Visa Guide (${article._id})`)
    
  } catch (error) {
    console.error('Error creating content:', error)
  }
}

// Run the script
createTestContent()