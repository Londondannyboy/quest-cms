/**
 * Check Quest-CMS Railway deployment using Puppeteer
 */
const puppeteer = require('puppeteer');

async function checkDeployment() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    
    console.log('🔍 Checking Railway deployment...');
    
    try {
        // Check the Railway deployment URL
        const railwayUrl = 'https://quest-cms-production.railway.app';
        console.log(`📡 Checking: ${railwayUrl}`);
        
        await page.goto(railwayUrl, { waitUntil: 'networkidle0', timeout: 30000 });
        
        // Check if page loads
        const title = await page.title();
        console.log(`📄 Page title: ${title}`);
        
        // Check for Quest-CMS content
        const content = await page.content();
        
        if (content.includes('Quest CMS') || content.includes('railway')) {
            console.log('✅ Railway deployment is live!');
            
            // Check admin interface
            const adminUrl = `${railwayUrl}/admin`;
            console.log(`🔧 Checking admin interface: ${adminUrl}`);
            
            await page.goto(adminUrl, { waitUntil: 'networkidle0', timeout: 30000 });
            
            const adminContent = await page.content();
            if (adminContent.includes('Quest CMS') || adminContent.includes('Dashboard')) {
                console.log('✅ Admin interface is working!');
            } else {
                console.log('❌ Admin interface not found');
            }
            
        } else {
            console.log('❌ Quest-CMS content not found');
            console.log('📄 Page content preview:', content.substring(0, 500));
        }
        
    } catch (error) {
        console.log(`❌ Railway deployment check failed: ${error.message}`);
        
        // Check if it's a 404 or other error
        if (error.message.includes('net::ERR_NAME_NOT_RESOLVED')) {
            console.log('🔄 Railway deployment may still be building...');
        }
    }
    
    // Also check local deployment
    console.log('\n🏠 Checking local deployment...');
    try {
        await page.goto('http://localhost:8080/admin', { waitUntil: 'networkidle0', timeout: 10000 });
        
        const localContent = await page.content();
        if (localContent.includes('Quest CMS')) {
            console.log('✅ Local deployment is working perfectly!');
        } else {
            console.log('❌ Local deployment issue');
        }
        
    } catch (error) {
        console.log(`❌ Local deployment check failed: ${error.message}`);
    }
    
    await browser.close();
}

checkDeployment();