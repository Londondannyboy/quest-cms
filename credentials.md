# Quest-CMS Credentials

## Railway Deployment
- **Railway Token**: `22ada421-9487-45a3-b8cf-1ba21b9b39de`
- **Platform**: railway.app
- **Use Case**: Python backend deployment for Quest-CMS
- **Created**: October 2025

## Environment Variables for Production
```bash
# Railway Environment Variables
RAILWAY_TOKEN=22ada421-9487-45a3-b8cf-1ba21b9b39de

# Required for Full Quest-CMS (Production)
NEON_CONNECTION_STRING=postgresql://user:pass@ep-xxx.us-east-1.aws.neon.tech/neondb
CLAUDE_API_KEY=sk-ant-api03-xxx
REPLICATE_API_TOKEN=r8_xxx
CLOUDINARY_URL=cloudinary://xxx:xxx@your-cloud-name

# Application Settings
PORT=8080
DEBUG=false
```

## Deployment Strategy
- **Backend (Quest-CMS)**: Railway (Python/NiceGUI)
- **Frontend Publishing (Astro sites)**: Vercel (Static sites)
- **Database**: Neon PostgreSQL
- **AI Services**: Anthropic Claude + Replicate