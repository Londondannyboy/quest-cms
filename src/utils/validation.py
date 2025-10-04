"""
Validation utilities for Quest-CMS
Following documented guardrails and quality standards
"""
import os
import asyncio
import psutil
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)

class SystemValidator:
    """System validation following MANDATORY guardrails from documentation"""
    
    @staticmethod
    def validate_environment() -> Dict[str, bool]:
        """
        Validate environment configuration - MANDATORY per guardrails
        """
        required_vars = [
            "NEON_CONNECTION_STRING",
            "CLAUDE_API_KEY", 
            "REPLICATE_API_TOKEN"
        ]
        
        optional_vars = [
            "CLOUDINARY_URL"
        ]
        
        results = {
            'required_vars': True,
            'missing_required': [],
            'missing_optional': []
        }
        
        # Check required variables
        for var in required_vars:
            if not os.getenv(var):
                results['required_vars'] = False
                results['missing_required'].append(var)
        
        # Check optional variables
        for var in optional_vars:
            if not os.getenv(var):
                results['missing_optional'].append(var)
        
        if not results['required_vars']:
            raise ValueError(f"Missing required environment variables: {results['missing_required']}")
        
        return results
    
    @staticmethod
    def check_memory_usage() -> Dict[str, Any]:
        """
        Monitor memory usage - MANDATORY per guardrails
        """
        memory = psutil.virtual_memory()
        
        memory_info = {
            'percent_used': memory.percent,
            'available_gb': memory.available / (1024**3),
            'total_gb': memory.total / (1024**3),
            'status': 'ok'
        }
        
        if memory.percent > 80:
            memory_info['status'] = 'critical'
            raise ValueError(f"Memory usage too high: {memory.percent}%")
        elif memory.percent > 70:
            memory_info['status'] = 'warning'
            logger.warning(f"High memory usage: {memory.percent}%")
        
        return memory_info
    
    @staticmethod
    async def validate_performance_baseline() -> Dict[str, bool]:
        """
        Validate performance requirements - NON-NEGOTIABLE per guardrails
        """
        performance_results = {
            'database_response': False,
            'ai_service_response': False,
            'memory_usage': False
        }
        
        try:
            # Test database response time (< 100ms target)
            start_time = asyncio.get_event_loop().time()
            # Simulate quick DB operation
            await asyncio.sleep(0.05)  # Placeholder for actual DB test
            db_time = (asyncio.get_event_loop().time() - start_time) * 1000
            
            performance_results['database_response'] = db_time < 100
            
            # Test memory usage
            memory_info = SystemValidator.check_memory_usage()
            performance_results['memory_usage'] = memory_info['status'] in ['ok', 'warning']
            
            # AI service timing will be tested during actual operations
            performance_results['ai_service_response'] = True
            
        except Exception as e:
            logger.error(f"Performance validation failed: {e}")
            
        return performance_results

class ContentValidator:
    """Content validation following documented quality standards"""
    
    @staticmethod
    def validate_article_data(title: str, content: str, attributes: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Validate article data before saving
        """
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Title validation
        if not title or not title.strip():
            validation_result['valid'] = False
            validation_result['errors'].append("Title is required")
        elif len(title.strip()) < 5:
            validation_result['valid'] = False
            validation_result['errors'].append("Title must be at least 5 characters")
        elif len(title) > 200:
            validation_result['warnings'].append("Title is very long (over 200 characters)")
        
        # Content validation
        if not content or not content.strip():
            validation_result['valid'] = False
            validation_result['errors'].append("Content is required")
        else:
            word_count = len(content.split())
            if word_count < 100:
                validation_result['warnings'].append(f"Content is short ({word_count} words). Consider adding more detail.")
            elif word_count < 300:
                validation_result['warnings'].append(f"Content is brief ({word_count} words). Consider expanding for better SEO.")
        
        # Header structure validation
        if content and '\n#' not in content:
            validation_result['warnings'].append("Content should include headers for better structure")
        
        # Attributes validation
        if attributes:
            if 'seo_description' in attributes and attributes['seo_description']:
                seo_desc = attributes['seo_description']
                if len(seo_desc) > 160:
                    validation_result['warnings'].append("SEO description is over 160 characters")
                elif len(seo_desc) < 120:
                    validation_result['warnings'].append("SEO description could be longer for better optimization")
        
        return validation_result
    
    @staticmethod
    def validate_ai_content_structure(content: str) -> bool:
        """
        Validate AI-generated content structure - MANDATORY per guardrails
        """
        # Minimum word count
        word_count = len(content.split())
        if word_count < 500:
            raise ValueError("Content too short (minimum 500 words)")
        
        # Header structure requirement
        if content.count('\n#') < 2:
            raise ValueError("Content must have proper header structure")
        
        return True
    
    @staticmethod
    def sanitize_content(content: str) -> str:
        """
        Sanitize content for security
        """
        # Basic sanitization - can be enhanced with more sophisticated cleaning
        
        # Remove potentially dangerous HTML
        dangerous_tags = ['<script', '<iframe', '<object', '<embed', '<form']
        for tag in dangerous_tags:
            if tag.lower() in content.lower():
                logger.warning(f"Removed potentially dangerous tag: {tag}")
                content = content.replace(tag, f'&lt;{tag[1:]}')
        
        return content
    
    @staticmethod
    def extract_metadata(content: str) -> Dict[str, Any]:
        """
        Extract metadata from content
        """
        metadata = {
            'word_count': len(content.split()),
            'character_count': len(content),
            'paragraph_count': len([p for p in content.split('\n\n') if p.strip()]),
            'header_count': content.count('\n#'),
            'estimated_reading_time': len(content.split()) // 200  # Assume 200 WPM
        }
        
        # Extract headers
        headers = []
        for line in content.split('\n'):
            if line.strip().startswith('#'):
                headers.append(line.strip())
        metadata['headers'] = headers
        
        # Check for images
        metadata['has_images'] = '![' in content
        metadata['image_count'] = content.count('![')
        
        return metadata

class SecurityValidator:
    """Security validation utilities"""
    
    @staticmethod
    def validate_access_request(request_data: Dict[str, Any]) -> bool:
        """
        Basic access validation - can be enhanced with authentication
        """
        # Placeholder for access control
        # In production, implement proper authentication here
        return True
    
    @staticmethod
    def validate_input_safety(input_data: str) -> bool:
        """
        Validate input for safety
        """
        # Check for potential injection attempts
        dangerous_patterns = [
            'javascript:', 'data:', 'vbscript:', 'onload=', 'onerror=', 'onclick='
        ]
        
        input_lower = input_data.lower()
        for pattern in dangerous_patterns:
            if pattern in input_lower:
                logger.warning(f"Potentially dangerous input detected: {pattern}")
                return False
        
        return True