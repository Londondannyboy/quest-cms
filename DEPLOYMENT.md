# Quest-CMS Railway Deployment Guide

## 🚀 Deploy to Railway

### **Method 1: Web Interface (Recommended)**

1. **Create GitHub Repository**
   ```bash
   # If you have GitHub CLI
   gh repo create quest-cms --public --source=. --push
   
   # Or manually:
   # 1. Go to github.com/new
   # 2. Create repo named "quest-cms"
   # 3. Push this code to the repo
   ```

2. **Deploy via Railway Dashboard**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your quest-cms repository
   - Railway will automatically detect Python and deploy!

3. **Set Environment Variables in Railway**
   ```bash
   # Required for demo mode (current)
   PORT=8080
   
   # Required for production (when you have API keys)
   NEON_CONNECTION_STRING=your_neon_db_url
   CLAUDE_API_KEY=your_claude_key
   REPLICATE_API_TOKEN=your_replicate_key
   CLOUDINARY_URL=your_cloudinary_url
   ```

### **Method 2: Railway CLI**

```bash
# Install Railway CLI
curl -fsSL https://railway.app/install.sh | sh

# Login with your token
railway login --token 22ada421-9487-45a3-b8cf-1ba21b9b39de

# Deploy
railway up
```

## 🌐 Production URLs

After deployment, you'll get:
- **Admin Interface**: `https://your-app.railway.app/admin`
- **Health Check**: `https://your-app.railway.app/health`

## 🔧 Railway Configuration

The project includes these Railway-specific files:

### `railway.json`
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python3 simple_demo.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### `Procfile`
```
web: python3 simple_demo.py
```

### `requirements.txt`
All Python dependencies for automatic installation.

## 🎯 Quest Ecosystem Deployment Strategy

### **Your Architecture is Perfect:**

**Railway (Python Backends):**
- ✅ Quest-CMS (this project)
- 🔄 Quest-Pilot (intelligence platform)  
- 🔄 Quest-API (shared services)

**Vercel (Astro Frontends):**
- 🔄 Relocation-Quest
- 🔄 Rainmaker-Quest  
- 🔄 Placement-Quest

**Neon (Database):**
- 🔄 Shared PostgreSQL for all services
- 🔄 PostgREST API auto-generation
- 🔄 Vector embeddings for AI

## 💡 Next Steps

1. **Deploy Quest-CMS to Railway** (ready now!)
2. **Set up Neon database** (when ready for production)
3. **Configure AI API keys** (when ready for real content generation)
4. **Deploy Astro sites to Vercel** (for content consumption)

## 🔑 Your Railway Token

**Token**: `22ada421-9487-45a3-b8cf-1ba21b9b39de`
**Status**: ✅ Ready for deployment
**Usage**: Deploy Quest-CMS and future Quest ecosystem services

---

**Railway is perfect for Python backends like Quest-CMS while Vercel handles Astro static sites - exactly as you planned!** 🎯