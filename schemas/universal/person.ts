import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'person',
  title: 'Person',
  type: 'document',
  fields: [
    // Core Fields
    defineField({
      name: 'name',
      title: 'Full Name',
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
      name: 'title',
      title: 'Job Title',
      type: 'string',
    }),
    defineField({
      name: 'bio',
      title: 'Biography',
      type: 'text',
      rows: 4,
    }),
    defineField({
      name: 'photo',
      title: 'Photo',
      type: 'image',
      options: {
        hotspot: true,
      },
    }),

    // Company Association
    defineField({
      name: 'company',
      title: 'Company',
      type: 'reference',
      to: [{ type: 'company' }],
    }),

    // Seniority Level
    defineField({
      name: 'seniority',
      title: 'Seniority Level',
      type: 'string',
      options: {
        list: [
          { title: 'Entry Level', value: 'entry' },
          { title: 'Junior', value: 'junior' },
          { title: 'Mid-Level', value: 'mid' },
          { title: 'Senior', value: 'senior' },
          { title: 'Lead', value: 'lead' },
          { title: 'Manager', value: 'manager' },
          { title: 'Director', value: 'director' },
          { title: 'VP', value: 'vp' },
          { title: 'Executive', value: 'executive' },
          { title: 'C-Suite', value: 'c-suite' },
          { title: 'Founder', value: 'founder' },
          { title: 'Partner', value: 'partner' },
        ],
      },
    }),

    // Expertise Areas
    defineField({
      name: 'expertise',
      title: 'Areas of Expertise',
      type: 'array',
      of: [
        {
          type: 'string',
          options: {
            list: [
              // Investment Expertise
              { title: 'Private Equity', value: 'private-equity' },
              { title: 'Venture Capital', value: 'venture-capital' },
              { title: 'M&A', value: 'ma' },
              { title: 'Capital Markets', value: 'capital-markets' },
              { title: 'Fund Placement', value: 'fund-placement' },
              { title: 'Real Estate', value: 'real-estate' },
              { title: 'Infrastructure', value: 'infrastructure' },
              { title: 'Debt Capital', value: 'debt-capital' },
              
              // Professional Expertise
              { title: 'Immigration Law', value: 'immigration-law' },
              { title: 'Tax Advisory', value: 'tax-advisory' },
              { title: 'Corporate Law', value: 'corporate-law' },
              { title: 'Executive Search', value: 'executive-search' },
              { title: 'HR Management', value: 'hr-management' },
              { title: 'Technology', value: 'technology' },
              { title: 'Healthcare', value: 'healthcare' },
              { title: 'Education', value: 'education' },
              
              // Geographic Expertise
              { title: 'North America', value: 'north-america' },
              { title: 'Europe', value: 'europe' },
              { title: 'Asia-Pacific', value: 'asia-pacific' },
              { title: 'Middle East', value: 'middle-east' },
              { title: 'Latin America', value: 'latin-america' },
              { title: 'Africa', value: 'africa' },
            ],
          },
        },
      ],
    }),

    // App Contexts
    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should display this person',
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
          name: 'linkedinUrl',
          title: 'LinkedIn URL',
          type: 'url',
        }),
        defineField({
          name: 'twitterUrl',
          title: 'Twitter URL',
          type: 'url',
        }),
      ],
    }),

    // Location
    defineField({
      name: 'location',
      title: 'Location',
      type: 'reference',
      to: [{ type: 'location' }],
    }),

    // Achievements & Credentials
    defineField({
      name: 'credentials',
      title: 'Credentials',
      type: 'object',
      fields: [
        defineField({
          name: 'education',
          title: 'Education',
          type: 'array',
          of: [
            {
              type: 'object',
              fields: [
                defineField({
                  name: 'degree',
                  title: 'Degree',
                  type: 'string',
                }),
                defineField({
                  name: 'institution',
                  title: 'Institution',
                  type: 'string',
                }),
                defineField({
                  name: 'year',
                  title: 'Year',
                  type: 'number',
                }),
              ],
            },
          ],
        }),
        defineField({
          name: 'certifications',
          title: 'Certifications',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            layout: 'tags',
          },
        }),
        defineField({
          name: 'awards',
          title: 'Awards',
          type: 'array',
          of: [{ type: 'string' }],
        }),
        defineField({
          name: 'publications',
          title: 'Publications',
          type: 'array',
          of: [{ type: 'string' }],
        }),
      ],
    }),

    // Experience Metrics
    defineField({
      name: 'metrics',
      title: 'Experience Metrics',
      type: 'object',
      fields: [
        defineField({
          name: 'yearsExperience',
          title: 'Years of Experience',
          type: 'number',
        }),
        defineField({
          name: 'dealsCompleted',
          title: 'Deals Completed',
          type: 'number',
        }),
        defineField({
          name: 'totalValueManaged',
          title: 'Total Value Managed ($M)',
          type: 'number',
        }),
        defineField({
          name: 'clientsServed',
          title: 'Clients Served',
          type: 'number',
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
          { title: 'Inactive', value: 'inactive' },
        ],
      },
      initialValue: 'active',
    }),
  ],

  preview: {
    select: {
      title: 'name',
      subtitle: 'title',
      company: 'company.name',
      media: 'photo',
      seniority: 'seniority',
    },
    prepare(selection) {
      const { title, subtitle, company, media, seniority } = selection
      const seniorityStr = seniority ? ` (${seniority})` : ''
      const companyStr = company ? ` at ${company}` : ''
      return {
        title,
        subtitle: `${subtitle}${companyStr}${seniorityStr}`,
        media,
      }
    },
  },
})