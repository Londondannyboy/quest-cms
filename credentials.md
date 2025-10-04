# Quest-CMS Project Credentials

**⚠️ SECURE PROJECT CREDENTIALS - Do not commit to git**  
**📍 Location**: `/Users/dankeegan/quest-cms/` (project-specific)  
**Last Updated**: 2025-10-04  
**Status**: ✅ CONFIGURED for Quest-CMS deployment

---

## 🎯 Quest-CMS Specific Credentials

### Railway Deployment
```bash
# Railway deployment token for Quest-CMS project
RAILWAY_TOKEN=22ada421-9487-45a3-b8cf-1ba21b9b39de

# Railway project details
RAILWAY_PROJECT_URL=https://quest-cms-production.railway.app
RAILWAY_PROJECT_ID=[to be determined after GitHub connection]
```

### GitHub Repository
```bash
# GitHub repository for Quest-CMS
GITHUB_REPO=https://github.com/Londondannyboy/quest-cms
GITHUB_TOKEN=[REDACTED - see local credentials file]
```

---

## 🔑 Production Environment Variables

### Database Connection
```bash
# Neon PostgreSQL connection string (to be configured for production)
NEON_CONNECTION_STRING=postgresql://quest_user:password@ep-example.us-east-1.aws.neon.tech/quest_cms_db?sslmode=require
```

### AI Services
```bash
# Claude API for content generation
CLAUDE_API_KEY=[REDACTED - see local credentials file]

# Replicate API for image generation (Flux Pro)
REPLICATE_API_TOKEN=[REDACTED - see local credentials file]
```

### Application Configuration
```bash
# Application port for Railway deployment
PORT=8080

# Environment designation
NODE_ENV=production
```

---

## 📋 Railway Deployment Checklist

### Environment Variables to Set in Railway Dashboard
1. **NEON_CONNECTION_STRING** - Database connection string
2. **CLAUDE_API_KEY** - Claude API for content generation
3. **REPLICATE_API_TOKEN** - Replicate API for image generation
4. **PORT** - Application port (8080)

### GitHub Integration Steps
1. Access Railway dashboard at https://railway.app/dashboard
2. Find "quest-cms-production" project
3. Connect to GitHub repository: `Londondannyboy/quest-cms`
4. Set deployment branch to `main`
5. Enable auto-deployment on push

---

## 🔗 Service References

### Primary Data Sources
- **Master Credentials**: `/Users/dankeegan/credentials/quest-credentials.md`
- **Railway Documentation**: `RAILWAY_GITHUB_SETUP.md`
- **Knowledge Base**: `knowledge-base/02-PROJECT-DOCS/QUEST_CMS/`

### External Service Dashboards
- **Railway Dashboard**: https://railway.app/dashboard
- **Neon Console**: https://console.neon.tech/
- **Claude Console**: https://console.anthropic.com
- **Replicate Dashboard**: https://replicate.com/account
- **GitHub Repository**: https://github.com/Londondannyboy/quest-cms

---

## 🚨 Security Notes

### Access Control
- **Railway Token**: Full deployment access - protect carefully
- **GitHub Token**: Repository access - full permissions
- **Database Credentials**: Production database access
- **AI Service Keys**: Usage-based billing - monitor usage

### Best Practices
1. **Never commit credentials to version control**
2. **Use environment variables in production**
3. **Rotate tokens quarterly or on security incidents**
4. **Monitor usage through service dashboards**
5. **Keep this file local only - no cloud sync**

---

## 🎯 Production Deployment Status

### ✅ Configured
- [x] Railway token available for deployment
- [x] GitHub repository connected and accessible
- [x] AI service credentials validated and working
- [x] Local development environment fully functional

### 🔄 Pending
- [ ] Railway GitHub auto-deployment connection (manual setup required)
- [ ] Production database connection string configuration
- [ ] Environment variables set in Railway dashboard
- [ ] Live production deployment verified

---

**Created**: 2025-10-04  
**Authority**: Quest-CMS Archon Implementation  
**Next Action**: Complete Railway GitHub connection and configure production environment variables