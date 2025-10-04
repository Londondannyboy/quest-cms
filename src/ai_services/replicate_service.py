"""
Replicate image generation service for Quest-CMS
Using Flux Pro 1.1 for high-quality image generation
"""
import os
import asyncio
from typing import Dict, Any, Optional, List
import logging
import replicate

logger = logging.getLogger(__name__)

class ReplicateService:
    """Replicate service for AI image generation"""
    
    def __init__(self):
        self.api_token = os.getenv("REPLICATE_API_TOKEN")
        if not self.api_token:
            raise ValueError("REPLICATE_API_TOKEN environment variable is required")
        
        # Set API token for replicate client
        replicate.Client(api_token=self.api_token)
        
        self.primary_model = os.getenv("REPLICATE_MODEL_PRIMARY", "black-forest-labs/flux-1.1-pro")
        self.dev_model = os.getenv("REPLICATE_MODEL_DEV", "black-forest-labs/flux-dev")
        
        # Rate limiting semaphore - MANDATORY per guardrails
        self.operation_semaphore = asyncio.Semaphore(2)
    
    async def validate_service(self) -> bool:
        """Validate Replicate API accessibility - MANDATORY per guardrails"""
        try:
            # Simple ping test
            await asyncio.to_thread(replicate.ping)
            return True
        except Exception as e:
            logger.error(f"Replicate API validation failed: {e}")
            raise ValueError(f"Replicate API validation failed: {e}")
    
    async def generate_featured_image(
        self,
        title: str,
        content_preview: Optional[str] = None,
        style: str = "professional",
        aspect_ratio: str = "16:9",
        use_pro_model: bool = True
    ) -> Dict[str, Any]:
        """
        Generate featured image for article using Flux Pro 1.1
        Following documented image generation patterns
        """
        try:
            async with self.operation_semaphore:
                # Build prompt for image generation
                prompt = self._build_image_prompt(title, content_preview, style)
                
                model = self.primary_model if use_pro_model else self.dev_model
                
                # Generate image
                output = await asyncio.to_thread(
                    replicate.run,
                    model,
                    input={
                        "prompt": prompt,
                        "aspect_ratio": aspect_ratio,
                        "output_quality": 95,
                        "safety_tolerance": 2,
                        "prompt_upsampling": True
                    }
                )
                
                image_url = output[0] if isinstance(output, list) else output
                
                result = {
                    'image_url': image_url,
                    'prompt': prompt,
                    'model_used': model,
                    'aspect_ratio': aspect_ratio,
                    'style': style,
                    'title': title
                }
                
                logger.info(f"Generated featured image for: {title}")
                return result
                
        except Exception as e:
            logger.error(f"Image generation failed for title '{title}': {e}")
            raise ValueError(f"Image generation failed: {str(e)}")
    
    async def generate_social_media_variants(
        self,
        original_prompt: str,
        title: str
    ) -> Dict[str, str]:
        """Generate social media image variants"""
        try:
            variants = {}
            
            # Common social media aspect ratios
            social_formats = {
                "instagram_square": "1:1",
                "facebook_post": "16:9", 
                "twitter_post": "16:9",
                "linkedin_post": "1.91:1",
                "instagram_story": "9:16"
            }
            
            tasks = []
            for format_name, aspect_ratio in social_formats.items():
                task = self._generate_variant(original_prompt, aspect_ratio, format_name)
                tasks.append(task)
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, (format_name, aspect_ratio) in enumerate(social_formats.items()):
                result = results[i]
                if not isinstance(result, Exception):
                    variants[format_name] = result
                else:
                    logger.error(f"Failed to generate {format_name} variant: {result}")
                    variants[format_name] = None
            
            return variants
            
        except Exception as e:
            logger.error(f"Social media variants generation failed: {e}")
            raise ValueError(f"Social media variants generation failed: {str(e)}")
    
    async def _generate_variant(self, prompt: str, aspect_ratio: str, format_name: str) -> str:
        """Generate single image variant"""
        async with self.operation_semaphore:
            output = await asyncio.to_thread(
                replicate.run,
                self.dev_model,  # Use dev model for variants to save costs
                input={
                    "prompt": f"{prompt} optimized for {format_name}",
                    "aspect_ratio": aspect_ratio,
                    "output_quality": 90,
                    "safety_tolerance": 2
                }
            )
            
            return output[0] if isinstance(output, list) else output
    
    async def generate_bulk_images(
        self,
        image_requests: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Generate multiple images in parallel for MCP integration
        Following bulk generation pattern from documentation
        """
        try:
            tasks = []
            for request in image_requests:
                task = self.generate_featured_image(
                    title=request.get('title', ''),
                    content_preview=request.get('content_preview'),
                    style=request.get('style', 'professional'),
                    aspect_ratio=request.get('aspect_ratio', '16:9'),
                    use_pro_model=request.get('use_pro_model', False)  # Use dev for bulk
                )
                tasks.append(task)
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Separate successful from failed generations
            successful = []
            failed = []
            
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    failed.append({
                        'request': image_requests[i],
                        'error': str(result)
                    })
                else:
                    successful.append(result)
            
            bulk_result = {
                'generated_count': len(successful),
                'failed_count': len(failed),
                'images': successful,
                'errors': failed
            }
            
            logger.info(f"Bulk image generation: {len(successful)} successful, {len(failed)} failed")
            return bulk_result
            
        except Exception as e:
            logger.error(f"Bulk image generation failed: {e}")
            raise ValueError(f"Bulk image generation failed: {str(e)}")
    
    async def optimize_image_prompt(self, basic_prompt: str) -> str:
        """Optimize image prompt for better results"""
        try:
            # Add quality and style modifiers
            quality_modifiers = [
                "high quality",
                "professional photography",
                "sharp focus",
                "clean composition",
                "modern design"
            ]
            
            negative_modifiers = [
                "no text",
                "no watermarks", 
                "no low quality",
                "no blurry",
                "no distorted"
            ]
            
            optimized_prompt = f"{basic_prompt}, {', '.join(quality_modifiers)}"
            
            return optimized_prompt
            
        except Exception as e:
            logger.error(f"Prompt optimization failed: {e}")
            return basic_prompt
    
    def _build_image_prompt(
        self,
        title: str,
        content_preview: Optional[str] = None,
        style: str = "professional"
    ) -> str:
        """Build optimized prompt for image generation"""
        
        # Style templates
        style_templates = {
            "professional": "Professional, clean, modern business-style",
            "minimalist": "Minimalist design, clean lines, simple composition",
            "vibrant": "Vibrant colors, energetic, eye-catching design",
            "elegant": "Elegant, sophisticated, high-end aesthetic",
            "tech": "Modern technology theme, digital, futuristic",
            "travel": "Travel and lifestyle, scenic, inspirational",
            "business": "Corporate, professional, business-focused"
        }
        
        base_style = style_templates.get(style, style_templates["professional"])
        
        # Extract key concepts from title
        title_words = title.lower().split()
        key_concepts = []
        
        # Common topic keywords for image generation
        topic_keywords = {
            "nomad": "digital nomad, remote work, laptop lifestyle",
            "travel": "travel, destination, adventure",
            "business": "business, entrepreneurship, success",
            "tech": "technology, innovation, digital",
            "lifestyle": "lifestyle, modern living, wellness",
            "finance": "finance, money, investment",
            "guide": "education, learning, knowledge"
        }
        
        for word in title_words:
            for keyword, concepts in topic_keywords.items():
                if keyword in word:
                    key_concepts.append(concepts)
                    break
        
        # Build final prompt
        prompt_parts = [
            f"Featured image for article: {title}",
            base_style,
            "high quality, professional photography",
            "clean composition, sharp focus"
        ]
        
        if key_concepts:
            prompt_parts.extend(key_concepts[:2])  # Limit to avoid prompt overflow
        
        if content_preview:
            # Extract additional context from content preview
            content_words = content_preview.lower().split()[:20]
            relevant_context = " ".join(content_words)
            if len(relevant_context) < 100:
                prompt_parts.append(f"Context: {relevant_context}")
        
        prompt = ", ".join(prompt_parts)
        
        # Ensure prompt isn't too long
        if len(prompt) > 400:
            prompt = prompt[:397] + "..."
        
        return prompt

# Global Replicate service instance
replicate_service = ReplicateService()