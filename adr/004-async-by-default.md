# 4. Async by Default for I/O

Date: 2026-01-14
Status: Accepted

## Context
Modern web applications are I/O bound (waiting for DBs, APIs, AI models). Blocking the main thread in a synchronous web server (like WSGI) severely limits concurrency and throughput, requiring heavy worker scaling.

## Decision
We utilize **FastAPI** and **AsyncIO** as the default paradigm:
1.  **Async**: All I/O bound operations (DB queries, HTTP clients) MUST use `async/await`.
2.  **Sync**: CPU-bound operations (image processing, heavy math) should remain synchronous and be defined as standard `def` functions so FastAPI can offload them to a thread pool.

## Consequences
-   **Positive**: High concurrency with low resource usage.
-   **Positive**: Native compatibility with modern Python tooling (FastAPI, httpx, asyncpg).
-   **Negative**: "What color is your function?" problem (sync code cannot call async code easily).
-   **Negative**: Debugging async stack traces can be more complex.
