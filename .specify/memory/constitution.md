# Quest-CMS Constitution

## Core Principles

### I. AI-First Content Architecture (NON-NEGOTIABLE)
All content creation starts with AI generation followed by human review gates. Every piece of content must be AI-generated using Claude API, scored for quality, and routed through human review workflows before publication. No manual content creation without AI assistance.

### II. Database-First Data Integrity  
PostgreSQL serves as the single source of truth for all content operations. All data mutations must go through the database layer with proper schema validation. No in-memory state management or file-based storage for persistent data.

### III. Progressive Web Application Design
NiceGUI framework provides cross-platform compatibility with real-time WebSocket updates. UI must be responsive, accessible, and function as a Progressive Web App. All user interactions must provide immediate feedback.

### IV. Performance Standards (NON-NEGOTIABLE)
- Page loads: < 2 seconds for all admin operations
- Database queries: < 500ms for content retrieval
- AI generation: < 30 seconds for single article
- Search operations: < 500ms for full-text search
- Uptime target: 99.9% in production

### V. Human-AI Workflow Integration
Every AI-generated content piece requires human quality assessment and approval. Quality scoring (1-10) is mandatory for all AI content. Review workflow must be intuitive and efficient for non-technical users.

## Technology Architecture Standards

### Framework Requirements
- **Backend**: NiceGUI (FastAPI + Vue.js + WebSockets) for rapid development
- **Database**: Neon PostgreSQL with pg_search and pgvector extensions
- **AI Services**: Claude API for content, Replicate Flux Pro for images
- **Deployment**: Railway platform with GitHub auto-deployment
- **Environment**: Python 3.11+ with uv package management

### API Design Standards
- RESTful endpoints for all CRUD operations
- WebSocket connections for real-time updates
- JSON API responses with consistent error handling
- Environment-based configuration (dev/staging/production)

### Security Requirements
- All credentials stored as environment variables
- SSL/TLS encryption for all database connections
- Input validation for all user-provided data
- Rate limiting for AI service calls

## Development Workflow

### Code Quality Gates
1. **Manual Testing**: All CRUD operations must be manually tested
2. **AI Integration Testing**: Claude and Replicate APIs must be functional
3. **Database Testing**: All database operations validated
4. **Performance Testing**: Response times within specified targets

### Documentation Standards
- All functions require docstrings with purpose and parameters
- API endpoints documented with request/response examples
- Database schema documented with relationships
- Deployment instructions must be step-by-step executable

### Error Handling Requirements
- Try-catch blocks mandatory for all database operations
- User-friendly error messages in all UI components
- Comprehensive logging for debugging and monitoring
- Graceful degradation when AI services are unavailable

## Quest Ecosystem Integration

### Content Distribution
Quest-CMS feeds content to the entire Quest platform ecosystem:
- Quest-Pilot: Intelligence platform consuming content
- Relocation-Quest: Location-specific content pipeline
- Rainmaker-Quest: Business content pipeline
- Placement-Quest: Job market content pipeline

### Data Flow Architecture
```
MCP → AI Content Generation → Quest-CMS Review → Neon Database → Quest Sites
```

### Scalability Requirements
- Content volume: 1000+ articles/month supported
- Concurrent users: 100+ simultaneous users
- AI operations: 5+ concurrent Claude requests
- Database: Auto-scaling with Neon serverless

## Quality Assurance Framework

### Pre-Deployment Validation
1. Environment variables properly configured
2. Database connectivity verified
3. AI service health checks passing
4. All CRUD operations functional
5. Performance benchmarks met

### Production Monitoring
- Application performance tracking
- Database query performance monitoring
- AI service availability monitoring
- User experience metrics tracking

### Continuous Quality Standards
- Code reviews required for all changes
- Performance regression testing
- Security vulnerability scanning
- Documentation updates with code changes

## Governance

### Constitution Authority
This constitution supersedes all other development practices and decisions for Quest-CMS. All pull requests and code reviews must verify compliance with these principles.

### Amendment Process
Constitution amendments require:
1. Technical justification document
2. Performance impact assessment
3. Implementation migration plan
4. Approval from Quest ecosystem stakeholders

### Development Guidance
For runtime development decisions not covered in this constitution, refer to:
- PRODUCT_REQUIREMENTS_DOCUMENT.md for G3 framework guidance
- CLAUDE.md for project-specific instructions
- Spec Kit specifications for feature development

**Version**: 1.0.0 | **Ratified**: 2025-10-04 | **Last Amended**: 2025-10-04