# AI & Development Guidelines

[![CI](https://github.com/lilidl-nft/AI/actions/workflows/test-template.yml/badge.svg)](https://github.com/lilidl-nft/AI/actions/workflows/test-template.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Agentic](https://img.shields.io/badge/Agentic-Ready-blueviolet)](llms.txt)

This repository serves as a central knowledge base for coding standards, best practices, and project templates. It is designed to ensure consistency, quality, and strict adherence to "Zen of Python" principles across all projects.

## 🚀 Workflow: How to use this repo

Follow these steps to ship high-quality code using these guidelines:

1.  **Scaffold**: Start your project using the standard template.
    ```bash
    # Requires cookiecutter (uv tool install cookiecutter)
    cookiecutter https://github.com/lilidl-nft/AI --directory templates/python-starter
    ```
2.  **Enforce**: Copy the standard configs to your project root to ensure quality gates are active from Day 1.
    -   `cp configs/pyproject.toml .` (Linting/Typing rules)
    -   `cp configs/pre-commit-config.yaml .` (Git hooks)
    -   `mkdir -p .github/workflows && cp configs/ci.yml .github/workflows/` (CI Pipeline)
3.  **Contextualize AI**: Copy `guides/gemini_rules.md` to your project root (e.g., as `.cursorrules` or `gemini_rules.md`) so your AI assistant knows the rules.
4.  **Configure**: Set up your environment using `.env.example` as a template. Enforce configuration via `pydantic-settings`.
5.  **Implement**: Write code following strict [Python Best Practices](guides/python_best_practices.md) and [API Rules](guides/api_rules.md).
6.  **Verify**: Run the quality gates before committing.
    ```bash
    uv run pytest
    uv run ruff check
    uv run mypy .
    ```
7.  **Review**: Check your work against the [Definition of Done](guides/testing_and_dod.md) checklist.
8.  **Architect**: If building RAG or MCP systems, consult the [Architecture](architecture/) folder before writing code.
9.  **Evolve**: If you need to break a rule, document the "Why" in a new [ADR](adr/).

## 🤖 AI Agent Usage

This repository is optimized for consumption by AI models.

-   **Context Injection**: Feed `llms.txt` to your LLM to give it immediate knowledge of all our standards.
-   **System Persona**: Use `prompts/system_prompt.md` as the system instruction for any chat-based coding assistant.
-   **Discovery**: Autonomous agents can read `agent_manifest.json` to map the repository resources.

## 📂 Contents

### ⚙️ Enforceable Configs
*Location: `/configs`*
- [**pyproject.toml**](configs/pyproject.toml): The "One Config to Rule Them All" for Ruff, Mypy, and Pytest.
- [**pre-commit-config.yaml**](configs/pre-commit-config.yaml): Standard git hooks to fix issues before they are committed.
- [**ci.yml**](configs/ci.yml): GitHub Actions workflow for automated testing and linting.
- [**dependabot.yml**](configs/dependabot.yml): Automated dependency updates.

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
- [**001: Use `uv`**](adr/001-use-uv-for-dependency-management.md): Why we chose `uv` over Poetry/Pip.
- [**002: Pragmatic Strict Typing**](adr/002-pragmatic-strict-typing.md): Our stance on Mypy strictness.
- [**003: `src/` Layout**](adr/003-src-layout.md): Why we nest code in a `src` folder.
- [**004: Async by Default**](adr/004-async-by-default.md): When to use `async` vs `sync`.
