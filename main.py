"""
Quest-CMS Main Application
AI-First Content Management System following G3 methodology and proven patterns
"""
import os
import asyncio
import logging
from dotenv import load_dotenv
from nicegui import ui, app

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import application modules
from src.database.connection import db_manager
from src.admin.dashboard import admin_dashboard
from src.admin.content_editor import content_editor  
from src.admin.review_workflow import review_workflow
from src.ai_services.claude import claude_service
from src.ai_services.replicate_service import replicate_service
from src.utils.validation import SystemValidator

class QuestCMS:
    """
    Main Quest-CMS application class
    Following documented NiceGUI component pattern
    """
    
    def __init__(self):
        self.initialized = False
        
    async def initialize(self):
        """
        Initialize application with health checks
        Following MANDATORY validation patterns from guardrails
        """
        try:
            logger.info("Initializing Quest-CMS...")
            
            # 1. Validate environment configuration
            SystemValidator.validate_environment()
            logger.info("✅ Environment configuration validated")
            
            # 2. Check system resources
            SystemValidator.check_memory_usage()
            logger.info("✅ System resources validated")
            
            # 3. Initialize database
            await db_manager.initialize()
            logger.info("✅ Database connection established")
            
            # 4. Validate AI services
            await claude_service.validate_service()
            logger.info("✅ Claude API validated")
            
            await replicate_service.validate_service()
            logger.info("✅ Replicate API validated")
            
            # 5. Initialize admin components
            await admin_dashboard.initialize()
            logger.info("✅ Admin dashboard initialized")
            
            # 6. Performance baseline check
            performance_results = await SystemValidator.validate_performance_baseline()
            logger.info(f"✅ Performance baseline: {performance_results}")
            
            self.initialized = True
            logger.info("🚀 Quest-CMS initialization completed successfully!")
            
        except Exception as e:
            logger.error(f"❌ Quest-CMS initialization failed: {e}")
            raise e
    
    async def shutdown(self):
        """Cleanup on application shutdown"""
        try:
            await db_manager.close()
            logger.info("🔄 Quest-CMS shutdown completed")
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")

# Global application instance
quest_cms = QuestCMS()

# NiceGUI Application Setup
@ui.page('/')
async def index():
    """Root page redirects to admin dashboard"""
    ui.navigate.to('/admin')

@ui.page('/health')
async def health_check():
    """Health check endpoint"""
    try:
        if not quest_cms.initialized:
            raise ValueError("Application not initialized")
        
        # Perform basic health checks
        health_status = {
            'status': 'healthy',
            'database': 'connected',
            'ai_services': 'available',
            'memory_usage': SystemValidator.check_memory_usage()['percent_used']
        }
        
        ui.json(health_status)
        
    except Exception as e:
        ui.json({
            'status': 'unhealthy',
            'error': str(e)
        })

# Application startup and shutdown handlers
@app.on_startup
async def startup():
    """Application startup handler"""
    try:
        await quest_cms.initialize()
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        # In production, you might want to exit the application here
        raise e

@app.on_shutdown
async def shutdown():
    """Application shutdown handler"""
    await quest_cms.shutdown()

# Error handling
@app.exception_handler(404)
async def not_found(request, exc):
    """Handle 404 errors"""
    ui.navigate.to('/admin')

@app.exception_handler(500) 
async def server_error(request, exc):
    """Handle server errors"""
    logger.error(f"Server error: {exc}")
    ui.notification('An error occurred. Please try again.', color='negative')

if __name__ in {"__main__", "__mp_main__"}:
    # Application configuration
    app_config = {
        'title': 'Quest CMS - AI Content Platform',
        'reload': os.getenv('DEBUG', 'false').lower() == 'true',
        'show': False,  # Don't auto-open browser
        'port': int(os.getenv('PORT', 8080)),
        'host': '0.0.0.0'  # Allow external connections
    }
    
    logger.info(f"Starting Quest-CMS on port {app_config['port']}")
    logger.info("Admin interface will be available at: /admin")
    logger.info("Health check available at: /health")
    
    # Run the application
    ui.run(**app_config)