"""
Claude AI content generation service
Following documented AI integration patterns
"""
import os
import asyncio
from typing import Dict, Any, Optional
import logging
from anthropic import Anthropic

logger = logging.getLogger(__name__)

class ClaudeService:
    """Claude AI service for content generation and enhancement"""
    
    def __init__(self):
        self.api_key = os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY environment variable is required")
        
        self.client = Anthropic(api_key=self.api_key)
        self.primary_model = os.getenv("CLAUDE_MODEL_PRIMARY", "claude-3-sonnet-20240229")
        self.fast_model = os.getenv("CLAUDE_MODEL_FAST", "claude-3-haiku-20240307")
        
        # Rate limiting semaphore - MANDATORY per guardrails
        self.operation_semaphore = asyncio.Semaphore(3)
    
    async def validate_service(self) -> bool:
        """Validate Claude API accessibility - MANDATORY per guardrails"""
        try:
            async with self.operation_semaphore:
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.fast_model,
                    max_tokens=10,
                    messages=[{"role": "user", "content": "Test"}]
                )
                return bool(response.content[0].text)
        except Exception as e:
            logger.error(f"Claude API validation failed: {e}")
            raise ValueError(f"Claude API validation failed: {e}")
    
    async def generate_article_content(
        self,
        topic: str,
        target_audience: str = "digital_nomads",
        word_count: int = 1000,
        additional_requirements: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate article content following PROVEN PATTERN from documentation
        """
        try:
            async with self.operation_semaphore:
                prompt = self._build_content_prompt(topic, target_audience, word_count, additional_requirements)
                
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.primary_model,
                    max_tokens=4000,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                content = response.content[0].text
                
                # Extract title from content (first H1 heading)
                title = self._extract_title_from_content(content)
                
                # Generate SEO description
                seo_description = await self._generate_seo_description(title, content)
                
                result = {
                    'title': title,
                    'content': content,
                    'seo_description': seo_description,
                    'word_count': len(content.split()),
                    'topic': topic,
                    'target_audience': target_audience,
                    'model_used': self.primary_model
                }
                
                logger.info(f"Generated article: {title} ({result['word_count']} words)")
                return result
                
        except Exception as e:
            logger.error(f"Content generation failed for topic '{topic}': {e}")
            raise ValueError(f"Content generation failed: {str(e)}")
    
    async def enhance_content(self, content: str, enhancement_type: str = "general") -> str:
        """Enhance existing content with AI"""
        try:
            async with self.operation_semaphore:
                enhancement_prompts = {
                    "general": "Enhance this article content to make it more engaging, informative, and well-structured. Maintain the core message but improve readability, flow, and impact.",
                    "seo": "Optimize this content for SEO while maintaining readability. Improve headers, add relevant keywords naturally, and enhance structure for search engines.",
                    "readability": "Improve the readability and clarity of this content. Make it more accessible to a broader audience while maintaining its informativeness.",
                    "engagement": "Make this content more engaging and compelling. Add storytelling elements, better examples, and more persuasive language."
                }
                
                prompt = f"{enhancement_prompts.get(enhancement_type, enhancement_prompts['general'])}\n\nContent to enhance:\n\n{content}"
                
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.primary_model,
                    max_tokens=4000,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                enhanced_content = response.content[0].text
                logger.info(f"Enhanced content using {enhancement_type} enhancement")
                return enhanced_content
                
        except Exception as e:
            logger.error(f"Content enhancement failed: {e}")
            raise ValueError(f"Content enhancement failed: {str(e)}")
    
    async def validate_content_quality(self, content: str) -> Dict[str, Any]:
        """
        Validate AI-generated content quality - MANDATORY per guardrails
        """
        try:
            # Basic validation
            word_count = len(content.split())
            if word_count < 500:
                raise ValueError("Content too short (minimum 500 words)")
            
            if content.count('\n#') < 2:
                raise ValueError("Content must have proper header structure")
            
            # AI quality validation
            async with self.operation_semaphore:
                prompt = f"""Rate this content quality 1-10 and identify any issues:
                
{content[:500]}...

Check for:
- Clarity and readability
- Factual accuracy concerns  
- Proper structure
- SEO optimization

Respond with: SCORE: X, ISSUES: [list]"""
                
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.fast_model,
                    max_tokens=500,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                response_text = response.content[0].text
                
                # Parse score
                score = 0
                issues = []
                
                if "SCORE: " in response_text:
                    try:
                        score = int(response_text.split("SCORE: ")[1].split(",")[0])
                    except (ValueError, IndexError):
                        score = 5  # Default neutral score
                
                if "ISSUES: " in response_text:
                    issues_text = response_text.split("ISSUES: ")[1]
                    issues = [issue.strip() for issue in issues_text.split(",") if issue.strip()]
                
                if score < 7:
                    raise ValueError(f"Content quality too low: {score}/10. Issues: {', '.join(issues)}")
                
                validation_result = {
                    'quality_score': score,
                    'word_count': word_count,
                    'issues': issues,
                    'passed': True
                }
                
                logger.info(f"Content validation passed with score {score}/10")
                return validation_result
                
        except ValueError as e:
            # Re-raise validation errors
            raise e
        except Exception as e:
            logger.error(f"Content validation failed: {e}")
            raise ValueError(f"Content validation failed: {str(e)}")
    
    async def generate_seo_metadata(self, title: str, content: str) -> Dict[str, str]:
        """Generate SEO title and description"""
        try:
            async with self.operation_semaphore:
                prompt = f"""Generate SEO metadata for this article:

Title: {title}
Content: {content[:800]}...

Generate:
1. SEO Title (60 characters max, compelling and keyword-rich)
2. Meta Description (155 characters max, compelling call-to-action)
3. Focus Keywords (3-5 primary keywords)

Format:
SEO_TITLE: [title]
META_DESCRIPTION: [description]
KEYWORDS: [keyword1, keyword2, keyword3]"""
                
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.fast_model,
                    max_tokens=300,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                response_text = response.content[0].text
                
                # Parse response
                seo_data = {}
                
                if "SEO_TITLE: " in response_text:
                    seo_data['seo_title'] = response_text.split("SEO_TITLE: ")[1].split("\n")[0].strip()
                
                if "META_DESCRIPTION: " in response_text:
                    seo_data['meta_description'] = response_text.split("META_DESCRIPTION: ")[1].split("\n")[0].strip()
                
                if "KEYWORDS: " in response_text:
                    keywords_text = response_text.split("KEYWORDS: ")[1].split("\n")[0].strip()
                    seo_data['keywords'] = [k.strip() for k in keywords_text.split(",")]
                
                return seo_data
                
        except Exception as e:
            logger.error(f"SEO metadata generation failed: {e}")
            return {'seo_title': title, 'meta_description': content[:155], 'keywords': []}
    
    def _build_content_prompt(
        self, 
        topic: str, 
        target_audience: str, 
        word_count: int, 
        additional_requirements: Optional[str]
    ) -> str:
        """Build content generation prompt"""
        prompt = f"""Write a comprehensive article for {target_audience} about: {topic}

Requirements:
- {word_count}-{word_count + 200} words
- Clear introduction, body with headers, conclusion
- SEO optimized with relevant keywords
- Engaging and informative tone
- Include practical examples and actionable advice
- Use markdown formatting for headers and structure
- Start with a compelling H1 title

Target audience: {target_audience}
"""
        
        if additional_requirements:
            prompt += f"\nAdditional requirements:\n{additional_requirements}"
        
        prompt += "\n\nWrite the complete article now:"
        
        return prompt
    
    def _extract_title_from_content(self, content: str) -> str:
        """Extract title from content (first H1 heading)"""
        lines = content.split('\n')
        for line in lines:
            if line.strip().startswith('# '):
                return line.strip()[2:].strip()
        
        # Fallback: use first line or generate from content
        first_line = lines[0].strip() if lines else "Untitled Article"
        return first_line.replace('#', '').strip()
    
    async def _generate_seo_description(self, title: str, content: str) -> str:
        """Generate SEO description for article"""
        try:
            async with self.operation_semaphore:
                prompt = f"""Write a compelling SEO meta description (150-155 characters) for this article:

Title: {title}
Content preview: {content[:300]}...

Make it compelling, include a call-to-action, and stay under 155 characters."""
                
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.fast_model,
                    max_tokens=100,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                description = response.content[0].text.strip()
                
                # Ensure it's under 155 characters
                if len(description) > 155:
                    description = description[:152] + "..."
                
                return description
                
        except Exception as e:
            logger.error(f"SEO description generation failed: {e}")
            # Fallback: create simple description from content
            words = content.split()[:25]
            fallback = " ".join(words)
            return fallback[:152] + "..." if len(fallback) > 152 else fallback

# Global Claude service instance
claude_service = ClaudeService()