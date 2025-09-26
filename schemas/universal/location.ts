import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'location',
  title: 'Location',
  type: 'document',
  fields: [
    // Core Fields
    defineField({
      name: 'name',
      title: 'Location Name',
      type: 'string',
      description: 'Full location name (e.g., "London, United Kingdom")',
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
      name: 'city',
      title: 'City',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'state',
      title: 'State/Province',
      type: 'string',
    }),
    defineField({
      name: 'country',
      title: 'Country',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'countryCode',
      title: 'Country Code',
      type: 'string',
      description: 'ISO 3166-1 alpha-2 code (e.g., US, GB, FR)',
      validation: (Rule) => Rule.required().length(2),
    }),
    defineField({
      name: 'region',
      title: 'Region',
      type: 'string',
      options: {
        list: [
          { title: 'North America', value: 'north-america' },
          { title: 'South America', value: 'south-america' },
          { title: 'Europe', value: 'europe' },
          { title: 'Asia', value: 'asia' },
          { title: 'Africa', value: 'africa' },
          { title: 'Oceania', value: 'oceania' },
          { title: 'Middle East', value: 'middle-east' },
        ],
      },
    }),

    // Geographic Data
    defineField({
      name: 'coordinates',
      title: 'Coordinates',
      type: 'geopoint',
    }),
    defineField({
      name: 'timezone',
      title: 'Timezone',
      type: 'string',
      description: 'e.g., America/New_York, Europe/London',
    }),

    // Descriptive Content
    defineField({
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 4,
    }),
    defineField({
      name: 'overview',
      title: 'Overview',
      type: 'array',
      of: [
        {
          type: 'block',
          styles: [
            { title: 'Normal', value: 'normal' },
            { title: 'H3', value: 'h3' },
            { title: 'H4', value: 'h4' },
          ],
          lists: [
            { title: 'Bullet', value: 'bullet' },
            { title: 'Number', value: 'number' },
          ],
        },
        {
          type: 'image',
          options: {
            hotspot: true,
          },
        },
      ],
    }),
    defineField({
      name: 'images',
      title: 'Images',
      type: 'array',
      of: [
        {
          type: 'image',
          options: {
            hotspot: true,
          },
          fields: [
            defineField({
              name: 'alt',
              title: 'Alt Text',
              type: 'string',
            }),
            defineField({
              name: 'caption',
              title: 'Caption',
              type: 'string',
            }),
          ],
        },
      ],
    }),

    // Location Attributes
    defineField({
      name: 'locationType',
      title: 'Location Type',
      type: 'string',
      options: {
        list: [
          { title: 'Capital City', value: 'capital' },
          { title: 'Major City', value: 'major-city' },
          { title: 'City', value: 'city' },
          { title: 'Town', value: 'town' },
          { title: 'District', value: 'district' },
          { title: 'Country', value: 'country' },
          { title: 'State/Province', value: 'state' },
        ],
      },
    }),
    defineField({
      name: 'businessHub',
      title: 'Business Hub',
      type: 'boolean',
      description: 'Is this a major business/financial center?',
      initialValue: false,
    }),
    defineField({
      name: 'techHub',
      title: 'Tech Hub',
      type: 'boolean',
      description: 'Is this a technology/startup hub?',
      initialValue: false,
    }),

    // Statistics & Data
    defineField({
      name: 'statistics',
      title: 'Statistics',
      type: 'object',
      fields: [
        defineField({
          name: 'population',
          title: 'Population',
          type: 'number',
        }),
        defineField({
          name: 'gdp',
          title: 'GDP (USD Billions)',
          type: 'number',
        }),
        defineField({
          name: 'averageSalary',
          title: 'Average Salary (USD)',
          type: 'number',
        }),
        defineField({
          name: 'costOfLivingIndex',
          title: 'Cost of Living Index',
          type: 'number',
          description: 'Base 100 = New York City',
        }),
        defineField({
          name: 'qualityOfLifeIndex',
          title: 'Quality of Life Index',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(10),
        }),
        defineField({
          name: 'safetyIndex',
          title: 'Safety Index',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
        defineField({
          name: 'englishProficiency',
          title: 'English Proficiency %',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
      ],
    }),

    // Living Information
    defineField({
      name: 'livingInfo',
      title: 'Living Information',
      type: 'object',
      fields: [
        defineField({
          name: 'averageRent',
          title: 'Average Monthly Rent (1BR)',
          type: 'number',
          description: 'In USD',
        }),
        defineField({
          name: 'publicTransport',
          title: 'Public Transport Quality',
          type: 'string',
          options: {
            list: [
              { title: 'Excellent', value: 'excellent' },
              { title: 'Good', value: 'good' },
              { title: 'Fair', value: 'fair' },
              { title: 'Poor', value: 'poor' },
            ],
          },
        }),
        defineField({
          name: 'internationalSchools',
          title: 'Number of International Schools',
          type: 'number',
        }),
        defineField({
          name: 'hospitals',
          title: 'Major Hospitals',
          type: 'number',
        }),
        defineField({
          name: 'expatCommunity',
          title: 'Expat Community Size',
          type: 'string',
          options: {
            list: [
              { title: 'Very Large', value: 'very-large' },
              { title: 'Large', value: 'large' },
              { title: 'Medium', value: 'medium' },
              { title: 'Small', value: 'small' },
              { title: 'Very Small', value: 'very-small' },
            ],
          },
        }),
      ],
    }),

    // Business Information
    defineField({
      name: 'businessInfo',
      title: 'Business Information',
      type: 'object',
      fields: [
        defineField({
          name: 'corporateTaxRate',
          title: 'Corporate Tax Rate (%)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
        defineField({
          name: 'personalTaxRate',
          title: 'Top Personal Tax Rate (%)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
        defineField({
          name: 'easeOfBusiness',
          title: 'Ease of Doing Business Score',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(100),
        }),
        defineField({
          name: 'startupEcosystem',
          title: 'Startup Ecosystem Rating',
          type: 'string',
          options: {
            list: [
              { title: 'World-Class', value: 'world-class' },
              { title: 'Excellent', value: 'excellent' },
              { title: 'Good', value: 'good' },
              { title: 'Emerging', value: 'emerging' },
              { title: 'Developing', value: 'developing' },
            ],
          },
        }),
      ],
    }),

    // App Contexts
    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should display this location',
      of: [
        {
          type: 'string',
          options: {
            list: [
              { title: 'Quest Relocation', value: 'quest-relocation' },
              { title: 'Quest Placement', value: 'quest-placement' },
              { title: 'Quest Rainmaker', value: 'quest-rainmaker' },
              { title: 'Quest Chief', value: 'quest-chief' },
            ],
          },
        },
      ],
      validation: (Rule) => Rule.required().min(1),
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
      name: 'featured',
      title: 'Featured Location',
      type: 'boolean',
      initialValue: false,
    }),
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
      country: 'country',
      region: 'region',
      featured: 'featured',
      media: 'images.0',
    },
    prepare(selection) {
      const { title, country, region, featured } = selection
      return {
        title: `${featured ? '⭐ ' : ''}${title}`,
        subtitle: `${country} • ${region}`,
      }
    },
  },
})