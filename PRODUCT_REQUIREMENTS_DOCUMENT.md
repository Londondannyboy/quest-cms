# Quest-CMS Product Requirements Document (PRD)

## 📋 Document Overview

**Project**: Quest-CMS  
**Version**: 1.0  
**Status**: Implementation Complete, Production Deployment Pending  
**Framework**: Archon Methodology - G3 Framework (Guideline, Guidance, Guardrails)  
**Last Updated**: 2025-10-04  

## 🎯 Guideline: Shared AI-Human Understanding

### Project Context
Quest-CMS is the centralized content management system for the Quest ecosystem, designed to leverage AI-assisted content creation with human review workflows. It serves as the content hub for multiple Quest ecosystem sites including relocation_quest, rainmaker_quest, and future verticals.

### Technical Rationale
- **Framework Choice**: NiceGUI selected for rapid development and real-time features
- **Database**: Neon PostgreSQL for scalability and full-text search capabilities
- **AI Integration**: Claude for text generation, Flux Pro for image generation
- **Deployment**: Railway for seamless GitHub integration and auto-deployment

### Architectural Decisions
- Database-first architecture ensuring data integrity
- Progressive Web App design for cross-platform compatibility
- RESTful API design for ecosystem integration
- Environment-based configuration for deployment flexibility

### Business Requirements
- **Performance**: Sub-2-second response times for all operations
- **Quality**: AI-generated content requires minimal human editing
- **Scalability**: Support for multiple Quest ecosystem verticals
- **Reliability**: 99.9% uptime for production deployment

## 🛠️ Guidance: Methodology for Evolving Prompts

### Proven Implementation Patterns

#### 1. NiceGUI Application Structure
```python
# Proven pattern for NiceGUI 3.0 compatibility
from nicegui import ui, run
import asyncio

class QuestCMS:
    def __init__(self):
        self.setup_database()
        self.setup_ui()
    
    def setup_ui(self):
        # Use ui.splitter() with add_slot() method (NiceGUI 3.0)
        with ui.splitter() as splitter:
            with splitter.add_slot():
                # Navigation content
                pass
            with splitter.add_slot():
                # Main content area
                pass
```

#### 2. Database Connection Pattern
```python
# Proven Neon PostgreSQL connection pattern
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db_connection():
    return psycopg2.connect(
        os.getenv('NEON_CONNECTION_STRING'),
        cursor_factory=RealDictCursor
    )
```

#### 3. AI Service Integration Pattern
```python
# Proven Claude API integration
import anthropic

class AIContentGenerator:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv('CLAUDE_API_KEY')
        )
    
    async def generate_content(self, prompt, category):
        response = await self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
```

### Implementation Templates

#### Database Schema Template
```sql
-- Core content management schema
CREATE TABLE content_items (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    category VARCHAR(100),
    status VARCHAR(50) DEFAULT 'draft',
    ai_generated BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_content_status ON content_items(status);
CREATE INDEX idx_content_category ON content_items(category);
```

#### API Endpoint Template
```python
# RESTful API endpoint pattern
@ui.page('/api/content')
async def content_api():
    if request.method == 'GET':
        return await get_all_content()
    elif request.method == 'POST':
        return await create_content(request.json)
```

### Best Practices

#### 1. Error Handling
- Always use try-catch blocks for database operations
- Implement proper logging for debugging
- Provide user-friendly error messages in UI

#### 2. Security
- Environment variables for all sensitive credentials
- Input validation for all user-provided data
- Secure database connections with SSL

#### 3. Performance
- Database connection pooling for high traffic
- Async operations for AI service calls
- Pagination for large content lists

### Anti-Patterns (What NOT to Do)

#### ❌ NiceGUI 2.x Splitter API
```python
# DON'T USE - Deprecated in NiceGUI 3.0
with ui.splitter() as splitter:
    splitter.before = content  # This will fail
```

#### ❌ Synchronous AI Calls
```python
# DON'T USE - Blocks UI thread
def generate_content(prompt):
    response = client.messages.create(...)  # Blocking call
    return response
```

#### ❌ Hardcoded Credentials
```python
# DON'T USE - Security vulnerability
CLAUDE_API_KEY = "sk-ant-api03-..."  # Never hardcode
```

## 🛡️ Guardrails: AI-Assisted Quality Checkpoints

### Pre-Implementation Validation

#### 1. Environment Setup Verification
```bash
# Required environment variables must be set
echo $NEON_CONNECTION_STRING
echo $CLAUDE_API_KEY
echo $REPLICATE_API_TOKEN
```

#### 2. Database Connectivity Check
```python
# Database connection must succeed
try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("✅ Database connection successful")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
```

#### 3. AI Service Health Check
```python
# AI services must be accessible
try:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=10,
        messages=[{"role": "user", "content": "test"}]
    )
    print("✅ Claude API accessible")
except Exception as e:
    print(f"❌ Claude API failed: {e}")
```

### Service Health Checks

#### 1. Database Performance
- Query response time < 500ms for content retrieval
- Connection pool utilization < 80%
- No database connection leaks

#### 2. AI Service Performance
- Claude API response time < 10 seconds
- Replicate API response time < 30 seconds
- Error rate < 5% for AI generations

#### 3. Application Performance
- Page load time < 2 seconds
- Memory usage < 512MB
- No memory leaks in long-running sessions

### Code Quality Standards

#### 1. Code Structure
- ✅ Modular component design
- ✅ Clear separation of concerns
- ✅ Consistent naming conventions
- ✅ Comprehensive error handling

#### 2. Documentation
- ✅ All functions have docstrings
- ✅ API endpoints documented
- ✅ Database schema documented
- ✅ Deployment instructions clear

#### 3. Testing
- ✅ Manual testing of all CRUD operations
- ✅ AI service integration testing
- ✅ Database operation testing
- ✅ UI responsiveness testing

### Performance Requirements (Non-Negotiable)

#### 1. Response Time Targets
- **Content List**: < 1 second
- **Content Detail**: < 500ms
- **Content Creation**: < 2 seconds
- **AI Generation**: < 30 seconds

#### 2. Availability Targets
- **Uptime**: 99.9% (8.76 hours downtime/year max)
- **Database**: 99.95% availability
- **AI Services**: 95% availability (external dependency)

#### 3. Scalability Targets
- **Concurrent Users**: 100+ simultaneous users
- **Content Volume**: 10,000+ content items
- **Database**: 1M+ records capacity

## 🚀 Implementation Status

### ✅ Completed Components
1. **Core Application**: NiceGUI-based admin interface
2. **Database Integration**: Neon PostgreSQL with optimized schema
3. **AI Services**: Claude and Flux Pro integration
4. **CRUD Operations**: Complete content management workflow
5. **Real-time Features**: Live markdown preview and WebSocket updates
6. **Code Quality**: Clean, documented, maintainable codebase

### 🔄 Pending Components
1. **Production Deployment**: Railway GitHub auto-deployment connection
2. **Environment Configuration**: Production environment variables setup
3. **Live Testing**: End-to-end production testing
4. **Performance Validation**: Production performance benchmarking

### 📋 Success Validation Checklist

#### Technical Success Criteria
- [ ] Railway auto-deployment working from GitHub pushes
- [ ] Production environment variables configured
- [ ] Live admin interface accessible at production URL
- [ ] All CRUD operations working in production
- [ ] AI content generation functional in production
- [ ] Database operations performing within targets

#### Business Success Criteria
- [ ] Admin interface usable by non-technical users
- [ ] Content creation workflow efficient and intuitive
- [ ] AI-generated content quality meets standards
- [ ] Performance targets met under normal load

#### AI Collaboration Success Criteria
- [ ] PRD successfully guided implementation
- [ ] All guardrails passing consistently
- [ ] Implementation matches specified patterns
- [ ] Code quality standards maintained throughout

---

**Implementation Authority**: Archon Methodology AI-Human Collaboration  
**Quality Assurance**: G3 Framework Validation  
**Next Milestone**: Production Deployment Completion