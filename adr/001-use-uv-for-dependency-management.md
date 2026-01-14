# 1. Use `uv` for Dependency Management

Date: 2026-01-14
Status: Accepted

## Context
Python packaging has historically been fragmented (pip, virtualenv, poetry, pip-tools, pipenv). Teams often struggle with slow CI/CD pipelines due to dependency resolution and environment setup times. We needed a tool that is fast, reliable, and standards-compliant (`pyproject.toml`).

## Decision
We will use **[uv](https://github.com/astral-sh/uv)** as the single source of truth for:
1.  Python version management.
2.  Virtual environment creation.
3.  Dependency resolution and locking.
4.  Tool installation.

We explicitly **reject** Conda for general Python development to avoid mixing package indices and the complexity of solver environments, unless specific data science libraries strictly require it (rare nowadays).

## Consequences
-   **Positive**: CI/CD setup times are drastically reduced (10-100x faster).
-   **Positive**: `pyproject.toml` remains the standard configuration file.
-   **Negative**: Developers must install a Rust-based tool (though it ships as a standalone binary).
-   **Negative**: Some legacy workflows relying on `requirements.txt` generation need to use `uv pip compile`.
