# AI & Development Guidelines

This repository serves as a central knowledge base for coding standards, best practices, and project templates. It is designed to ensure consistency, quality, and strict adherence to "Zen of Python" principles across all projects.

## 🚀 Workflow: How to use this repo

Follow these steps to ship high-quality code using these guidelines:

1.  **Scaffold**: Start your project using the standard template.
    ```bash
    # Requires cookiecutter (uv tool install cookiecutter)
    cookiecutter https://github.com/lilidl-nft/AI --directory templates/python-starter
    ```
2.  **Contextualize AI**: Copy `guides/gemini_rules.md` to your project root (e.g., as `.cursorrules` or `gemini_rules.md`) so your AI assistant knows the rules.
3.  **Configure**: Set up your environment using `.env.example` as a template. Enforce configuration via `pydantic-settings`.
4.  **Implement**: Write code following strict [Python Best Practices](guides/python_best_practices.md) and [API Rules](guides/api_rules.md).
5.  **Verify**: Run the quality gates before committing.
    ```bash
    uv run pytest
    uv run ruff check
    uv run mypy .
    ```
6.  **Review**: Check your work against the [Definition of Done](guides/testing_and_dod.md) checklist.
7.  **Architect**: If building RAG or MCP systems, consult the [Architecture](architecture/) folder before writing code.
8.  **Evolve**: If you need to break a rule, document the "Why" in a new [ADR](adr/).

## 📂 Contents

### 🏗️ Templates & Scaffolds
*Location: `/templates`*
- [**Python Starter**](templates/python-starter/): Production-ready FastAPI project template with `uv`, `pydantic-settings`, and structured logging.

### 📚 Development Guides
*Location: `/guides`*
- [**Python Best Practices**](guides/python_best_practices.md): Coding philosophy, style guides (PEP 8), and modern tooling recommendations (Ruff, Mypy).
- [**API Design Rules**](guides/api_rules.md): Standards for building RESTful APIs, including URL structure, versioning, and security.
- [**Testing & Definition of Done**](guides/testing_and_dod.md): A rigorous strategy for testing (Pyramid) and criteria for considering a task complete.
- [**Gemini CLI Rules**](guides/gemini_rules.md): Operational guidelines for AI agents working within the Gemini CLI environment.

### 🏛️ Architecture & Systems
*Location: `/architecture`*
- [**RAG Best Practices**](architecture/rag_best_practices.md): Guidelines for building high-quality Retrieval-Augmented Generation systems.
- [**MCP Best Practices**](architecture/mcp_best_practices.md): Design principles for Model Context Protocol servers.

### ⚖️ Architectural Decision Records (ADR)
*Location: `/adr`*
- *(No records yet)*
