# PROJECT: Quest-CMS

## 📍 Location
- **Code**: `/Users/dankeegan/quest-cms/`
- **Knowledge**: `knowledge-base/02-PROJECT-DOCS/QUEST_CMS/`
- **Git**: https://github.com/Londondannyboy/quest-cms

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
- [ ] Production deployment on Railway
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

## 🚨 Known Issues
- NiceGUI 3.0 compatibility: Fixed splitter API (ui.splitter.before → splitter.add_slot)
- Production deployment: Ready but pending Railway configuration

## 📝 Recent Progress
- 2025-10-04: Fixed all NiceGUI 3.0 compatibility issues
- 2025-10-04: All CRUD operations working (Create, Edit, View, Review)
- 2025-10-04: Live preview with real-time markdown rendering
- 2025-10-04: GitHub credentials configured for deployment
- 2025-10-04: Railway deployment configuration completed

## 🏗️ Architecture
- **Framework**: NiceGUI (FastAPI + Vue.js + WebSockets)
- **Database**: Neon PostgreSQL with full-text search
- **AI Services**: Claude (content) + Flux Pro (images)
- **Deployment**: Railway (Python backend)
- **Frontend**: Progressive Web App capabilities

## 🔑 Environment Variables Required
```bash
# Production deployment
NEON_CONNECTION_STRING=postgresql://...
CLAUDE_API_KEY=sk-ant-api03-...
REPLICATE_API_TOKEN=r8_...
PORT=8080
```

## 🎯 Next Steps
1. Deploy to Railway production
2. Configure production environment variables
3. Test live admin interface
4. Integration with Quest ecosystem sites

---
**Note**: This is a bridge file. Main application is `working_demo.py`. Complete documentation is in knowledge-base.