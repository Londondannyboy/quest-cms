"""
Human Review Workflow for Quest-CMS
Implementing review workflow for AI-generated content quality control
"""
from nicegui import ui
import asyncio
from typing import Dict, Any, Optional, List
import logging
import json

from ..database.operations import ArticleOperations
from ..ai_services.claude import claude_service

logger = logging.getLogger(__name__)

class ReviewWorkflow:
    """Human review workflow for AI-generated content"""
    
    def __init__(self):
        self.article_ops = ArticleOperations()
        self.current_article = None
        
        # UI component references
        self.article_list = None
        self.content_display = None
        self.review_notes_input = None
        self.quality_score_slider = None
        self.decision_buttons = None
    
    @ui.page('/admin/review')
    async def review_queue_page(self):
        """Review queue page for content approval"""
        
        # Header
        with ui.header():
            ui.label('Quest CMS - Review Queue').classes('text-xl font-bold')
            with ui.row().classes('ml-auto'):
                ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat')
                ui.button('🔄 Refresh Queue', on_click=self._refresh_queue).props('color=secondary')
        
        # Main layout
        with ui.splitter(value=30) as splitter:
            
            # Left side: Articles pending review
            with splitter.before:
                with ui.column().classes('p-4 h-full'):
                    ui.markdown('### Articles Pending Review')
                    
                    # Filter controls
                    with ui.row().classes('w-full mb-4'):
                        filter_select = ui.select(
                            ['All', 'AI Generated', 'Human Created', 'High Priority'],
                            value='All',
                            label='Filter'
                        ).classes('flex-1')
                        filter_select.on('update:model-value', self._filter_articles)
                    
                    # Articles list container
                    with ui.scroll_area().classes('h-full'):
                        self.article_list = ui.column().classes('w-full')
                        await self._load_review_queue()
            
            # Right side: Article review interface
            with splitter.after:
                with ui.column().classes('p-4 h-full'):
                    ui.markdown('### Review Article')
                    
                    # Article content display
                    with ui.scroll_area().classes('h-full'):
                        self.content_display = ui.column().classes('w-full')
                        
                        with self.content_display:
                            ui.markdown('*Select an article from the queue to begin review*').classes('text-gray-500 italic text-center mt-8')
    
    async def _load_review_queue(self):
        """Load articles pending review"""
        try:
            # Get articles with review status
            review_articles = await self.article_ops.list_articles(status='review', limit=50)
            
            # Also include draft articles that are AI-generated
            draft_articles = await self.article_ops.list_articles(status='draft', limit=50)
            ai_drafts = [a for a in draft_articles if a.get('ai_generated', False)]
            
            all_articles = review_articles + ai_drafts
            
            self.article_list.clear()
            
            if not all_articles:
                with self.article_list:
                    ui.card().classes('p-4 text-center').style('border: 2px dashed #e0e0e0'):
                        ui.markdown('🎉 **No articles pending review!**')
                        ui.label('All content is up to date.').classes('text-gray-600')
                        ui.button('Create New Content', on_click=lambda: ui.navigate.to('/admin/create')).props('color=primary')
                return
            
            # Sort by priority (AI-generated first, then by creation date)
            all_articles.sort(key=lambda x: (not x.get('ai_generated', False), x['created_at']), reverse=True)
            
            with self.article_list:
                for article in all_articles:
                    await self._render_article_card(article)
                    
        except Exception as e:
            logger.error(f"Failed to load review queue: {e}")
            ui.notification(f'Failed to load review queue: {str(e)}', color='negative')
    
    async def _render_article_card(self, article: Dict[str, Any]):
        """Render individual article card in review queue"""
        
        # Determine priority and styling
        is_ai_generated = article.get('ai_generated', False)
        priority_color = 'border-l-4 border-orange-500' if is_ai_generated else 'border-l-4 border-blue-500'
        
        with ui.card().classes(f'w-full mb-2 cursor-pointer hover:shadow-lg {priority_color}').on('click', lambda a=article: self._select_article_for_review(a)):
            with ui.card_section():
                with ui.row().classes('w-full items-center'):
                    with ui.column().classes('flex-1'):
                        # Title
                        title = article['title'][:50] + '...' if len(article['title']) > 50 else article['title']
                        ui.label(title).classes('font-semibold text-lg')
                        
                        # Metadata
                        with ui.row().classes('text-sm text-gray-600 gap-4'):
                            ui.label(f"📅 {self._format_date(article['created_at'])}")
                            ui.label('🤖 AI Generated' if is_ai_generated else '👤 Human Created')
                            ui.label(f"📊 Status: {article['status'].title()}")
                            
                            # Quality score if available
                            if article.get('quality_score'):
                                score = article['quality_score']
                                score_color = 'text-green-600' if score >= 8 else 'text-orange-600' if score >= 6 else 'text-red-600'
                                ui.label(f"⭐ {score}/10").classes(score_color)
                    
                    # Priority indicator
                    if is_ai_generated:
                        ui.badge('HIGH PRIORITY', color='orange').classes('ml-2')
    
    async def _select_article_for_review(self, article: Dict[str, Any]):
        """Select article for detailed review"""
        try:
            self.current_article = article
            
            # Clear and populate content display
            self.content_display.clear()
            
            with self.content_display:
                # Article header
                with ui.card().classes('w-full mb-4'):
                    with ui.card_section():
                        ui.markdown(f"# {article['title']}")
                        
                        with ui.row().classes('text-sm text-gray-600 gap-4 mt-2'):
                            ui.label(f"📅 Created: {self._format_date(article['created_at'])}")
                            ui.label('🤖 AI Generated' if article.get('ai_generated') else '👤 Human Created')
                            ui.label(f"📝 Words: {len(article['content'].split())}")
                            
                            if article.get('ai_model'):
                                ui.label(f"🧠 Model: {article['ai_model']}")
                
                # Content preview
                with ui.card().classes('w-full mb-4'):
                    with ui.card_section():
                        ui.label('Article Content').classes('font-semibold mb-2')
                        ui.markdown(article['content'][:2000] + '...' if len(article['content']) > 2000 else article['content'])
                
                # AI Analysis (if AI-generated)
                if article.get('ai_generated'):
                    await self._render_ai_analysis(article)
                
                # Review interface
                await self._render_review_interface(article)
                
        except Exception as e:
            logger.error(f"Failed to select article for review: {e}")
            ui.notification(f'Failed to load article: {str(e)}', color='negative')
    
    async def _render_ai_analysis(self, article: Dict[str, Any]):
        """Render AI content analysis"""
        with ui.card().classes('w-full mb-4'):
            with ui.card_section():
                ui.label('🔍 AI Content Analysis').classes('font-semibold mb-2')
                
                try:
                    # Perform quality validation
                    validation_result = await claude_service.validate_content_quality(article['content'])
                    
                    with ui.row().classes('gap-4 mb-2'):
                        # Quality score
                        score = validation_result['quality_score']
                        score_color = 'text-green-600' if score >= 8 else 'text-orange-600' if score >= 6 else 'text-red-600'
                        ui.label(f"Quality Score: {score}/10").classes(f'font-semibold {score_color}')
                        
                        # Word count
                        ui.label(f"Word Count: {validation_result['word_count']}")
                    
                    # Issues (if any)
                    if validation_result.get('issues'):
                        ui.label('Issues Found:').classes('font-medium text-orange-600')
                        for issue in validation_result['issues']:
                            ui.label(f"• {issue}").classes('text-sm text-gray-700 ml-4')
                    else:
                        ui.label('✅ No issues detected').classes('text-green-600')
                        
                except Exception as e:
                    ui.label(f'⚠️ AI analysis failed: {str(e)}').classes('text-red-600')
    
    async def _render_review_interface(self, article: Dict[str, Any]):
        """Render human review interface"""
        with ui.card().classes('w-full'):
            with ui.card_section():
                ui.label('👤 Human Review').classes('font-semibold mb-4')
                
                # Quality score slider
                with ui.row().classes('w-full items-center mb-4'):
                    ui.label('Quality Score:').classes('w-32')
                    self.quality_score_slider = ui.slider(
                        min=1, max=10, step=1, value=article.get('quality_score', 7)
                    ).classes('flex-1')
                    score_display = ui.label(str(int(self.quality_score_slider.value))).classes('w-8 text-center')
                    self.quality_score_slider.on('update:model-value', lambda e: score_display.set_text(str(int(e.args))))
                
                # Review notes
                self.review_notes_input = ui.textarea(
                    'Review Notes',
                    placeholder='Add any notes about content quality, required changes, or approval reasons...',
                    value=article.get('review_notes', '')
                ).classes('w-full mb-4').style('height: 120px')
                
                # Decision buttons
                with ui.row().classes('w-full gap-2'):
                    ui.button(
                        '✅ Approve & Publish',
                        on_click=lambda: self._approve_article('published')
                    ).props('color=green').classes('flex-1')
                    
                    ui.button(
                        '📝 Approve as Draft',
                        on_click=lambda: self._approve_article('draft')
                    ).props('color=blue').classes('flex-1')
                    
                    ui.button(
                        '❌ Reject',
                        on_click=self._reject_article
                    ).props('color=red').classes('flex-1')
                    
                    ui.button(
                        '📤 Edit',
                        on_click=lambda: ui.navigate.to(f'/admin/edit/{article["id"]}')
                    ).props('color=orange').classes('flex-1')
    
    async def _approve_article(self, new_status: str):
        """Approve article with specified status"""
        try:
            if not self.current_article:
                return
            
            # Update article with review data
            success = await self.article_ops.update_article(
                article_id=str(self.current_article['id']),
                status=new_status,
                reviewed_by='admin',  # TODO: Replace with actual user
                review_notes=self.review_notes_input.value,
                quality_score=self.quality_score_slider.value
            )
            
            if success:
                status_text = 'published' if new_status == 'published' else 'approved as draft'
                ui.notification(f'Article {status_text} successfully!', color='positive')
                
                # Refresh queue and clear selection
                await self._refresh_queue()
                self._clear_review_interface()
            else:
                ui.notification('Failed to update article', color='negative')
                
        except Exception as e:
            logger.error(f"Failed to approve article: {e}")
            ui.notification(f'Approval failed: {str(e)}', color='negative')
    
    async def _reject_article(self):
        """Reject article and move back to draft"""
        try:
            if not self.current_article:
                return
            
            # Update article with rejection notes
            success = await self.article_ops.update_article(
                article_id=str(self.current_article['id']),
                status='draft',
                reviewed_by='admin',  # TODO: Replace with actual user
                review_notes=f"REJECTED: {self.review_notes_input.value}",
                quality_score=self.quality_score_slider.value
            )
            
            if success:
                ui.notification('Article rejected and moved to drafts', color='warning')
                
                # Refresh queue and clear selection
                await self._refresh_queue()
                self._clear_review_interface()
            else:
                ui.notification('Failed to reject article', color='negative')
                
        except Exception as e:
            logger.error(f"Failed to reject article: {e}")
            ui.notification(f'Rejection failed: {str(e)}', color='negative')
    
    async def _refresh_queue(self):
        """Refresh the review queue"""
        await self._load_review_queue()
    
    async def _filter_articles(self, filter_value):
        """Filter articles in review queue"""
        # TODO: Implement filtering logic
        await self._load_review_queue()
    
    def _clear_review_interface(self):
        """Clear the review interface"""
        self.current_article = None
        self.content_display.clear()
        
        with self.content_display:
            ui.markdown('*Select an article from the queue to begin review*').classes('text-gray-500 italic text-center mt-8')
    
    def _format_date(self, date_obj) -> str:
        """Format date for display"""
        if not date_obj:
            return 'N/A'
        
        # Simple date formatting
        try:
            if hasattr(date_obj, 'strftime'):
                return date_obj.strftime('%m/%d/%Y %H:%M')
            else:
                return str(date_obj)[:16]  # Basic string truncation
        except:
            return str(date_obj)

# Global review workflow instance
review_workflow = ReviewWorkflow()