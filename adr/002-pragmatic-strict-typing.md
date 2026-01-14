# 2. Pragmatic Strict Typing

Date: 2026-01-14
Status: Accepted

## Context
Dynamic typing in Python allows for rapid prototyping but leads to runtime errors ("AttributeError: 'NoneType' object has no attribute 'x'") in production. "Strict" typing can be burdensome and slow down development if applied dogmatically to every local variable.

## Decision
We adopt a **"Pragmatic Strict"** approach using `mypy`:
1.  **Boundaries are Sacred**: Function signatures (args, return types) and Class attributes **MUST** be typed.
2.  **Strict Config**: We enable `strict = true` in `pyproject.toml` to catch implicit `Any` and untyped definitions.
3.  **Escape Hatches**: We allow `ignore_missing_imports = true` for untyped 3rd party libraries and permit explicit `Any` when the type system cannot easily express the logic without excessive boilerplate.

## Consequences
-   **Positive**: Significant reduction in `NoneType` errors in production.
-   **Positive**: Code becomes self-documenting via signatures.
-   **Negative**: Initial learning curve for developers unused to static typing.
-   **Negative**: Occasionally requires "fighting" the type checker for complex dynamic patterns (metaprogramming).
