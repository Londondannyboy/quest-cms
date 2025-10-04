-- Quest-CMS Database Schema
-- Database-first architecture with full-text search and vector embeddings

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- Core content table with full-text search and vector embeddings
CREATE TABLE IF NOT EXISTS articles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'review', 'published', 'archived')),
    
    -- Flexible attributes (no migrations needed)
    attributes JSONB DEFAULT '{}',
    
    -- Full-text search with BM25 ranking
    title_search TSVECTOR GENERATED ALWAYS AS (to_tsvector('english', title)) STORED,
    content_search TSVECTOR GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
    
    -- AI embeddings for similarity and personalization
    content_embedding vector(1536),
    
    -- Audit and workflow tracking
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    published_at TIMESTAMPTZ,
    reviewed_by TEXT,
    review_notes TEXT,
    
    -- AI generation metadata
    ai_generated BOOLEAN DEFAULT false,
    ai_model TEXT,
    generation_prompt TEXT,
    quality_score DECIMAL(3,2)
);

-- Performance indexes
CREATE INDEX IF NOT EXISTS articles_search_idx ON articles USING GIN ((title_search || content_search));
CREATE INDEX IF NOT EXISTS articles_status_idx ON articles (status, created_at DESC);
CREATE INDEX IF NOT EXISTS articles_embedding_idx ON articles USING ivfflat (content_embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS articles_attributes_idx ON articles USING GIN (attributes);
CREATE INDEX IF NOT EXISTS articles_created_idx ON articles (created_at DESC);
CREATE INDEX IF NOT EXISTS articles_published_idx ON articles (published_at DESC) WHERE status = 'published';

-- Update trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_articles_updated_at 
    BEFORE UPDATE ON articles 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- Row Level Security (RLS) setup
ALTER TABLE articles ENABLE ROW LEVEL SECURITY;

-- Basic policy for authenticated users (can be enhanced with user roles)
CREATE POLICY articles_policy ON articles
    USING (true)
    WITH CHECK (true);

-- Function for full-text search with BM25 ranking
CREATE OR REPLACE FUNCTION search_articles_bm25(search_query TEXT, result_limit INTEGER DEFAULT 20)
RETURNS TABLE (
    id UUID,
    title TEXT,
    content TEXT,
    status TEXT,
    attributes JSONB,
    created_at TIMESTAMPTZ,
    published_at TIMESTAMPTZ,
    rank REAL,
    snippet TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.id,
        a.title,
        a.content,
        a.status,
        a.attributes,
        a.created_at,
        a.published_at,
        ts_rank_cd(a.title_search || a.content_search, websearch_to_tsquery(search_query)) as rank,
        ts_headline('english', a.content, websearch_to_tsquery(search_query), 'MaxWords=20') as snippet
    FROM articles a
    WHERE 
        a.title_search @@ websearch_to_tsquery(search_query) 
        OR a.content_search @@ websearch_to_tsquery(search_query)
    ORDER BY rank DESC
    LIMIT result_limit;
END;
$$ LANGUAGE plpgsql;

-- Function for similarity search using vector embeddings
CREATE OR REPLACE FUNCTION find_similar_articles(target_embedding vector(1536), similarity_threshold REAL DEFAULT 0.5, result_limit INTEGER DEFAULT 10)
RETURNS TABLE (
    id UUID,
    title TEXT,
    similarity REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.id,
        a.title,
        1 - (a.content_embedding <=> target_embedding) as similarity
    FROM articles a
    WHERE 
        a.content_embedding IS NOT NULL
        AND 1 - (a.content_embedding <=> target_embedding) > similarity_threshold
    ORDER BY similarity DESC
    LIMIT result_limit;
END;
$$ LANGUAGE plpgsql;