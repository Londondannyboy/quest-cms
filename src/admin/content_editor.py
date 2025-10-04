"""
Live Content Editor for Quest-CMS
Following documented live preview pattern with real-time updates
"""
from nicegui import ui
import asyncio
from typing import Dict, Any, Optional
import logging
import json

from ..database.operations import ArticleOperations
from ..ai_services.claude import claude_service
from ..ai_services.replicate_service import replicate_service

logger = logging.getLogger(__name__)

class ContentEditor:
    """Live content editor with real-time preview following documented pattern"""
    
    def __init__(self):
        self.article_ops = ArticleOperations()
        self.current_article_id = None
        
        # UI component references
        self.title_input = None
        self.content_textarea = None
        self.preview_container = None
        self.seo_title_input = None
        self.seo_description_input = None
        self.category_select = None
        self.tags_input = None
        self.status_select = None
        
        # AI operation status
        self.ai_operation_status = None
    
    @ui.page('/admin/create')
    async def create_article_page(self):
        """Create new article page with live editor"""
        await self._render_editor_page()
    
    @ui.page('/admin/edit/{article_id}')
    async def edit_article_page(self, article_id: str):
        """Edit existing article page"""
        self.current_article_id = article_id
        await self._render_editor_page(article_id)
    
    async def _render_editor_page(self, article_id: Optional[str] = None):
        """
        Render content editor with live preview
        Following PROVEN PATTERN from documentation
        """
        
        # Header
        with ui.header():
            page_title = 'Edit Article' if article_id else 'Create New Article'
            ui.label(f'Quest CMS - {page_title}').classes('text-xl font-bold')
            with ui.row().classes('ml-auto'):
                ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/admin')).props('flat')
        
        # Main editor layout with splitter
        with ui.splitter(value=50) as splitter:
            
            # Left side: Content Editor
            with splitter.before:
                with ui.column().classes('p-4 h-full'):
                    ui.markdown('### Content Editor')
                    
                    # Article title
                    self.title_input = ui.input('Article Title').classes('w-full mb-4')
                    self.title_input.on('input', self._update_preview)
                    
                    # Content textarea with markdown support
                    self.content_textarea = ui.textarea(
                        'Content (Markdown)', 
                        placeholder='Write your article content in Markdown...'
                    ).classes('w-full mb-4').style('height: 400px')
                    self.content_textarea.on('input', self._update_preview)
                    
                    # AI Enhancement Tools
                    with ui.expansion('🤖 AI Tools', icon='smart_toy').classes('w-full mb-4'):
                        with ui.row().classes('w-full gap-2'):
                            ui.button(
                                '🧠 Generate Content',
                                on_click=self._generate_content_with_ai
                            ).props('color=purple')
                            
                            ui.button(
                                '✨ Enhance Content', 
                                on_click=self._enhance_content_with_ai
                            ).props('color=blue')
                            
                            ui.button(
                                '🎨 Generate Image',
                                on_click=self._generate_featured_image
                            ).props('color=green')
                        
                        # AI operation status
                        self.ai_operation_status = ui.label('').classes('text-sm text-gray-600')
                    
                    # SEO and Metadata
                    with ui.expansion('🔍 SEO & Metadata', icon='search').classes('w-full mb-4'):
                        self.seo_title_input = ui.input('SEO Title').classes('w-full mb-2')
                        self.seo_description_input = ui.textarea(
                            'SEO Description', 
                            placeholder='Max 155 characters'
                        ).classes('w-full mb-2').style('height: 80px')
                        
                        with ui.row().classes('w-full gap-2'):
                            self.category_select = ui.select(
                                ['Guide', 'Tutorial', 'News', 'Analysis', 'Comparison', 'Review'],
                                label='Category'
                            ).classes('flex-1')
                            
                            self.tags_input = ui.input(
                                'Tags', 
                                placeholder='tag1, tag2, tag3'
                            ).classes('flex-1')
                    
                    # Article Status and Actions
                    with ui.row().classes('w-full gap-2 mt-4'):
                        self.status_select = ui.select(
                            ['draft', 'review', 'published', 'archived'],
                            label='Status',
                            value='draft'
                        ).classes('flex-1')
                        
                        ui.button('💾 Save', on_click=self._save_article).props('color=primary')
                        ui.button('👁 Preview', on_click=self._preview_article).props('color=secondary')
            
            # Right side: Live Preview
            with splitter.after:
                with ui.column().classes('p-4 h-full'):
                    ui.markdown('### Live Preview')
                    
                    # Preview container with scroll
                    with ui.scroll_area().classes('h-full w-full border rounded p-4'):
                        self.preview_container = ui.column().classes('w-full')
                        
                        # Initial preview message
                        with self.preview_container:
                            ui.markdown('*Start typing to see live preview...*').classes('text-gray-500 italic')
        
        # Load existing article if editing
        if article_id:
            await self._load_article(article_id)
    
    async def _load_article(self, article_id: str):
        """Load existing article for editing"""
        try:
            article = await self.article_ops.get_article(article_id)
            if not article:
                ui.notification('Article not found', color='negative')
                ui.navigate.to('/admin')
                return
            
            # Populate form fields
            self.title_input.value = article['title']
            self.content_textarea.value = article['content']
            self.status_select.value = article['status']
            
            # Load metadata from attributes
            attributes = article.get('attributes', {})
            if isinstance(attributes, str):
                attributes = json.loads(attributes)
            
            self.seo_title_input.value = attributes.get('seo_title', '')
            self.seo_description_input.value = attributes.get('seo_description', '')
            self.category_select.value = attributes.get('category', '')
            self.tags_input.value = ', '.join(attributes.get('tags', []))
            
            # Update preview
            await self._update_preview()
            
            ui.notification(f'Loaded article: {article["title"]}', color='positive')
            
        except Exception as e:
            logger.error(f"Failed to load article {article_id}: {e}")
            ui.notification(f'Failed to load article: {str(e)}', color='negative')
    
    async def _update_preview(self):
        """Update live preview with current content"""
        try:
            title = self.title_input.value if self.title_input else ''
            content = self.content_textarea.value if self.content_textarea else ''
            
            # Clear and update preview
            self.preview_container.clear()
            
            with self.preview_container:
                if title:
                    ui.markdown(f'# {title}').classes('border-b pb-2 mb-4')
                
                if content:
                    ui.markdown(content)
                else:
                    ui.markdown('*Start typing to see live preview...*').classes('text-gray-500 italic')
                    
        except Exception as e:
            logger.error(f"Preview update failed: {e}")
    
    async def _generate_content_with_ai(self):
        """Generate content using Claude AI"""
        try:
            if not self.title_input.value:
                ui.notification('Please enter a title first', color='warning')
                return
            
            self.ai_operation_status.text = '🧠 Generating content with Claude...'
            
            # Generate content
            result = await claude_service.generate_article_content(
                topic=self.title_input.value,
                target_audience="digital_nomads",
                word_count=1000
            )
            
            # Update form with generated content
            self.title_input.value = result['title']
            self.content_textarea.value = result['content']
            self.seo_description_input.value = result.get('seo_description', '')
            
            # Update preview
            await self._update_preview()
            
            self.ai_operation_status.text = f'✅ Generated {result["word_count"]} words'
            ui.notification('Content generated successfully!', color='positive')
            
        except Exception as e:
            logger.error(f"Content generation failed: {e}")
            self.ai_operation_status.text = f'❌ Generation failed: {str(e)}'
            ui.notification(f'Content generation failed: {str(e)}', color='negative')
    
    async def _enhance_content_with_ai(self):
        """Enhance existing content with Claude AI"""
        try:
            if not self.content_textarea.value:
                ui.notification('Please enter content to enhance', color='warning')
                return
            
            self.ai_operation_status.text = '✨ Enhancing content with Claude...'
            
            # Enhance content
            enhanced_content = await claude_service.enhance_content(
                content=self.content_textarea.value,
                enhancement_type="general"
            )
            
            # Update content
            self.content_textarea.value = enhanced_content
            
            # Update preview
            await self._update_preview()
            
            self.ai_operation_status.text = '✅ Content enhanced successfully'
            ui.notification('Content enhanced successfully!', color='positive')
            
        except Exception as e:
            logger.error(f"Content enhancement failed: {e}")
            self.ai_operation_status.text = f'❌ Enhancement failed: {str(e)}'
            ui.notification(f'Content enhancement failed: {str(e)}', color='negative')
    
    async def _generate_featured_image(self):
        """Generate featured image with Replicate"""
        try:
            if not self.title_input.value:
                ui.notification('Please enter a title first', color='warning')
                return
            
            self.ai_operation_status.text = '🎨 Generating image with Flux Pro...'
            
            # Generate image
            result = await replicate_service.generate_featured_image(
                title=self.title_input.value,
                content_preview=self.content_textarea.value[:200] if self.content_textarea.value else None,
                style="professional"
            )
            
            # Store image URL in article attributes
            image_url = result['image_url']
            
            # Add image to content if not present
            if '![Featured Image]' not in self.content_textarea.value:
                image_markdown = f'![Featured Image]({image_url})\n\n'
                self.content_textarea.value = image_markdown + self.content_textarea.value
            
            # Update preview
            await self._update_preview()
            
            self.ai_operation_status.text = '✅ Image generated successfully'
            ui.notification('Featured image generated and added!', color='positive')
            
        except Exception as e:
            logger.error(f"Image generation failed: {e}")
            self.ai_operation_status.text = f'❌ Image generation failed: {str(e)}'
            ui.notification(f'Image generation failed: {str(e)}', color='negative')
    
    async def _save_article(self):
        """Save article to database"""
        try:
            if not self.title_input.value or not self.content_textarea.value:
                ui.notification('Title and content are required', color='warning')
                return
            
            # Prepare article attributes
            attributes = {
                'seo_title': self.seo_title_input.value,
                'seo_description': self.seo_description_input.value,
                'category': self.category_select.value,
                'tags': [tag.strip() for tag in self.tags_input.value.split(',') if tag.strip()],
                'updated_at': str(asyncio.get_event_loop().time())
            }
            
            if self.current_article_id:
                # Update existing article
                success = await self.article_ops.update_article(
                    article_id=self.current_article_id,
                    title=self.title_input.value,
                    content=self.content_textarea.value,
                    status=self.status_select.value,
                    attributes=attributes
                )
                
                if success:
                    ui.notification('Article updated successfully!', color='positive')
                else:
                    ui.notification('Failed to update article', color='negative')
            else:
                # Create new article
                article_id = await self.article_ops.create_article_with_search(
                    title=self.title_input.value,
                    content=self.content_textarea.value,
                    status=self.status_select.value,
                    attributes=attributes
                )
                
                self.current_article_id = article_id
                ui.notification('Article created successfully!', color='positive')
                
                # Update URL to edit mode
                ui.navigate.to(f'/admin/edit/{article_id}')
                
        except Exception as e:
            logger.error(f"Save operation failed: {e}")
            ui.notification(f'Save failed: {str(e)}', color='negative')
    
    async def _preview_article(self):
        """Open article preview in new tab"""
        try:
            if self.current_article_id:
                ui.navigate.to(f'/admin/view/{self.current_article_id}', new_tab=True)
            else:
                ui.notification('Please save the article first', color='warning')
                
        except Exception as e:
            logger.error(f"Preview failed: {e}")
            ui.notification(f'Preview failed: {str(e)}', color='negative')

# Global content editor instance
content_editor = ContentEditor()