# Python Project Cookiecutter

## Stack (The core technology choices for development)
- Python 3.11+
- uv
- FastAPI
- Pydantic Settings (Strict typed configuration)
- pytest
- ruff
- mypy (pragmatic)
- pre-commit (Git hooks for quality gates)

## Structure (The standardized file and directory organization)

```text
project_root/
├── pyproject.toml      # Project metadata, dependencies, and tool config
├── README.md           # Documentation for humans
├── .env.example        # Template for environment variables (Explicit > Implicit)
├── src/{package_name}/ # Main source code container
│   ├── __main__.py     # Entry point for running as a module (python -m)
│   ├── app.py          # FastAPI application factory (Lifecycle management)
│   ├── main.py         # Primary entry point or CLI runner
│   ├── settings.py     # Typed configuration (Pydantic Settings)
│   ├── logging.py      # Structured logging (JSON prod, Console dev)
│   ├── errors.py       # Global exception handlers (Fail gracefully)
│   ├── api/            # API route handlers
│   │   └── health.py   # Standard health check endpoint
│   ├── models/         # Data schemas and Pydantic models
│   ├── services/       # Business logic (isolated from transport)
│   └── rag/            # RAG-specific logic (if applicable)
├── tests/              # Test suite (pytest)
└── .ai/                # AI context, prompts, and local LLM data
```

## Rules (Mandatory constraints & Philosophy)
- **Layout**: `src/` layout only.
- **Dependency Manager**: `uv` only (do not use conda).
- **Scope**: No Docker / DB / auth unless explicitly requested.
- **Config**: Use `pydantic-settings` for all environment variables.
- **Zen**: Flat is better than nested. Avoid deep package hierarchies.
- **Zen**: Explicit is better than implicit. Type everything at the boundary.
- **Production**: Structured logging and Health checks are mandatory.
