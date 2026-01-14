# 🧪 Testing Strategy & Definition of Done

## 🎯 Testing Philosophy
*Tests are not just for finding bugs; they are executable documentation and a safety net for refactoring.*

### 1. The Testing Pyramid
We prioritize fast, reliable tests at the bottom of the pyramid.

- **Unit Tests (70%)**:
  - **Scope**: Individual functions, classes, and business logic (`services/`).
  - **Speed**: Extremely fast (< 10ms per test).
  - **Dependencies**: All external I/O (DB, APIs, Disk) must be **mocked**.
  - **Goal**: Verify logic in isolation.

- **Integration Tests (20%)**:
  - **Scope**: Interaction between modules and external systems (DB, Cache).
  - **Tooling**: Use `testcontainers` or local docker-compose services.
  - **Goal**: Verify that the application talks to the database/API correctly.

- **End-to-End (E2E) Tests (10%)**:
  - **Scope**: Critical user flows from the API entry point to the database and back.
  - **Goal**: Ensure the system works as a whole from the user's perspective.

## 🛠️ Tooling & Standards

- **Runner**: `pytest`
- **Mocking**: `unittest.mock` or `pytest-mock`
- **Coverage**: `pytest-cov`
  - **Target**: > 80% overall, 100% for critical business logic.
  - **Constraint**: Builds should fail if coverage drops.
- **Async Support**: `pytest-asyncio` for FastAPI/AsyncIO tests.

## ✅ Definition of Done (DoD)

*A feature or task is only considered "Complete" when all the following criteria are met:*

### 1. Code Quality
- [ ] Code follows **PEP 8** and project style guidelines (`ruff check` passes).
- [ ] Type hints are present for all boundaries (`mypy` passes).
- [ ] No dead code or unused imports.

### 2. Testing
- [ ] **Unit Tests** implemented for all new logic.
- [ ] **Integration Tests** added for new DB queries or API clients.
- [ ] Test coverage meets the project threshold (> 80%).
- [ ] All existing tests pass (regression check).

### 3. Documentation
- [ ] Docstrings added/updated for public modules and complex functions.
- [ ] `README.md` updated if setup or usage instructions changed.
- [ ] API documentation (Swagger/OpenAPI) is accurate.

### 4. Review & Build
- [ ] CI/CD pipeline passes (Lint, Test, Type Check).
- [ ] Code review completed and approved by at least one peer.
- [ ] No sensitive data (secrets, keys) committed.

## 🚀 Release Criteria
*Before deploying to production:*
- [ ] Semantic versioning bumped (e.g., `v1.0.1` -> `v1.1.0`).
- [ ] Changelog updated.
- [ ] `/health` endpoint validates all downstream dependencies.
