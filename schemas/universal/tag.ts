import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'tag',
  title: 'Tag',
  type: 'document',
  fields: [
    defineField({
      name: 'name',
      title: 'Tag Name',
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
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 2,
    }),
    defineField({
      name: 'category',
      title: 'Tag Category',
      type: 'string',
      options: {
        list: [
          { title: 'Topic', value: 'topic' },
          { title: 'Industry', value: 'industry' },
          { title: 'Technology', value: 'technology' },
          { title: 'Location', value: 'location' },
          { title: 'Service', value: 'service' },
          { title: 'Feature', value: 'feature' },
          { title: 'Other', value: 'other' },
        ],
      },
    }),
    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should use this tag',
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
              { title: 'All Apps', value: 'all' },
            ],
          },
        },
      ],
      validation: (Rule) => Rule.required().min(1),
    }),
    defineField({
      name: 'color',
      title: 'Tag Color',
      type: 'string',
      description: 'Hex color for tag display (e.g., #3B82F6)',
      validation: (Rule) => 
        Rule.custom((color) => {
          if (!color) return true
          if (!/^#[0-9A-F]{6}$/i.test(color)) {
            return 'Please enter a valid hex color (e.g., #3B82F6)'
          }
          return true
        }),
    }),
    defineField({
      name: 'priority',
      title: 'Priority',
      type: 'number',
      description: 'Higher numbers appear first',
      initialValue: 0,
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
      category: 'category',
      contexts: 'contexts',
      color: 'color',
    },
    prepare(selection) {
      const { title, category, contexts, color } = selection
      const contextStr = contexts?.includes('all') ? 'All Apps' : contexts?.join(', ')
      return {
        title: `${color ? '🎨 ' : ''}${title}`,
        subtitle: `${category || 'Uncategorized'} • ${contextStr || 'No contexts'}`,
      }
    },
  },
})