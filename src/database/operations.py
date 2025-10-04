"""
Database operations for Quest-CMS following proven database-first patterns
"""
import json
import uuid
from typing import Optional, Dict, Any, List
from datetime import datetime
import logging

from .connection import db_manager

logger = logging.getLogger(__name__)

class ArticleOperations:
    """Article database operations following documented patterns"""
    
    @staticmethod
    async def create_article_with_search(
        title: str, 
        content: str, 
        attributes: Optional[Dict[str, Any]] = None,
        status: str = 'draft'
    ) -> str:
        """
        Create article with automatic search indexing and API availability
        Following PROVEN PATTERN from documentation
        """
        if attributes is None:
            attributes = {}
        
        try:
            article_id = await db_manager.execute_query("""
                INSERT INTO articles (
                    title, 
                    content, 
                    attributes,
                    status
                ) VALUES (
                    $1, $2, $3, $4
                )
                RETURNING id
            """, title, content, json.dumps(attributes), status)
            
            logger.info(f"Article created with ID: {article_id}")
            # Article immediately available via PostgREST API:
            # GET /articles?id=eq.{article_id}
            return str(article_id)
            
        except Exception as e:
            logger.error(f"Failed to create article: {e}")
            raise ValueError(f"Article creation failed: {str(e)}")
    
    @staticmethod
    async def get_article(article_id: str) -> Optional[Dict[str, Any]]:
        """Get article by ID"""
        try:
            result = await db_manager.execute_query("""
                SELECT 
                    id, title, content, status, attributes,
                    created_at, updated_at, published_at,
                    reviewed_by, review_notes,
                    ai_generated, ai_model, generation_prompt, quality_score
                FROM articles 
                WHERE id = $1
            """, uuid.UUID(article_id))
            
            if result:
                article = dict(result[0])
                # Parse JSON attributes
                if article['attributes']:
                    article['attributes'] = json.loads(article['attributes']) if isinstance(article['attributes'], str) else article['attributes']
                return article
            return None
            
        except Exception as e:
            logger.error(f"Failed to get article {article_id}: {e}")
            raise ValueError(f"Article retrieval failed: {str(e)}")
    
    @staticmethod
    async def search_articles_bm25(
        query: str, 
        limit: int = 20,
        status_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Full-text search with BM25 ranking
        Following PROVEN PATTERN from documentation
        """
        try:
            base_query = """
                SELECT 
                    id, title, content, status, attributes,
                    created_at, published_at,
                    ts_rank_cd(title_search || content_search, websearch_to_tsquery($1)) as rank,
                    ts_headline('english', content, websearch_to_tsquery($1), 'MaxWords=20') as snippet
                FROM articles
                WHERE 
                    title_search @@ websearch_to_tsquery($1) 
                    OR content_search @@ websearch_to_tsquery($1)
            """
            
            params = [query]
            
            if status_filter:
                base_query += " AND status = $2"
                params.append(status_filter)
                base_query += " ORDER BY rank DESC LIMIT $3"
                params.append(limit)
            else:
                base_query += " ORDER BY rank DESC LIMIT $2"
                params.append(limit)
            
            results = await db_manager.execute_query(base_query, *params)
            
            articles = []
            for row in results:
                article = dict(row)
                # Parse JSON attributes
                if article['attributes']:
                    article['attributes'] = json.loads(article['attributes']) if isinstance(article['attributes'], str) else article['attributes']
                articles.append(article)
            
            return articles
            
        except Exception as e:
            logger.error(f"Search failed for query '{query}': {e}")
            raise ValueError(f"Search operation failed: {str(e)}")
    
    @staticmethod
    async def list_articles(
        status: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """List articles with optional status filter"""
        try:
            if status:
                query = """
                    SELECT 
                        id, title, status, attributes,
                        created_at, updated_at, published_at,
                        ai_generated, quality_score
                    FROM articles 
                    WHERE status = $1
                    ORDER BY created_at DESC
                    LIMIT $2 OFFSET $3
                """
                params = [status, limit, offset]
            else:
                query = """
                    SELECT 
                        id, title, status, attributes,
                        created_at, updated_at, published_at,
                        ai_generated, quality_score
                    FROM articles 
                    ORDER BY created_at DESC
                    LIMIT $1 OFFSET $2
                """
                params = [limit, offset]
            
            results = await db_manager.execute_query(query, *params)
            
            articles = []
            for row in results:
                article = dict(row)
                # Parse JSON attributes
                if article['attributes']:
                    article['attributes'] = json.loads(article['attributes']) if isinstance(article['attributes'], str) else article['attributes']
                articles.append(article)
            
            return articles
            
        except Exception as e:
            logger.error(f"Failed to list articles: {e}")
            raise ValueError(f"Article listing failed: {str(e)}")
    
    @staticmethod
    async def update_article(
        article_id: str,
        title: Optional[str] = None,
        content: Optional[str] = None,
        status: Optional[str] = None,
        attributes: Optional[Dict[str, Any]] = None,
        reviewed_by: Optional[str] = None,
        review_notes: Optional[str] = None,
        quality_score: Optional[float] = None
    ) -> bool:
        """Update article with optional fields"""
        try:
            update_fields = []
            params = []
            param_count = 1
            
            if title is not None:
                update_fields.append(f"title = ${param_count}")
                params.append(title)
                param_count += 1
            
            if content is not None:
                update_fields.append(f"content = ${param_count}")
                params.append(content)
                param_count += 1
            
            if status is not None:
                update_fields.append(f"status = ${param_count}")
                params.append(status)
                param_count += 1
                
                # Set published_at when status becomes 'published'
                if status == 'published':
                    update_fields.append("published_at = NOW()")
            
            if attributes is not None:
                update_fields.append(f"attributes = ${param_count}")
                params.append(json.dumps(attributes))
                param_count += 1
            
            if reviewed_by is not None:
                update_fields.append(f"reviewed_by = ${param_count}")
                params.append(reviewed_by)
                param_count += 1
            
            if review_notes is not None:
                update_fields.append(f"review_notes = ${param_count}")
                params.append(review_notes)
                param_count += 1
            
            if quality_score is not None:
                update_fields.append(f"quality_score = ${param_count}")
                params.append(quality_score)
                param_count += 1
            
            if not update_fields:
                return False
            
            # Add article ID as last parameter
            params.append(uuid.UUID(article_id))
            
            query = f"""
                UPDATE articles 
                SET {', '.join(update_fields)}
                WHERE id = ${param_count}
                RETURNING id
            """
            
            result = await db_manager.execute_query(query, *params)
            return result is not None
            
        except Exception as e:
            logger.error(f"Failed to update article {article_id}: {e}")
            raise ValueError(f"Article update failed: {str(e)}")
    
    @staticmethod
    async def delete_article(article_id: str) -> bool:
        """Delete article by ID"""
        try:
            result = await db_manager.execute_query("""
                DELETE FROM articles 
                WHERE id = $1
                RETURNING id
            """, uuid.UUID(article_id))
            
            return result is not None
            
        except Exception as e:
            logger.error(f"Failed to delete article {article_id}: {e}")
            raise ValueError(f"Article deletion failed: {str(e)}")
    
    @staticmethod
    async def get_article_stats() -> Dict[str, int]:
        """Get article statistics for dashboard"""
        try:
            results = await db_manager.execute_query("""
                SELECT 
                    status,
                    COUNT(*) as count
                FROM articles 
                GROUP BY status
            """)
            
            stats = {
                'total': 0,
                'draft': 0,
                'review': 0,
                'published': 0,
                'archived': 0
            }
            
            for row in results:
                stats[row['status']] = row['count']
                stats['total'] += row['count']
            
            return stats
            
        except Exception as e:
            logger.error(f"Failed to get article stats: {e}")
            raise ValueError(f"Stats retrieval failed: {str(e)}")
    
    @staticmethod
    async def mark_ai_generated(
        article_id: str,
        ai_model: str,
        generation_prompt: str,
        quality_score: Optional[float] = None
    ) -> bool:
        """Mark article as AI-generated with metadata"""
        try:
            params = [True, ai_model, generation_prompt, uuid.UUID(article_id)]
            
            if quality_score is not None:
                query = """
                    UPDATE articles 
                    SET 
                        ai_generated = $1,
                        ai_model = $2,
                        generation_prompt = $3,
                        quality_score = $5
                    WHERE id = $4
                    RETURNING id
                """
                params.insert(4, quality_score)
            else:
                query = """
                    UPDATE articles 
                    SET 
                        ai_generated = $1,
                        ai_model = $2,
                        generation_prompt = $3
                    WHERE id = $4
                    RETURNING id
                """
            
            result = await db_manager.execute_query(query, *params)
            return result is not None
            
        except Exception as e:
            logger.error(f"Failed to mark article as AI-generated {article_id}: {e}")
            raise ValueError(f"AI metadata update failed: {str(e)}")