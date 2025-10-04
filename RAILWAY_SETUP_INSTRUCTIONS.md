# Railway GitHub Setup - Step by Step

## 🚨 Current Issue
Railway can't find your GitHub repositories because the GitHub app isn't properly installed/authorized.

## ✅ Solution Steps

### Step 1: Install Railway GitHub App
1. **Go to Railway GitHub App Page**: https://github.com/apps/railway
2. **Click "Install"** (not just "Configure")
3. **Choose Installation**: Select your personal account `Londondannyboy`
4. **Repository Access**: Choose "All repositories" or select specific ones including `quest-cms`
5. **Click "Install"**

### Step 2: Check Authorization
1. **Go to GitHub Settings**: https://github.com/settings/applications
2. **Check "Authorized OAuth Apps"**: Should see "Railway" listed
3. **Check "Installed GitHub Apps"**: Should see "Railway" with access to repositories

### Step 3: Verify in Railway
1. **Go to Railway Dashboard**: https://railway.app/dashboard
2. **Try New Project**: https://railway.com/new/github
3. **Your repositories should now appear**

### Step 4: Connect Quest-CMS
1. **Search for `quest-cms`** in the repository list
2. **Click on the repository**
3. **Click "Deploy Now"**
4. **Set environment variables** (see credentials.md)

## 🔧 Troubleshooting

### If repositories still don't appear:
1. **Check account age**: GitHub account must be 90+ days old
2. **Revoke and reinstall**: Go to GitHub Settings > Applications, revoke Railway, then reinstall
3. **Try incognito browser**: Sometimes cached permissions cause issues

### Account Requirements:
- **GitHub account age**: Minimum 90 days for Railway basic tier
- **Active commit history**: 6+ months for higher tiers
- **Repository permissions**: Must have admin access to repositories

## 🎯 Next Steps After Connection
1. **Deploy Quest-CMS**: Should auto-deploy from main branch
2. **Set Environment Variables**: Use Railway dashboard
3. **Test Deployment**: Verify production URL works
4. **Enable Auto-Deploy**: Pushes to main branch auto-deploy

---

**Try this first, then we'll implement true Archon + Spec Kit architecture!**