"""
NiceGUI Admin Dashboard for Quest-CMS
Following documented real-time admin interface patterns
"""
from nicegui import ui, app
import asyncio
from typing import Dict, Any, Optional
import logging
from datetime import datetime

from ..database.operations import ArticleOperations
from ..database.connection import db_manager

logger = logging.getLogger(__name__)

class AdminDashboard:
    """Main admin dashboard following NiceGUI component pattern"""
    
    def __init__(self):
        self.article_ops = ArticleOperations()
        self.stats_cache = None
        self.cache_timestamp = None
        
    async def initialize(self):
        """Initialize dashboard and validate database"""
        try:
            await db_manager.initialize()
            logger.info("Admin dashboard initialized successfully")
        except Exception as e:
            logger.error(f"Dashboard initialization failed: {e}")
            raise e
    
    @ui.page('/admin')
    async def main_dashboard(self):
        """
        Main dashboard page following PROVEN PATTERN from documentation
        """
        await self.validate_access()
        
        # Header
        with ui.header():
            ui.label('Quest CMS - AI Content Platform').classes('text-xl font-bold')
            with ui.row().classes('ml-auto'):
                ui.button('Create Article', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
                ui.button('Review Queue', on_click=lambda: ui.navigate.to('/admin/review')).props('color=secondary')
        
        # Left navigation drawer
        with ui.left_drawer():
            ui.nav_link('Dashboard', '/admin').classes('text-blue-500')
            ui.nav_link('Create Content', '/admin/create').classes('text-green-500')
            ui.nav_link('Review Queue', '/admin/review').classes('text-orange-500')
            ui.nav_link('AI Tools', '/admin/ai').classes('text-purple-500')
            ui.nav_link('Search', '/admin/search').classes('text-gray-500')
            ui.separator()
            ui.nav_link('All Articles', '/admin/articles').classes('text-gray-600')
            ui.nav_link('Published', '/admin/articles?status=published').classes('text-gray-600')
            ui.nav_link('Drafts', '/admin/articles?status=draft').classes('text-gray-600')
        
        # Main content
        with ui.column().classes('w-full p-4'):
            await self.render_dashboard_metrics()
            await self.render_recent_articles()
    
    async def render_dashboard_metrics(self):
        """Real-time metrics display"""
        ui.markdown('## Dashboard Overview')
        
        # Get article statistics
        try:
            stats = await self.article_ops.get_article_stats()
            
            with ui.row().classes('w-full gap-4'):
                # Total articles metric
                with ui.card().classes('p-4'):
                    ui.label('Total Articles').classes('text-gray-600 text-sm')
                    ui.label(str(stats.get('total', 0))).classes('text-2xl font-bold text-blue-600')
                
                # Draft articles metric  
                with ui.card().classes('p-4'):
                    ui.label('Pending Review').classes('text-gray-600 text-sm')
                    ui.label(str(stats.get('review', 0))).classes('text-2xl font-bold text-orange-600')
                
                # Published articles metric
                with ui.card().classes('p-4'):
                    ui.label('Published').classes('text-gray-600 text-sm')
                    ui.label(str(stats.get('published', 0))).classes('text-2xl font-bold text-green-600')
                
                # Draft articles metric
                with ui.card().classes('p-4'):
                    ui.label('Drafts').classes('text-gray-600 text-sm')
                    ui.label(str(stats.get('draft', 0))).classes('text-2xl font-bold text-gray-600')
                
        except Exception as e:
            logger.error(f"Failed to render metrics: {e}")
            ui.notification(f'Failed to load metrics: {str(e)}', color='negative')
    
    async def render_recent_articles(self):
        """Display recent articles with real-time updates"""
        ui.markdown('## Recent Articles')
        
        try:
            # Get recent articles
            articles = await self.article_ops.list_articles(limit=10)
            
            if not articles:
                ui.label('No articles found. Create your first article!').classes('text-gray-500 italic')
                ui.button('Create Article', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
                return
            
            # Articles table
            columns = [
                {'name': 'title', 'label': 'Title', 'field': 'title', 'required': True, 'align': 'left'},
                {'name': 'status', 'label': 'Status', 'field': 'status', 'align': 'center'},
                {'name': 'created_at', 'label': 'Created', 'field': 'created_at', 'align': 'center'},
                {'name': 'ai_generated', 'label': 'AI Generated', 'field': 'ai_generated', 'align': 'center'},
                {'name': 'actions', 'label': 'Actions', 'field': 'actions', 'align': 'center'}
            ]
            
            # Process articles for table display
            table_data = []
            for article in articles:
                table_data.append({
                    'id': str(article['id']),
                    'title': article['title'][:60] + '...' if len(article['title']) > 60 else article['title'],
                    'status': self._format_status(article['status']),
                    'created_at': self._format_date(article['created_at']),
                    'ai_generated': '🤖' if article.get('ai_generated') else '👤',
                    'actions': str(article['id'])  # Will be replaced with action buttons
                })
            
            # Create table with custom action column
            table = ui.table(columns=columns, rows=table_data, pagination=10)
            table.add_slot('body-cell-actions', '''
                <q-td :props="props">
                    <q-btn flat round color="primary" icon="edit" size="sm" 
                           @click="$parent.$emit('edit', props.row)" />
                    <q-btn flat round color="secondary" icon="visibility" size="sm"
                           @click="$parent.$emit('view', props.row)" />
                </q-td>
            ''')
            
            # Handle table actions
            table.on('edit', lambda e: ui.navigate.to(f'/admin/edit/{e.args["id"]}'))
            table.on('view', lambda e: ui.navigate.to(f'/admin/view/{e.args["id"]}'))
            
        except Exception as e:
            logger.error(f"Failed to render recent articles: {e}")
            ui.notification(f'Failed to load articles: {str(e)}', color='negative')
    
    async def validate_access(self):
        """Security validation - can be enhanced with authentication"""
        # Basic validation - can be extended with user authentication
        pass
    
    def _format_status(self, status: str) -> str:
        """Format status with colors and icons"""
        status_formats = {
            'draft': '📝 Draft',
            'review': '🔍 Review',
            'published': '✅ Published',
            'archived': '📦 Archived'
        }
        return status_formats.get(status, status)
    
    def _format_date(self, date_obj) -> str:
        """Format date for display"""
        if not date_obj:
            return 'N/A'
        
        if isinstance(date_obj, str):
            try:
                date_obj = datetime.fromisoformat(date_obj.replace('Z', '+00:00'))
            except:
                return date_obj
        
        # Show relative time for recent dates
        now = datetime.now(date_obj.tzinfo)
        diff = now - date_obj
        
        if diff.days == 0:
            if diff.seconds < 3600:
                minutes = diff.seconds // 60
                return f'{minutes}m ago'
            else:
                hours = diff.seconds // 3600
                return f'{hours}h ago'
        elif diff.days < 7:
            return f'{diff.days}d ago'
        else:
            return date_obj.strftime('%m/%d/%Y')

# Global dashboard instance
admin_dashboard = AdminDashboard()