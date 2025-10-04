"""
Quest-CMS Demo Mode
Run the admin interface without requiring real database or API connections
"""
import os
import logging
from dotenv import load_dotenv
from nicegui import ui, app
import asyncio
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Mock data for demo
DEMO_ARTICLES = [
    {
        'id': '1',
        'title': 'Ultimate Guide to Digital Nomad Tax Planning',
        'status': 'published',
        'created_at': datetime.now(),
        'ai_generated': True,
        'quality_score': 8.5,
        'content': '''# Ultimate Guide to Digital Nomad Tax Planning

Digital nomadism has revolutionized how we think about work and lifestyle, but it comes with unique tax challenges that require careful planning.

## Understanding Tax Residency

As a digital nomad, your tax obligations depend on several factors...

### Key Considerations
- Physical presence tests
- Tax treaty benefits  
- Income sourcing rules

## Strategic Planning Tips

1. **Keep detailed records** of your travel and work locations
2. **Understand tax treaties** between countries
3. **Consider establishing tax residency** in a favorable jurisdiction

*This article was generated with AI assistance and reviewed by tax professionals.*'''
    },
    {
        'id': '2', 
        'title': 'Best Coworking Spaces in Lisbon for Remote Workers',
        'status': 'review',
        'created_at': datetime.now(),
        'ai_generated': True,
        'quality_score': 7.2,
        'content': '''# Best Coworking Spaces in Lisbon for Remote Workers

Lisbon has become a top destination for digital nomads, offering excellent coworking spaces that blend productivity with Portuguese charm.

## Top Recommendations

### 1. Second Home Lisboa
Located in the trendy Cais do Sodré area, this premium coworking space offers...

### 2. Utopia
A creative hub in the heart of Lisbon with flexible membership options...

*Content needs review for accuracy and completeness.*'''
    },
    {
        'id': '3',
        'title': 'Remote Work Tools Every Digital Nomad Needs in 2024', 
        'status': 'draft',
        'created_at': datetime.now(),
        'ai_generated': False,
        'quality_score': None,
        'content': '''# Remote Work Tools Every Digital Nomad Needs in 2024

Working remotely while traveling requires the right toolkit to stay productive and connected.

## Essential Categories

### Communication Tools
- Slack for team communication
- Zoom for video calls
- Discord for community building

### Productivity Apps
- Notion for note-taking and project management
- Toggl for time tracking
- 1Password for secure password management

*Draft article - needs expansion and real-world testing of tools.*'''
    }
]

class DemoQuestCMS:
    """Demo version of Quest-CMS for interface testing"""
    
    def __init__(self):
        self.articles = DEMO_ARTICLES
        
    async def get_article_stats(self):
        """Mock article statistics"""
        return {
            'total': len(self.articles),
            'draft': len([a for a in self.articles if a['status'] == 'draft']),
            'review': len([a for a in self.articles if a['status'] == 'review']),
            'published': len([a for a in self.articles if a['status'] == 'published']),
            'archived': 0
        }
    
    async def list_articles(self, status=None, limit=50):
        """Mock article listing"""
        if status:
            return [a for a in self.articles if a['status'] == status]
        return self.articles[:limit]
    
    async def get_article(self, article_id):
        """Mock get single article"""
        return next((a for a in self.articles if a['id'] == article_id), None)

# Global demo instance
demo_cms = DemoQuestCMS()

@ui.page('/')
async def index():
    """Root page redirects to admin dashboard"""
    ui.navigate.to('/admin')

@ui.page('/admin')
async def admin_dashboard():
    """Demo admin dashboard"""
    
    # Header
    with ui.header():
        ui.label('Quest CMS - AI Content Platform (DEMO MODE)').classes('text-xl font-bold')
        with ui.row().classes('ml-auto'):
            ui.badge('DEMO', color='orange')
            ui.button('Create Article', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
            ui.button('Review Queue', on_click=lambda: ui.navigate.to('/admin/review')).props('color=secondary')
    
    # Left navigation drawer
    with ui.left_drawer():
        ui.nav_link('Dashboard', '/admin').classes('text-blue-500')
        ui.nav_link('Create Content', '/admin/create').classes('text-green-500')
        ui.nav_link('Review Queue', '/admin/review').classes('text-orange-500')
        ui.nav_link('AI Tools', '/admin/ai').classes('text-purple-500')
        ui.separator()
        ui.nav_link('All Articles', '/admin/articles').classes('text-gray-600')
    
    # Main content
    with ui.column().classes('w-full p-4'):
        await render_dashboard_metrics()
        await render_recent_articles()

async def render_dashboard_metrics():
    """Demo metrics display"""
    ui.markdown('## Dashboard Overview')
    
    stats = await demo_cms.get_article_stats()
    
    with ui.row().classes('w-full gap-4'):
        # Total articles metric
        with ui.card().classes('p-4'):
            ui.label('Total Articles').classes('text-gray-600 text-sm')
            ui.label(str(stats.get('total', 0))).classes('text-2xl font-bold text-blue-600')
        
        # Review articles metric  
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

async def render_recent_articles():
    """Demo recent articles display"""
    ui.markdown('## Recent Articles')
    
    articles = await demo_cms.list_articles(limit=10)
    
    if not articles:
        ui.label('No articles found. Create your first article!').classes('text-gray-500 italic')
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
            'status': format_status(article['status']),
            'created_at': 'Just now',
            'ai_generated': '🤖' if article.get('ai_generated') else '👤',
            'actions': str(article['id'])
        })
    
    table = ui.table(columns=columns, rows=table_data, pagination=10)
    table.add_slot('body-cell-actions', '''
        <q-td :props="props">
            <q-btn flat round color="primary" icon="edit" size="sm" 
                   @click="$parent.$emit('edit', props.row)" />
            <q-btn flat round color="secondary" icon="visibility" size="sm"
                   @click="$parent.$emit('view', props.row)" />
        </q-td>
    ''')
    
    table.on('edit', lambda e: ui.notify(f'Edit article: {e.args["title"]}', color='info'))
    table.on('view', lambda e: ui.navigate.to(f'/admin/view/{e.args["id"]}'))

@ui.page('/admin/create')
async def create_article_page():
    """Demo content creation page"""
    
    # Header
    with ui.header():
        ui.label('Quest CMS - Create New Article (DEMO)').classes('text-xl font-bold')
        with ui.row().classes('ml-auto'):
            ui.badge('DEMO', color='orange')
            ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat')
    
    # Editor layout
    with ui.splitter(value=50) as splitter:
        
        # Left side: Content Editor
        with splitter.before:
            with ui.column().classes('p-4 h-full'):
                ui.markdown('### Content Editor')
                
                title_input = ui.input('Article Title', value='Sample Article Title').classes('w-full mb-4')
                content_textarea = ui.textarea(
                    'Content (Markdown)', 
                    value='# Sample Article\n\nThis is a demo article showing the Quest-CMS interface.\n\n## Features\n\n- AI-powered content generation\n- Real-time preview\n- Human review workflow\n\n*This is demo content.*'
                ).classes('w-full mb-4').style('height: 300px')
                
                # AI Tools (demo)
                with ui.expansion('🤖 AI Tools', icon='smart_toy').classes('w-full mb-4'):
                    with ui.row().classes('w-full gap-2'):
                        ui.button(
                            '🧠 Generate Content',
                            on_click=lambda: ui.notify('Demo: AI content generation would happen here', color='info')
                        ).props('color=purple')
                        
                        ui.button(
                            '✨ Enhance Content', 
                            on_click=lambda: ui.notify('Demo: Content enhancement would happen here', color='info')
                        ).props('color=blue')
                        
                        ui.button(
                            '🎨 Generate Image',
                            on_click=lambda: ui.notify('Demo: Image generation would happen here', color='info')
                        ).props('color=green')
                
                # Actions
                with ui.row().classes('w-full gap-2 mt-4'):
                    status_select = ui.select(['draft', 'review', 'published'], value='draft', label='Status')
                    ui.button('💾 Save', on_click=lambda: ui.notify('Demo: Article saved!', color='positive')).props('color=primary')
        
        # Right side: Live Preview
        with splitter.after:
            with ui.column().classes('p-4 h-full'):
                ui.markdown('### Live Preview')
                
                with ui.scroll_area().classes('h-full w-full border rounded p-4'):
                    preview_container = ui.column().classes('w-full')
                    
                    with preview_container:
                        ui.markdown('# Sample Article\n\nThis is a demo article showing the Quest-CMS interface.\n\n## Features\n\n- AI-powered content generation\n- Real-time preview\n- Human review workflow\n\n*This is demo content.*')
                
                # Update preview when typing
                def update_preview():
                    preview_container.clear()
                    with preview_container:
                        if title_input.value:
                            ui.markdown(f'# {title_input.value}')
                        if content_textarea.value:
                            ui.markdown(content_textarea.value)
                
                title_input.on('input', lambda: update_preview())
                content_textarea.on('input', lambda: update_preview())

@ui.page('/admin/review')
async def review_queue_page():
    """Demo review queue page"""
    
    # Header
    with ui.header():
        ui.label('Quest CMS - Review Queue (DEMO)').classes('text-xl font-bold')
        with ui.row().classes('ml-auto'):
            ui.badge('DEMO', color='orange')
            ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat')
    
    with ui.column().classes('w-full p-4'):
        ui.markdown('## Articles Pending Review')
        
        # Show articles needing review
        review_articles = await demo_cms.list_articles(status='review')
        
        if not review_articles:
            ui.markdown('🎉 **No articles pending review!**')
            ui.label('All content is up to date.').classes('text-gray-600')
            return
        
        for article in review_articles:
            with ui.card().classes('w-full mb-4'):
                with ui.card_section():
                    with ui.row().classes('w-full items-center'):
                        with ui.column().classes('flex-1'):
                            ui.label(article['title']).classes('font-semibold text-lg')
                            with ui.row().classes('text-sm text-gray-600 gap-4'):
                                ui.label('🤖 AI Generated' if article.get('ai_generated') else '👤 Human Created')
                                ui.label(f"⭐ {article.get('quality_score', 'N/A')}/10")
                        
                        ui.badge('NEEDS REVIEW', color='orange')
                        ui.button('Review', on_click=lambda a=article: show_review_dialog(a)).props('color=primary')

def show_review_dialog(article):
    """Show review dialog for article"""
    with ui.dialog().props('persistent') as dialog, ui.card():
        ui.markdown(f"## Review: {article['title']}")
        
        ui.markdown(article['content'][:500] + '...')
        
        with ui.row().classes('gap-2 mt-4'):
            ui.button('✅ Approve', on_click=lambda: (ui.notify('Article approved!', color='positive'), dialog.close())).props('color=green')
            ui.button('❌ Reject', on_click=lambda: (ui.notify('Article rejected', color='warning'), dialog.close())).props('color=red')
            ui.button('Cancel', on_click=dialog.close).props('flat')
    
    dialog.open()

@ui.page('/admin/view/{article_id}')
async def view_article_page(article_id: str):
    """Demo article view page"""
    article = await demo_cms.get_article(article_id)
    
    if not article:
        ui.markdown('# Article Not Found')
        ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin'))
        return
    
    # Header
    with ui.header():
        ui.label(f'Quest CMS - {article["title"]} (DEMO)').classes('text-xl font-bold')
        with ui.row().classes('ml-auto'):
            ui.badge('DEMO', color='orange')
            ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat')
    
    with ui.column().classes('w-full p-4'):
        ui.markdown(f"# {article['title']}")
        
        with ui.row().classes('text-sm text-gray-600 gap-4 mb-4'):
            ui.label(f"Status: {article['status'].title()}")
            ui.label('🤖 AI Generated' if article.get('ai_generated') else '👤 Human Created')
            if article.get('quality_score'):
                ui.label(f"⭐ Quality: {article['quality_score']}/10")
        
        with ui.card().classes('w-full'):
            with ui.card_section():
                ui.markdown(article['content'])

def format_status(status: str) -> str:
    """Format status with colors and icons"""
    status_formats = {
        'draft': '📝 Draft',
        'review': '🔍 Review', 
        'published': '✅ Published',
        'archived': '📦 Archived'
    }
    return status_formats.get(status, status)

@ui.page('/health')
async def health_check():
    """Demo health check"""
    ui.json({
        'status': 'healthy (demo mode)',
        'mode': 'demo',
        'features': ['admin_interface', 'content_editor', 'review_workflow'],
        'database': 'mock_data',
        'ai_services': 'demo_mode'
    })

if __name__ in {"__main__", "__mp_main__"}:
    logger.info("Starting Quest-CMS in DEMO MODE")
    logger.info("This demo shows the admin interface without requiring real API keys")
    logger.info("Admin interface will be available at: http://localhost:8080/admin")
    
    ui.run(
        title='Quest CMS - Demo Mode',
        port=8080,
        host='0.0.0.0',
        reload=True,
        show=False
    )