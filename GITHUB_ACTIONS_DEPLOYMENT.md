# GitHub Actions Deployment to Railway

## Overview

This setup uses **GitHub Actions** to deploy Quest-CMS to Railway, avoiding the complex Railway GitHub integration issues. This approach is more reliable and gives you full control over the deployment process.

## ✅ What's Already Set Up

1. **GitHub Actions Workflow**: `.github/workflows/deploy-railway.yml`
2. **Production-Ready Code**: Quest-CMS with proper environment configuration
3. **Spec Kit Integration**: Complete specifications and slash commands working
4. **Security**: No credentials in repository, all handled via GitHub secrets

## 🔑 Required Setup Steps

### Step 1: Create Railway Project (Manual)

1. **Visit**: https://railway.app/dashboard
2. **Create New Project**: Choose "Empty Project"
3. **Note the Project ID**: You'll need this for GitHub secrets

### Step 2: Get Railway Token

1. **Go to**: https://railway.app/account/tokens
2. **Create New Token**: Name it "GitHub Actions Deployment"
3. **Copy the token**: You'll add this to GitHub secrets

### Step 3: Configure GitHub Secrets

Go to your GitHub repository: https://github.com/Londondannyboy/quest-cms/settings/secrets/actions

Add these secrets:

```bash
# Railway Configuration
RAILWAY_TOKEN=[your railway token from step 2]
RAILWAY_PROJECT_ID=[your project ID from step 1]

# Database Configuration  
NEON_CONNECTION_STRING=[your Neon PostgreSQL connection string]

# AI Services
CLAUDE_API_KEY=[your Claude API key]
REPLICATE_API_TOKEN=[your Replicate API token]
```

### Step 4: Trigger Deployment

1. **Push to main branch** (already done) or
2. **Manual trigger**: Go to Actions tab → "Deploy Quest-CMS to Railway" → "Run workflow"

## 🚀 Deployment Process

The GitHub Action will:

1. ✅ **Checkout code** from main branch
2. ✅ **Setup Python 3.11** environment  
3. ✅ **Install dependencies** from requirements.txt
4. ✅ **Run basic tests** to verify imports work
5. ✅ **Install Railway CLI** in the runner
6. ✅ **Deploy to Railway** using railway up
7. ✅ **Set environment variables** securely
8. ✅ **Wait for deployment** to complete
9. ✅ **Get deployment URL** and run health check

## 🔍 Monitoring Deployment

### GitHub Actions Tab
- **Real-time logs**: See each step of the deployment
- **Error details**: Full stack traces if anything fails
- **Deployment URL**: Displayed in the final step

### Railway Dashboard
- **Build logs**: See Railway's build process
- **Environment variables**: Verify all secrets are set
- **Service status**: Monitor application health

## ⚡ Benefits of This Approach

### **vs. Railway Direct Integration**
- ✅ **More reliable**: No account age restrictions
- ✅ **Better debugging**: Full GitHub Actions logs
- ✅ **Version control**: Deployment config in git
- ✅ **Flexible**: Can modify deployment steps easily

### **vs. Manual Deployment**
- ✅ **Automated**: Deploys on every push to main
- ✅ **Consistent**: Same process every time
- ✅ **Secure**: Credentials managed via GitHub secrets
- ✅ **Rollback capable**: Previous versions available

## 🔧 Troubleshooting

### If Deployment Fails

1. **Check GitHub Actions logs**: Repository → Actions tab
2. **Verify secrets**: Make sure all required secrets are set
3. **Check Railway dashboard**: Look for service errors
4. **Test locally**: Ensure app runs with `python working_demo.py`

### Common Issues

#### **Railway Token Invalid**
- **Solution**: Generate new token at https://railway.app/account/tokens
- **Update**: GitHub repository secrets

#### **Environment Variables Missing**
- **Solution**: Double-check all secrets in GitHub settings
- **Verify**: Names match exactly (case-sensitive)

#### **Deployment Timeout**
- **Solution**: Railway may be slow, check Railway dashboard
- **Wait**: Give it 5-10 minutes, then check service status

## 🎯 Success Indicators

### ✅ Successful Deployment
- **GitHub Actions**: All green checkmarks
- **Railway Dashboard**: Service shows "Active"
- **Health Check**: `/health` endpoint returns JSON
- **Admin Interface**: `/admin` loads Quest-CMS interface

### 🔄 Next Push = Auto-Deploy
- **Any push to main**: Triggers automatic deployment
- **No manual steps**: Completely automated pipeline
- **Environment variables**: Persist across deployments

## 🔒 Security Notes

### **GitHub Secrets Best Practices**
- ✅ **Never commit secrets**: All credentials in GitHub secrets only
- ✅ **Rotate regularly**: Update tokens quarterly  
- ✅ **Minimal permissions**: Railway token only for your project
- ✅ **Monitor usage**: Check Railway dashboard for unusual activity

### **Railway Security**
- ✅ **Environment variables**: Encrypted at rest and in transit
- ✅ **Network isolation**: Service isolated from other projects
- ✅ **HTTPS enforced**: Automatic SSL certificates
- ✅ **Access logs**: Available in Railway dashboard

## 📈 Scaling and Optimization

### **Performance Monitoring**
- **Railway Dashboard**: CPU, memory, response times
- **GitHub Actions**: Deployment time trends
- **Health Checks**: Automated monitoring possible

### **Cost Optimization**  
- **Pay-per-use**: Railway charges based on actual usage
- **Sleep mode**: Service scales to zero when idle
- **Resource limits**: Can set CPU/memory constraints

## 🎯 Summary

This GitHub Actions deployment approach gives you:

- ✅ **Reliable automated deployment** 
- ✅ **Complete deployment visibility**
- ✅ **Secure credential management**
- ✅ **Easy troubleshooting and rollback**
- ✅ **No Railway account age restrictions**

**Ready to deploy!** Just add the GitHub secrets and push to main branch.