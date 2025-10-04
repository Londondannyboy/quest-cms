"""
Simple Quest-CMS Demo - Fixed for NiceGUI 3.0
"""
from nicegui import ui
from datetime import datetime

# Demo data
demo_articles = [
    {
        'id': '1',
        'title': 'Ultimate Guide to Digital Nomad Tax Planning',
        'status': 'published',
        'content': '# Ultimate Guide to Digital Nomad Tax Planning\n\nDigital nomadism revolutionizes work...',
        'ai_generated': True,
        'quality_score': 8.5
    },
    {
        'id': '2', 
        'title': 'Best Coworking Spaces in Lisbon',
        'status': 'review',
        'content': '# Best Coworking Spaces in Lisbon\n\nLisbon has become a top destination...',
        'ai_generated': True,
        'quality_score': 7.2
    },
    {
        'id': '3',
        'title': 'Remote Work Tools for 2024',
        'status': 'draft',
        'content': '# Remote Work Tools for 2024\n\nWorking remotely requires the right toolkit...',
        'ai_generated': False,
        'quality_score': None
    }
]

@ui.page('/')
def index():
    ui.navigate.to('/admin')

@ui.page('/admin')
def admin_dashboard():
    """Quest-CMS Admin Dashboard"""
    
    # Header with modern styling
    with ui.header().classes('bg-blue-600'):
        with ui.row().classes('w-full items-center'):
            ui.label('Quest CMS - AI Content Platform').classes('text-xl font-bold text-white')
            ui.badge('DEMO MODE', color='orange').classes('ml-4')
            with ui.row().classes('ml-auto gap-2'):
                ui.button('Create Article', on_click=lambda: ui.navigate.to('/admin/create')).props('color=green outline')
                ui.button('Review Queue', on_click=lambda: ui.navigate.to('/admin/review')).props('color=orange outline')
    
    # Sidebar navigation
    with ui.left_drawer(top_corner=True, bottom_corner=True).classes('bg-gray-50'):
        with ui.column().classes('p-4 gap-2'):
            ui.button('📊 Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat color=blue align=left').classes('w-full')
            ui.button('✍️ Create Content', on_click=lambda: ui.navigate.to('/admin/create')).props('flat color=green align=left').classes('w-full')
            ui.button('🔍 Review Queue', on_click=lambda: ui.navigate.to('/admin/review')).props('flat color=orange align=left').classes('w-full')
            ui.separator()
            ui.button('📝 All Articles', on_click=lambda: ui.navigate.to('/admin/articles')).props('flat color=gray align=left').classes('w-full')
    
    # Main content
    with ui.column().classes('p-6 w-full'):
        render_dashboard_metrics()
        render_recent_articles()

def render_dashboard_metrics():
    """Dashboard metrics cards"""
    ui.markdown('## 📊 Dashboard Overview')
    
    stats = get_article_stats()
    
    with ui.row().classes('w-full gap-4 mb-6'):
        # Total articles
        with ui.card().classes('p-4 bg-blue-50 border-l-4 border-blue-500'):
            ui.label('Total Articles').classes('text-gray-600 text-sm font-medium')
            ui.label(str(stats['total'])).classes('text-3xl font-bold text-blue-600')
        
        # Pending review
        with ui.card().classes('p-4 bg-orange-50 border-l-4 border-orange-500'):
            ui.label('Pending Review').classes('text-gray-600 text-sm font-medium')
            ui.label(str(stats['review'])).classes('text-3xl font-bold text-orange-600')
        
        # Published
        with ui.card().classes('p-4 bg-green-50 border-l-4 border-green-500'):
            ui.label('Published').classes('text-gray-600 text-sm font-medium')
            ui.label(str(stats['published'])).classes('text-3xl font-bold text-green-600')
        
        # Drafts
        with ui.card().classes('p-4 bg-gray-50 border-l-4 border-gray-500'):
            ui.label('Drafts').classes('text-gray-600 text-sm font-medium')
            ui.label(str(stats['draft'])).classes('text-3xl font-bold text-gray-600')

def render_recent_articles():
    """Recent articles table"""
    ui.markdown('## 📄 Recent Articles')
    
    if not demo_articles:
        with ui.card().classes('p-6 text-center'):
            ui.markdown('🎉 **No articles found**')
            ui.label('Create your first article to get started!').classes('text-gray-600')
            ui.button('Create Article', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
        return
    
    # Articles grid
    with ui.column().classes('w-full gap-4'):
        for article in demo_articles:
            with ui.card().classes('w-full hover:shadow-lg transition-shadow'):
                with ui.card_section():
                    with ui.row().classes('w-full items-center justify-between'):
                        with ui.column().classes('flex-1'):
                            ui.label(article['title']).classes('text-lg font-semibold')
                            
                            with ui.row().classes('gap-4 mt-2'):
                                ui.badge(format_status(article['status']), color=get_status_color(article['status']))
                                ui.label('🤖 AI' if article.get('ai_generated') else '👤 Human').classes('text-sm text-gray-600')
                                if article.get('quality_score'):
                                    ui.label(f"⭐ {article['quality_score']}/10").classes('text-sm text-gray-600')
                        
                        with ui.row().classes('gap-2'):
                            ui.button('Edit', on_click=lambda a=article: edit_article(a['id'])).props('size=sm color=primary outline')
                            ui.button('View', on_click=lambda a=article: view_article(a['id'])).props('size=sm color=secondary outline')

@ui.page('/admin/create')
def create_article():
    """Content creation page"""
    
    with ui.header().classes('bg-green-600'):
        with ui.row().classes('w-full items-center'):
            ui.label('Create New Article').classes('text-xl font-bold text-white')
            ui.badge('DEMO MODE', color='orange').classes('ml-4')
            ui.button('← Back', on_click=lambda: ui.navigate.to('/admin')).props('color=white outline').classes('ml-auto')
    
    # Editor layout
    with ui.splitter(value=50).classes('h-screen'):
        
        # Editor side
        with ui.splitter.before:
            with ui.column().classes('p-6 h-full'):
                ui.markdown('### ✍️ Content Editor')
                
                title_input = ui.input('Article Title', value='New Article Title').classes('w-full mb-4')
                content_area = ui.textarea(
                    'Content (Markdown)', 
                    value='# New Article\n\nStart writing your content here...\n\n## Section 1\n\nYour content goes here.'
                ).classes('w-full mb-4').style('height: 300px')
                
                # AI Tools section
                with ui.expansion('🤖 AI Tools', icon='smart_toy').classes('w-full mb-4'):
                    with ui.row().classes('w-full gap-2'):
                        ui.button('🧠 Generate Content', on_click=lambda: ai_demo_action('Content generation')).props('color=purple')
                        ui.button('✨ Enhance Text', on_click=lambda: ai_demo_action('Content enhancement')).props('color=blue')
                        ui.button('🎨 Generate Image', on_click=lambda: ai_demo_action('Image generation')).props('color=green')
                
                # Metadata section
                with ui.expansion('🔍 SEO & Metadata').classes('w-full mb-4'):
                    ui.input('SEO Title').classes('w-full mb-2')
                    ui.textarea('SEO Description', placeholder='Max 155 characters').classes('w-full mb-2').style('height: 80px')
                    with ui.row().classes('w-full gap-2'):
                        ui.select(['Guide', 'Tutorial', 'News', 'Analysis'], label='Category').classes('flex-1')
                        ui.input('Tags', placeholder='tag1, tag2, tag3').classes('flex-1')
                
                # Actions
                with ui.row().classes('w-full gap-2 mt-4'):
                    ui.select(['draft', 'review', 'published'], value='draft', label='Status').classes('flex-1')
                    ui.button('💾 Save Article', on_click=lambda: save_demo_action()).props('color=primary')
        
        # Preview side
        with ui.splitter.after:
            with ui.column().classes('p-6 h-full'):
                ui.markdown('### 👀 Live Preview')
                
                with ui.scroll_area().classes('h-full w-full border rounded p-4 bg-white'):
                    preview_container = ui.column().classes('w-full')
                    
                    with preview_container:
                        ui.markdown('# New Article\n\nStart writing your content here...\n\n## Section 1\n\nYour content goes here.')
                
                def update_preview():
                    preview_container.clear()
                    with preview_container:
                        if title_input.value:
                            ui.markdown(f'# {title_input.value}')
                        if content_area.value:
                            ui.markdown(content_area.value)
                
                title_input.on('input', lambda: update_preview())
                content_area.on('input', lambda: update_preview())

@ui.page('/admin/review')
def review_queue():
    """Review queue page"""
    
    with ui.header().classes('bg-orange-600'):
        with ui.row().classes('w-full items-center'):
            ui.label('Review Queue').classes('text-xl font-bold text-white')
            ui.badge('DEMO MODE', color='amber').classes('ml-4')
            ui.button('← Back', on_click=lambda: ui.navigate.to('/admin')).props('color=white outline').classes('ml-auto')
    
    with ui.column().classes('p-6 w-full'):
        ui.markdown('## 🔍 Articles Pending Review')
        
        review_articles = [a for a in demo_articles if a['status'] == 'review']
        
        if not review_articles:
            with ui.card().classes('p-6 text-center'):
                ui.markdown('🎉 **No articles pending review!**')
                ui.label('All content is up to date.').classes('text-gray-600 mb-4')
                ui.button('Create New Content', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
            return
        
        for article in review_articles:
            with ui.card().classes('w-full mb-4 border-l-4 border-orange-500'):
                with ui.card_section():
                    with ui.row().classes('w-full items-center justify-between'):
                        with ui.column().classes('flex-1'):
                            ui.label(article['title']).classes('text-lg font-semibold')
                            
                            with ui.row().classes('gap-4 mt-2 text-sm text-gray-600'):
                                ui.label('🤖 AI Generated' if article.get('ai_generated') else '👤 Human Created')
                                if article.get('quality_score'):
                                    ui.label(f"⭐ Quality: {article['quality_score']}/10")
                                ui.label('🕒 Waiting for review')
                        
                        ui.badge('NEEDS REVIEW', color='orange').classes('mr-4')
                        ui.button('Review Article', on_click=lambda a=article: show_review_dialog(a)).props('color=primary')

@ui.page('/admin/view/{article_id}')
def view_article(article_id: str):
    """Article view page"""
    article = next((a for a in demo_articles if a['id'] == article_id), None)
    
    if not article:
        with ui.column().classes('p-6'):
            ui.markdown('# ❌ Article Not Found')
            ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('color=primary')
        return
    
    with ui.header():
        with ui.row().classes('w-full items-center'):
            ui.label(f"View: {article['title'][:50]}...").classes('text-xl font-bold')
            ui.badge('DEMO MODE', color='orange').classes('ml-4')
            ui.button('← Back', on_click=lambda: ui.navigate.to('/admin')).props('outline').classes('ml-auto')
    
    with ui.column().classes('p-6 w-full max-w-4xl mx-auto'):
        ui.markdown(f"# {article['title']}")
        
        with ui.row().classes('gap-4 mb-6 text-sm text-gray-600'):
            ui.badge(format_status(article['status']), color=get_status_color(article['status']))
            ui.label('🤖 AI Generated' if article.get('ai_generated') else '👤 Human Created')
            if article.get('quality_score'):
                ui.label(f"⭐ Quality: {article['quality_score']}/10")
        
        with ui.card().classes('w-full'):
            with ui.card_section():
                ui.markdown(article['content'])

@ui.page('/health')
def health_check():
    """Health check endpoint"""
    with ui.column().classes('p-6'):
        ui.json({
            'status': 'healthy',
            'mode': 'demo',
            'version': 'Quest-CMS v1.0',
            'features': ['admin_interface', 'content_editor', 'review_workflow'],
            'database': 'demo_data',
            'ai_services': 'demo_mode'
        })

# Helper functions
def get_article_stats():
    """Get demo article statistics"""
    return {
        'total': len(demo_articles),
        'draft': len([a for a in demo_articles if a['status'] == 'draft']),
        'review': len([a for a in demo_articles if a['status'] == 'review']),
        'published': len([a for a in demo_articles if a['status'] == 'published']),
        'archived': 0
    }

def format_status(status):
    """Format status for display"""
    status_map = {
        'draft': 'Draft',
        'review': 'Under Review',
        'published': 'Published',
        'archived': 'Archived'
    }
    return status_map.get(status, status)

def get_status_color(status):
    """Get color for status"""
    color_map = {
        'draft': 'gray',
        'review': 'orange', 
        'published': 'green',
        'archived': 'blue'
    }
    return color_map.get(status, 'gray')

def ai_demo_action(action_type):
    """Demo AI action"""
    ui.notify(f'🤖 DEMO: {action_type} would happen here with real API keys', color='info', timeout=3000)

def save_demo_action():
    """Demo save action"""
    ui.notify('💾 DEMO: Article saved successfully!', color='positive', timeout=2000)

def edit_article(article_id):
    """Edit article action"""
    ui.notify(f'✏️ DEMO: Editing article {article_id}', color='info')

def show_review_dialog(article):
    """Show review dialog"""
    with ui.dialog().props('persistent') as dialog, ui.card():
        with ui.card_section():
            ui.markdown(f"## Review: {article['title']}")
            ui.markdown(article['content'][:300] + '...')
            
            ui.markdown('### Quality Assessment')
            quality_slider = ui.slider(min=1, max=10, value=article.get('quality_score', 7), step=1).props('label-always')
            
            notes_input = ui.textarea('Review Notes', placeholder='Add your review comments...').classes('w-full')
        
        with ui.card_actions():
            with ui.row().classes('gap-2'):
                ui.button('✅ Approve', on_click=lambda: (ui.notify('Article approved!', color='positive'), dialog.close())).props('color=green')
                ui.button('❌ Reject', on_click=lambda: (ui.notify('Article rejected', color='warning'), dialog.close())).props('color=red')
                ui.button('Cancel', on_click=dialog.close).props('outline')
    
    dialog.open()

if __name__ in {"__main__", "__mp_main__"}:
    print("🚀 Starting Quest-CMS Demo Mode")
    print("📝 Admin Interface: http://localhost:8080/admin")
    print("🔍 Health Check: http://localhost:8080/health")
    print("🎯 This demo shows the complete admin interface without requiring API keys")
    
    ui.run(
        title='Quest CMS - Demo Mode',
        port=8080,
        host='0.0.0.0',
        reload=True,
        show=False,
        favicon='🚀'
    )