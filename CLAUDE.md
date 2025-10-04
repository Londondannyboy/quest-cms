# PROJECT: Quest-CMS

## 📍 Location
- **Code**: `/Users/dankeegan/quest-cms/`
- **Knowledge**: `knowledge-base/02-PROJECT-DOCS/QUEST_CMS/`
- **Git**: https://github.com/Londondannyboy/quest-cms
- **Production**: https://quest-cms-production.railway.app

## 🔗 Related Knowledge Patterns
- `knowledge-base/03-TECHNOLOGY-STACK/RAILWAY_DEPLOYMENT_PLATFORM.md`
- `knowledge-base/03-TECHNOLOGY-STACK/NEON_POSTGRESQL_EXTENSIONS.md`
- `knowledge-base/02-PROJECT-DOCS/QUEST_CMS/QUEST_CMS_TECH_STACK.md`

## 🎯 Current Status
- [x] NiceGUI admin interface with working CRUD operations
- [x] Database-first architecture with Neon PostgreSQL schema
- [x] AI services integration (Claude + Flux Pro placeholders)  
- [x] Human review workflow
- [x] Local demo running perfectly (http://localhost:8080/admin)
- [x] Complete Archon methodology implementation
- [x] Product Requirements Document (PRD) following G3 framework
- [ ] Production deployment on Railway (GitHub connection pending)
- [ ] Environment variables configured for production

## ⚡ Quick Commands
```bash
# Start local development server
python3 working_demo.py

# Access admin interface
open http://localhost:8080/admin

# Push to GitHub (triggers Railway deployment)
git push origin main

# Health check
curl http://localhost:8080/health
```

## 🏗️ Architecture Overview

Quest-CMS is an AI-first content management system designed for mass content production with human review checkpoints. Built following Archon methodology and proven database-first patterns, it serves as the content creation hub for the Quest intelligence platform.

### Key Features
- **🤖 AI-Powered Content Creation**: Claude integration for high-quality articles, Flux Pro for featured images
- **📝 Human Review Workflow**: Review queue with quality control and approval process
- **🗄️ Database-First Architecture**: Neon PostgreSQL with full-text search and vector embeddings
- **🖥️ Modern Admin Interface**: NiceGUI framework with Progressive Web App capabilities

### Technology Stack
- **Framework**: NiceGUI (FastAPI + Vue.js + WebSockets)
- **Database**: Neon PostgreSQL with pg_search and pgvector extensions
- **AI Services**: Claude API (content) + Replicate Flux Pro (images)
- **Deployment**: Railway (Python backend with auto-deployment)
- **Frontend**: Progressive Web App with real-time updates

## 🔑 Environment Variables Required
```bash
# Production deployment
NEON_CONNECTION_STRING=postgresql://...
CLAUDE_API_KEY=sk-ant-api03-...
REPLICATE_API_TOKEN=r8_...
PORT=8080
```

## 📋 Spec Kit Integration

### Specification-Driven Development
Quest-CMS now follows **Spec Kit methodology** for all feature development:

```
.specify/
├── memory/                       # Project constitution and principles
├── scripts/                      # Slash command implementations
├── specs/                        # Feature specifications
└── templates/                    # Specification templates
```

### Development Workflow
- **🏛️ `/constitution`**: Establish project principles and quality standards
- **📋 `/specify`**: Define feature requirements and user stories
- **🔧 `/plan`**: Create technical implementation plans
- **✅ `/tasks`**: Generate actionable development tasks
- **🚀 `/implement`**: Execute implementation following specifications

## 🚨 Known Issues
- NiceGUI 3.0 compatibility: Fixed splitter API (ui.splitter.before → splitter.add_slot)
- Railway GitHub integration: Requires manual setup through Railway dashboard

## 📝 Recent Progress
- 2025-10-04: Fixed all NiceGUI 3.0 compatibility issues
- 2025-10-04: All CRUD operations working (Create, Edit, View, Review)
- 2025-10-04: Live preview with real-time markdown rendering
- 2025-10-04: GitHub credentials configured for deployment
- 2025-10-04: Railway deployment configuration completed
- 2025-10-04: Complete Archon methodology implementation
- 2025-10-04: Product Requirements Document (PRD) created with G3 framework
- 2025-10-04: Knowledge base structure established

## 🎯 Next Steps
1. **Complete Railway GitHub connection** using `RAILWAY_SETUP_INSTRUCTIONS.md`
2. **Use Spec Kit for next feature** - Start with `/constitution` command
3. **Demonstrate Spec Kit workflow** - `/specify` → `/plan` → `/tasks` → `/implement`
4. **Document learnings** in Obsidian knowledge base

## 📊 Performance Specifications

### Response Time Targets (NON-NEGOTIABLE)
- **Page Load**: < 2 seconds for all admin pages
- **Database Queries**: < 100ms for content operations  
- **AI Generation**: < 30 seconds for single article
- **Search Operations**: < 500ms for full-text search

### Scalability Metrics
- **Content Volume**: 1000+ articles/month supported
- **Concurrent Users**: 100 users supported
- **AI Operations**: 5 concurrent Claude requests
- **Database**: Scales automatically with Neon

## 🔗 Integration with Quest Ecosystem

Quest-CMS feeds content to the entire Quest platform:
- **Quest-Pilot**: Intelligence platform consuming content
- **Relocation-Quest**: Location content pipeline
- **Rainmaker-Quest**: Business content pipeline  
- **Placement-Quest**: Job content pipeline

### Data Flow
```
MCP → AI Content Generation → Quest-CMS Review → Neon Database → Quest Sites
```

---
**Note**: Complete project following Archon methodology. Main application is `working_demo.py`. Complete documentation in knowledge-base/ and PRODUCT_REQUIREMENTS_DOCUMENT.md.