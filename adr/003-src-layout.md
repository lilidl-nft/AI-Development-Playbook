# 3. Adoption of `src/` Layout

Date: 2026-01-14
Status: Accepted

## Context
Python projects can be structured with the package at the root or nested inside a `src/` directory. The root layout often leads to "import parity" issues where tests run against the local folder instead of the installed package, masking missing dependencies or build artifacts.

## Decision
We enforce the **`src/` layout** for all Python projects.
-   Code resides in `src/package_name/`.
-   Tests reside in `tests/`.

## Consequences
-   **Positive**: Prevents accidental import of the local package when running generic commands (e.g., `pytest`).
-   **Positive**: Forces developers to properly define package build metadata in `pyproject.toml`.
-   **Positive**: Keeps the project root clean (only config files and docs).
-   **Negative**: Slightly more verbose file paths.
-   **Negative**: Requires editable installs (`uv pip install -e .`) for local development to work (which is standard practice anyway).
