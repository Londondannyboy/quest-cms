import { defineField, defineType } from 'sanity'

export default defineType({
  name: 'job',
  title: 'Job',
  type: 'document',
  fields: [
    // Core Fields
    defineField({
      name: 'title',
      title: 'Job Title',
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
      name: 'company',
      title: 'Company',
      type: 'reference',
      to: [{ type: 'company' }],
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'description',
      title: 'Job Description',
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
      ],
    }),

    // Job Details
    defineField({
      name: 'jobType',
      title: 'Job Type',
      type: 'string',
      options: {
        list: [
          { title: 'Full Time', value: 'full-time' },
          { title: 'Part Time', value: 'part-time' },
          { title: 'Contract', value: 'contract' },
          { title: 'Freelance', value: 'freelance' },
          { title: 'Internship', value: 'internship' },
          { title: 'Temporary', value: 'temporary' },
        ],
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'workMode',
      title: 'Work Mode',
      type: 'string',
      options: {
        list: [
          { title: 'On-site', value: 'onsite' },
          { title: 'Remote', value: 'remote' },
          { title: 'Hybrid', value: 'hybrid' },
        ],
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'seniorityLevel',
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
        ],
      },
    }),
    defineField({
      name: 'department',
      title: 'Department',
      type: 'string',
      options: {
        list: [
          { title: 'Engineering', value: 'engineering' },
          { title: 'Product', value: 'product' },
          { title: 'Design', value: 'design' },
          { title: 'Marketing', value: 'marketing' },
          { title: 'Sales', value: 'sales' },
          { title: 'Operations', value: 'operations' },
          { title: 'Finance', value: 'finance' },
          { title: 'Legal', value: 'legal' },
          { title: 'HR', value: 'hr' },
          { title: 'Customer Success', value: 'customer-success' },
          { title: 'Data', value: 'data' },
          { title: 'Research', value: 'research' },
        ],
      },
    }),

    // Location
    defineField({
      name: 'location',
      title: 'Location',
      type: 'reference',
      to: [{ type: 'location' }],
    }),
    defineField({
      name: 'locationDetails',
      title: 'Location Details',
      type: 'string',
      description: 'Additional location information (e.g., "Downtown office")',
    }),

    // Compensation
    defineField({
      name: 'compensation',
      title: 'Compensation',
      type: 'object',
      fields: [
        defineField({
          name: 'salaryMin',
          title: 'Minimum Salary',
          type: 'number',
        }),
        defineField({
          name: 'salaryMax',
          title: 'Maximum Salary',
          type: 'number',
        }),
        defineField({
          name: 'currency',
          title: 'Currency',
          type: 'string',
          options: {
            list: [
              { title: 'USD', value: 'USD' },
              { title: 'EUR', value: 'EUR' },
              { title: 'GBP', value: 'GBP' },
              { title: 'CAD', value: 'CAD' },
              { title: 'AUD', value: 'AUD' },
            ],
          },
          initialValue: 'USD',
        }),
        defineField({
          name: 'salaryPeriod',
          title: 'Salary Period',
          type: 'string',
          options: {
            list: [
              { title: 'Per Hour', value: 'hour' },
              { title: 'Per Day', value: 'day' },
              { title: 'Per Week', value: 'week' },
              { title: 'Per Month', value: 'month' },
              { title: 'Per Year', value: 'year' },
            ],
          },
          initialValue: 'year',
        }),
        defineField({
          name: 'equity',
          title: 'Equity Offered',
          type: 'boolean',
        }),
        defineField({
          name: 'bonus',
          title: 'Bonus Structure',
          type: 'string',
        }),
      ],
    }),

    // Requirements
    defineField({
      name: 'requirements',
      title: 'Requirements',
      type: 'object',
      fields: [
        defineField({
          name: 'skills',
          title: 'Required Skills',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            layout: 'tags',
          },
        }),
        defineField({
          name: 'experience',
          title: 'Years of Experience',
          type: 'string',
        }),
        defineField({
          name: 'education',
          title: 'Education Requirements',
          type: 'string',
        }),
        defineField({
          name: 'certifications',
          title: 'Required Certifications',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            layout: 'tags',
          },
        }),
      ],
    }),

    // Benefits
    defineField({
      name: 'benefits',
      title: 'Benefits',
      type: 'array',
      of: [{ type: 'string' }],
      options: {
        list: [
          { title: 'Health Insurance', value: 'health-insurance' },
          { title: 'Dental Insurance', value: 'dental-insurance' },
          { title: 'Vision Insurance', value: 'vision-insurance' },
          { title: '401k', value: '401k' },
          { title: 'Stock Options', value: 'stock-options' },
          { title: 'PTO', value: 'pto' },
          { title: 'Flexible Hours', value: 'flexible-hours' },
          { title: 'Remote Work', value: 'remote-work' },
          { title: 'Professional Development', value: 'professional-development' },
          { title: 'Gym Membership', value: 'gym-membership' },
          { title: 'Commuter Benefits', value: 'commuter-benefits' },
          { title: 'Parental Leave', value: 'parental-leave' },
        ],
      },
    }),

    // App Contexts
    defineField({
      name: 'contexts',
      title: 'App Contexts',
      type: 'array',
      description: 'Which Quest apps should display this job',
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

    // Application Details
    defineField({
      name: 'applicationUrl',
      title: 'Application URL',
      type: 'url',
    }),
    defineField({
      name: 'applicationEmail',
      title: 'Application Email',
      type: 'email',
    }),
    defineField({
      name: 'applicationDeadline',
      title: 'Application Deadline',
      type: 'datetime',
    }),

    // Posting Details
    defineField({
      name: 'postedDate',
      title: 'Posted Date',
      type: 'datetime',
      initialValue: new Date().toISOString(),
    }),
    defineField({
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          { title: 'Active', value: 'active' },
          { title: 'Paused', value: 'paused' },
          { title: 'Filled', value: 'filled' },
          { title: 'Cancelled', value: 'cancelled' },
        ],
      },
      initialValue: 'active',
    }),
  ],

  preview: {
    select: {
      title: 'title',
      company: 'company.name',
      location: 'location.city',
      status: 'status',
      jobType: 'jobType',
    },
    prepare(selection) {
      const { title, company, location, status, jobType } = selection
      const subtitle = `${company || 'No Company'} • ${location || 'Remote'} • ${jobType || ''}`
      return {
        title: `${title} ${status === 'active' ? '🟢' : '🔴'}`,
        subtitle,
      }
    },
  },
})