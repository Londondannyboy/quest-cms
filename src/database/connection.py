"""
Database connection and pool management for Quest-CMS
Following documented database-first pattern with Neon PostgreSQL
"""
import asyncpg
import os
import json
from typing import Optional, Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Database manager with connection pooling and health checks"""
    
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None
        self.connection_string = os.getenv("NEON_CONNECTION_STRING")
        
        if not self.connection_string:
            raise ValueError("NEON_CONNECTION_STRING environment variable is required")
    
    async def initialize(self):
        """Initialize database connection pool"""
        try:
            self.pool = await asyncpg.create_pool(
                self.connection_string,
                min_size=1,
                max_size=5,
                command_timeout=30
            )
            
            # Validate connection and schema
            await self.validate_database_health()
            logger.info("Database connection pool initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise ValueError(f"Database initialization failed: {e}")
    
    async def close(self):
        """Close database connection pool"""
        if self.pool:
            await self.pool.close()
            logger.info("Database connection pool closed")
    
    async def validate_database_health(self):
        """Validate database connectivity and schema - MANDATORY per guardrails"""
        try:
            async with self.pool.acquire() as conn:
                # Verify schema exists
                schema_check = await conn.fetchval("""
                    SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables 
                        WHERE table_name = 'articles'
                    )
                """)
                
                if not schema_check:
                    raise ValueError("Articles table does not exist - run database_schema.sql")
                
                # Verify search index exists
                index_check = await conn.fetchval("""
                    SELECT EXISTS (
                        SELECT 1 FROM pg_indexes 
                        WHERE indexname = 'articles_search_idx'
                    )
                """)
                
                if not index_check:
                    raise ValueError("Search index missing - run schema migration")
                
                logger.info("Database health check passed")
                return True
                
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            raise ValueError(f"Database health check failed: {e}")
    
    async def execute_query(self, query: str, *args) -> Any:
        """Execute database query with connection pooling - MANDATORY pattern"""
        async with self.pool.acquire() as conn:
            try:
                if query.strip().upper().startswith('SELECT'):
                    return await conn.fetch(query, *args)
                else:
                    return await conn.fetchval(query, *args)
            except Exception as e:
                logger.error(f"Database operation failed: {e}")
                raise ValueError(f"Database operation failed: {str(e)}")
    
    async def execute_transaction(self, queries: List[tuple]) -> List[Any]:
        """Execute multiple queries in a transaction"""
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                results = []
                for query, args in queries:
                    try:
                        if query.strip().upper().startswith('SELECT'):
                            result = await conn.fetch(query, *args)
                        else:
                            result = await conn.fetchval(query, *args)
                        results.append(result)
                    except Exception as e:
                        logger.error(f"Transaction query failed: {e}")
                        raise ValueError(f"Transaction failed: {str(e)}")
                return results

# Global database manager instance
db_manager = DatabaseManager()