# Project Structure

This document outlines the organization of the Conversational AI Assistant project.

## Directory Structure

```
Conversational AI Assistant/
├── app/                          # Main application package
│   ├── __init__.py
│   ├── main.py                  # FastAPI application entry point
│   │
│   ├── api/                     # API layer - HTTP endpoints
│   │   ├── __init__.py
│   │   ├── routes.py            # API route definitions
│   │   └── models.py            # API request/response models
│   │
│   ├── config/                  # Configuration management
│   │   ├── __init__.py
│   │   ├── settings.py          # Application settings
│   │   └── constants.py         # Application constants
│   │
│   ├── core/                    # Core orchestration logic
│   │   ├── __init__.py
│   │   ├── orchestrator.py      # Main orchestration handler
│   │   ├── router.py            # Request routing logic
│   │   └── decision.py          # Decision-making logic
│   │
│   ├── schemas/                  # Pydantic data models (all schemas consolidated here)
│   │   ├── __init__.py
│   │   ├── agentic.py           # Agentic reasoning schemas
│   │   ├── understanding.py     # Understanding engine schemas
│   │   ├── response.py          # Response schemas
│   │   └── state.py             # State management schemas
│   │
│   ├── agentic/                 # Agentic reasoning components
│   │   ├── __init__.py
│   │   ├── planner.py           # Task planning
│   │   ├── executor.py          # Task execution
│   │   ├── verifier.py          # Answer verification
│   │   ├── global_document.py   # Global document processing
│   │   └── prompt.py            # Agentic prompts
│   │
│   ├── understanding/           # User intent understanding
│   │   ├── __init__.py
│   │   ├── engine.py            # Understanding engine
│   │   └── prompt.py            # Understanding prompts
│   │
│   ├── conversation/            # Conversation management
│   │   ├── __init__.py
│   │   ├── responder.py         # Response generation
│   │   └── prompt.py            # Conversation prompts
│   │
│   ├── memory/                  # Conversation memory management
│   │   ├── __init__.py
│   │   ├── manager.py           # Memory management logic
│   │   ├── store.py             # Memory storage
│   │   ├── session.py           # Session memory models
│   │   └── summarizer.py        # Memory summarization
│   │
│   ├── documents/               # Document processing and storage
│   │   ├── __init__.py
│   │   ├── store.py             # Document storage
│   │   ├── session.py           # Document session models
│   │   ├── chunker.py           # Text chunking
│   │   ├── summarize_chunk.py   # Chunk summarization
│   │   └── summarize_final.py   # Final document summarization
│   │
│   ├── ingestion/               # Document ingestion pipeline
│   │   ├── __init__.py
│   │   ├── router.py            # Ingestion routing
│   │   ├── models.py            # Ingestion models
│   │   ├── pdf.py               # PDF processing
│   │   ├── audio.py             # Audio processing
│   │   └── docling_extractor.py # Docling extraction
│   │
│   ├── tools/                   # External tool integrations
│   │   ├── __init__.py
│   │   ├── llm.py               # LLM tool wrapper
│   │   ├── retrieval.py         # Retrieval tool
│   │   ├── search.py            # Search tool
│   │   ├── code.py              # Code execution tool
│   │   └── summarizer.py        # Summarization tool
│   │
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       ├── logging.py           # Logging utilities
│       ├── token_counter.py     # Token counting
│       ├── helper.py            # Helper functions
│       └── guards.py            # Guard functions
│
├── tests/                       # Test suite
│   ├── test_api.py
│   ├── test_conversation.py
│   ├── test_router.py
│   └── test_understanding.py
│
├── venv/                        # Virtual environment (gitignored)
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── PROJECT_STRUCTURE.md         # This file
```

## Module Organization Principles

### 1. **Layered Architecture**
- **API Layer** (`api/`): HTTP endpoints and request/response handling
- **Core Layer** (`core/`): Business logic orchestration
- **Domain Layers**: Feature-specific modules (agentic, understanding, conversation, etc.)

### 2. **Schema Consolidation**
All Pydantic models are centralized in `schemas/`:
- `schemas/agentic.py` - Agentic reasoning models
- `schemas/understanding.py` - Understanding engine models
- `schemas/response.py` - API response models
- `schemas/state.py` - State management models

### 3. **Separation of Concerns**
- **Memory** (`memory/`): Conversation history and session management
- **Documents** (`documents/`): Document storage and processing
- **Ingestion** (`ingestion/`): Document ingestion pipeline
- **Tools** (`tools/`): External service integrations

### 4. **Clear Naming Conventions**
- Each module has a clear, single responsibility
- Related files are grouped in the same directory
- `__init__.py` files ensure proper Python package structure

## Key Improvements Made

1. ✅ **Added missing `__init__.py`** to `documents/` directory
2. ✅ **Consolidated schemas** - Moved `agentic/schemas.py` → `schemas/agentic.py`
3. ✅ **Updated imports** - All references now point to the new schema location
4. ✅ **Consistent structure** - All modules follow the same organizational pattern

## Import Patterns

### Recommended Import Style
```python
# Schemas
from app.schemas.agentic import ReasoningTask
from app.schemas.understanding import Understanding

# Core modules
from app.core.orchestrator import Orchestrator
from app.memory.store import get_session

# Tools
from app.tools.llm import call_llm
```

## Future Considerations

If the project grows, consider:
- Creating a `services/` layer for complex business logic
- Separating `models/` from `schemas/` if database models are needed
- Adding a `middleware/` directory for cross-cutting concerns
- Creating a `repositories/` layer if database access becomes complex

