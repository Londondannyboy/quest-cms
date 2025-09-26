import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'article',
  title: 'Article',
  type: 'document',
  fields: [
    // Core Fields
    defineField({
      name: 'title',
      title: 'Title',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96,
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'excerpt',
      title: 'Excerpt',
      type: 'text',
      rows: 3,
      description: 'Short summary for listings and previews',
      validation: (Rule) => Rule.required().max(300),
    }),
    defineField({
      name: 'featuredImage',
      title: 'Featured Image',
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
    }),

    // Content
    defineField({
      name: 'content',
      title: 'Content',
      type: 'array',
      of: [
        {
          type: 'block',
          styles: [
            { title: 'Normal', value: 'normal' },
            { title: 'H2', value: 'h2' },
            { title: 'H3', value: 'h3' },
            { title: 'H4', value: 'h4' },
            { title: 'Quote', value: 'blockquote' },
          ],
          lists: [
            { title: 'Bullet', value: 'bullet' },
            { title: 'Number', value: 'number' },
          ],
          marks: {
            decorators: [
              { title: 'Strong', value: 'strong' },
              { title: 'Emphasis', value: 'em' },
              { title: 'Underline', value: 'underline' },
              { title: 'Strike', value: 'strike-through' },
              { title: 'Code', value: 'code' },
            ],
            annotations: [
              {
                title: 'URL',
                name: 'link',
                type: 'object',
                fields: [
                  {
                    title: 'URL',
                    name: 'href',
                    type: 'url',
                  },
                  {
                    title: 'Open in new tab',
                    name: 'blank',
                    type: 'boolean',
                  },
                ],
              },
            ],
          },
        },
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

    // Categorization
    defineField({
      name: 'articleType',
      title: 'Article Type',
      type: 'string',
      options: {
        list: [
          { title: 'News', value: 'news' },
          { title: 'Guide', value: 'guide' },
          { title: 'Tutorial', value: 'tutorial' },
          { title: 'Case Study', value: 'case-study' },
          { title: 'Interview', value: 'interview' },
          { title: 'Opinion', value: 'opinion' },
          { title: 'Research', value: 'research' },
          { title: 'Announcement', value: 'announcement' },
          { title: 'Resource', value: 'resource' },
        ],
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'categories',
      title: 'Categories',
      type: 'array',
      of: [
        {
          type: 'string',
          options: {
            list: [
              // Relocation Categories
              { title: 'Visa & Immigration', value: 'visa-immigration' },
              { title: 'Living Abroad', value: 'living-abroad' },
              { title: 'Property & Housing', value: 'property-housing' },
              { title: 'Education', value: 'education' },
              { title: 'Healthcare', value: 'healthcare' },
              { title: 'Finance & Banking', value: 'finance-banking' },
              { title: 'Tax & Legal', value: 'tax-legal' },
              
              // Investment Categories
              { title: 'Private Equity', value: 'private-equity' },
              { title: 'Venture Capital', value: 'venture-capital' },
              { title: 'Fund Placement', value: 'fund-placement' },
              { title: 'M&A', value: 'ma' },
              { title: 'Market Analysis', value: 'market-analysis' },
              { title: 'Industry Trends', value: 'industry-trends' },
              
              // Career Categories
              { title: 'Job Search', value: 'job-search' },
              { title: 'Career Development', value: 'career-development' },
              { title: 'Executive Search', value: 'executive-search' },
              { title: 'Interview Tips', value: 'interview-tips' },
              { title: 'Workplace Culture', value: 'workplace-culture' },
              
              // General Categories
              { title: 'Technology', value: 'technology' },
              { title: 'Sustainability', value: 'sustainability' },
              { title: 'Innovation', value: 'innovation' },
              { title: 'Leadership', value: 'leadership' },
            ],
          },
        },
      ],
    }),
    defineField({
      name: 'tags',
      title: 'Tags',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'tag' }] }],
    }),

    // App Contexts
    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should display this article',
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

    // Author & Attribution
    defineField({
      name: 'author',
      title: 'Author',
      type: 'reference',
      to: [{ type: 'person' }],
    }),
    defineField({
      name: 'contributors',
      title: 'Contributors',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'person' }] }],
    }),
    defineField({
      name: 'relatedCompanies',
      title: 'Related Companies',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'company' }] }],
    }),
    defineField({
      name: 'relatedLocations',
      title: 'Related Locations',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'location' }] }],
    }),

    // Related Content
    defineField({
      name: 'relatedArticles',
      title: 'Related Articles',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'article' }] }],
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
        defineField({
          name: 'ogImage',
          title: 'Open Graph Image',
          type: 'image',
          description: 'Image for social media sharing',
        }),
      ],
    }),

    // Publishing
    defineField({
      name: 'publishedAt',
      title: 'Published At',
      type: 'datetime',
    }),
    defineField({
      name: 'updatedAt',
      title: 'Last Updated',
      type: 'datetime',
    }),
    defineField({
      name: 'featured',
      title: 'Featured Article',
      type: 'boolean',
      initialValue: false,
    }),
    defineField({
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          { title: 'Draft', value: 'draft' },
          { title: 'Review', value: 'review' },
          { title: 'Published', value: 'published' },
          { title: 'Archived', value: 'archived' },
        ],
      },
      initialValue: 'draft',
    }),
  ],

  preview: {
    select: {
      title: 'title',
      author: 'author.name',
      status: 'status',
      media: 'featuredImage',
      contexts: 'contexts',
    },
    prepare(selection) {
      const { title, author, status, media, contexts } = selection
      const statusEmoji = {
        draft: '📝',
        review: '👁️',
        published: '✅',
        archived: '📦',
      }
      const contextStr = contexts?.length ? ` [${contexts.join(', ')}]` : ''
      return {
        title: `${statusEmoji[status] || ''} ${title}`,
        subtitle: `by ${author || 'Unknown'}${contextStr}`,
        media,
      }
    },
  },
})