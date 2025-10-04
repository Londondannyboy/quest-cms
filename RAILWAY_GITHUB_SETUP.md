# Railway GitHub Auto-Deployment Setup Instructions

## 🎯 Current Status
- ✅ GitHub Repository: https://github.com/Londondannyboy/quest-cms
- ✅ Railway Project URL: https://quest-cms-production.railway.app
- ❌ GitHub repository not connected to Railway (manual setup required)

## 📋 Manual Setup Steps Required

### Step 1: Access Railway Dashboard
1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Log in with GitHub account linked to Londondannyboy

### Step 2: Connect GitHub Repository
1. Find the existing "quest-cms-production" project
2. Go to Service Settings
3. Look for "Source" or "Repository" section
4. Click "Connect Repository" or "Link GitHub"
5. Search for and select: `Londondannyboy/quest-cms`
6. Choose branch: `main` (default)

### Step 3: Configure Auto-Deployment
1. In Service Settings, ensure:
   - **Auto-Deploy**: Enabled
   - **Branch**: main
   - **Wait for CI**: Disabled (unless CI workflow exists)
2. Save settings

### Step 4: Environment Variables
Ensure these environment variables are set in Railway:
```
NEON_CONNECTION_STRING=postgresql://...
CLAUDE_API_KEY=sk-ant-api03-...
REPLICATE_API_TOKEN=r8_...
PORT=8080
```

### Step 5: Verify Deployment
1. Make a test commit to GitHub
2. Check Railway dashboard for automatic deployment
3. Verify live URL: https://quest-cms-production.railway.app

## 🔧 Alternative: CLI Method (if dashboard fails)

### Prerequisites
```bash
# Install Railway CLI (if not already installed)
npm install -g @railway/cli

# Login with token
railway login --token 22ada421-9487-45a3-b8cf-1ba21b9b39de
```

### Connect Repository via CLI
```bash
cd /Users/dankeegan/quest-cms
railway link [project-id]
railway environment production
railway domain
```

## ⚡ Post-Setup Verification

### Test Auto-Deployment
1. Make a small change to any file
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Test auto-deployment"
   git push origin main
   ```
3. Monitor Railway dashboard for deployment progress
4. Verify changes appear at production URL

### Expected Behavior
- Push to `main` branch → Automatic Railway deployment
- Build logs visible in Railway dashboard
- Live URL updates within 2-3 minutes

## 🚨 Troubleshooting

### If Connection Fails
1. Check GitHub app permissions for Railway
2. Ensure repository is public or Railway has private repo access
3. Verify GitHub account matches Railway account
4. Try disconnecting and reconnecting

### If Deployment Fails
1. Check Railway build logs
2. Verify all environment variables are set
3. Ensure `working_demo.py` is the correct entry point
4. Check for Python/dependency issues

---

**Next Action**: Complete manual setup through Railway dashboard, then verify auto-deployment is working.