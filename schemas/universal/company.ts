import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'company',
  title: 'Company',
  type: 'document',
  fields: [
    // Core Fields
    defineField({
      name: 'name',
      title: 'Company Name',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'name',
        maxLength: 96,
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'website',
      title: 'Website',
      type: 'url',
    }),
    defineField({
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 4,
    }),
    defineField({
      name: 'logo',
      title: 'Logo',
      type: 'image',
      options: {
        hotspot: true,
      },
    }),

    // Categorization (THE KEY!)
    defineField({
      name: 'primaryType',
      title: 'Primary Type',
      type: 'string',
      description: 'Main category for this company',
      options: {
        list: [
          { title: 'Placement Agent', value: 'placement-agent' },
          { title: 'VC Firm', value: 'vc-firm' },
          { title: 'Private Equity', value: 'private-equity' },
          { title: 'Law Firm', value: 'law-firm' },
          { title: 'Accounting Firm', value: 'accounting-firm' },
          { title: 'Immigration Service', value: 'immigration-service' },
          { title: 'Property Service', value: 'property-service' },
          { title: 'Education Provider', value: 'education-provider' },
          { title: 'Healthcare Provider', value: 'healthcare-provider' },
          { title: 'Banking Service', value: 'banking-service' },
          { title: 'Insurance Provider', value: 'insurance-provider' },
          { title: 'Consultancy', value: 'consultancy' },
          { title: 'Technology Company', value: 'tech-company' },
          { title: 'Government Agency', value: 'government-agency' },
          { title: 'Other', value: 'other' },
        ],
      },
      validation: (Rule) => Rule.required(),
    }),

    defineField({
      name: 'categories',
      title: 'Categories',
      type: 'array',
      description: 'Multiple categories this company serves',
      of: [
        {
          type: 'string',
          options: {
            list: [
              // Investment Categories
              { title: 'M&A Advisory', value: 'ma-advisory' },
              { title: 'Fund Placement', value: 'fund-placement' },
              { title: 'Capital Raising', value: 'capital-raising' },
              { title: 'Investment Banking', value: 'investment-banking' },
              { title: 'Venture Capital', value: 'venture-capital' },
              { title: 'Private Equity', value: 'private-equity' },
              { title: 'Growth Equity', value: 'growth-equity' },
              
              // Relocation Categories
              { title: 'Immigration Services', value: 'immigration-services' },
              { title: 'Visa Services', value: 'visa-services' },
              { title: 'Property Services', value: 'property-services' },
              { title: 'School Search', value: 'school-search' },
              { title: 'Pet Relocation', value: 'pet-relocation' },
              { title: 'Banking Services', value: 'banking-services' },
              { title: 'Tax Advisory', value: 'tax-advisory' },
              { title: 'Legal Services', value: 'legal-services' },
              
              // Professional Services
              { title: 'Executive Search', value: 'executive-search' },
              { title: 'Recruitment', value: 'recruitment' },
              { title: 'HR Services', value: 'hr-services' },
              { title: 'Payroll Services', value: 'payroll-services' },
              { title: 'Training Services', value: 'training-services' },
              { title: 'Consulting', value: 'consulting' },
              
              // Other
              { title: 'Technology Services', value: 'tech-services' },
              { title: 'Marketing Services', value: 'marketing-services' },
              { title: 'Healthcare Services', value: 'healthcare-services' },
              { title: 'Insurance Services', value: 'insurance-services' },
            ],
          },
        },
      ],
    }),

    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should display this company',
      of: [
        {
          type: 'string',
          options: {
            list: [
              { title: 'Quest Relocation', value: 'quest-relocation' },
              { title: 'Quest Placement', value: 'quest-placement' },
              { title: 'Quest Rainmaker', value: 'quest-rainmaker' },
              { title: 'Quest Chief', value: 'quest-chief' },
              { title: 'Quest Voice', value: 'quest-voice' },
            ],
          },
        },
      ],
      validation: (Rule) => Rule.required().min(1),
    }),

    // Contact Information
    defineField({
      name: 'contactInfo',
      title: 'Contact Information',
      type: 'object',
      fields: [
        defineField({
          name: 'email',
          title: 'Email',
          type: 'email',
        }),
        defineField({
          name: 'phone',
          title: 'Phone',
          type: 'string',
        }),
        defineField({
          name: 'address',
          title: 'Address',
          type: 'text',
          rows: 2,
        }),
        defineField({
          name: 'linkedinUrl',
          title: 'LinkedIn URL',
          type: 'url',
        }),
      ],
    }),

    // Location Data
    defineField({
      name: 'locations',
      title: 'Locations',
      type: 'array',
      of: [
        {
          type: 'reference',
          to: [{ type: 'location' }],
        },
      ],
    }),

    // Flexible Metrics
    defineField({
      name: 'metrics',
      title: 'Metrics',
      type: 'object',
      description: 'Flexible metrics based on company type',
      fields: [
        defineField({
          name: 'aumRaised',
          title: 'AUM Raised ($B)',
          type: 'number',
        }),
        defineField({
          name: 'dealsCompleted',
          title: 'Deals Completed',
          type: 'number',
        }),
        defineField({
          name: 'fundSize',
          title: 'Fund Size ($M)',
          type: 'number',
        }),
        defineField({
          name: 'successRate',
          title: 'Success Rate (%)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
        defineField({
          name: 'yearsInBusiness',
          title: 'Years in Business',
          type: 'number',
        }),
        defineField({
          name: 'teamSize',
          title: 'Team Size',
          type: 'number',
        }),
        defineField({
          name: 'clientsServed',
          title: 'Clients Served',
          type: 'number',
        }),
      ],
    }),

    // SEO & Meta
    defineField({
      name: 'seo',
      title: 'SEO',
      type: 'object',
      fields: [
        defineField({
          name: 'metaTitle',
          title: 'Meta Title',
          type: 'string',
          validation: (Rule) => Rule.max(60),
        }),
        defineField({
          name: 'metaDescription',
          title: 'Meta Description',
          type: 'text',
          rows: 2,
          validation: (Rule) => Rule.max(160),
        }),
        defineField({
          name: 'keywords',
          title: 'Keywords',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            layout: 'tags',
          },
        }),
      ],
    }),

    // Status
    defineField({
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          { title: 'Active', value: 'active' },
          { title: 'Pending', value: 'pending' },
          { title: 'Inactive', value: 'inactive' },
        ],
      },
      initialValue: 'active',
    }),
  ],

  preview: {
    select: {
      title: 'name',
      subtitle: 'primaryType',
      media: 'logo',
      contexts: 'contexts',
    },
    prepare(selection) {
      const { title, subtitle, media, contexts } = selection
      const contextStr = contexts?.length ? ` (${contexts.join(', ')})` : ''
      return {
        title,
        subtitle: `${subtitle}${contextStr}`,
        media,
      }
    },
  },
})