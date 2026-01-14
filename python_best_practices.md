# 🐍 Python Development Best Practices

## 🧠 Core Philosophy (The Zen - Guiding principles for clean code)
*These rules ensure code remains readable and maintainable over time.*
1.  **Explicit is better than implicit**: Avoid "magic" behavior. Function arguments should be obvious.
2.  **Simple is better than complex**: If the logic requires a paragraph to explain, refactor it.
3.  **Flat is better than nested**: Avoid deep folder structures and deeply nested `if/else` blocks.
4.  **Errors should never pass silently**: Use strict error handling. Fail fast and loudly.

## 🎨 Style & Standards (PEP 8 - Keeping the code looking consistent)
*Consistent formatting makes it easier for different developers to work on the same codebase.*
- **Compliance**: Follow [PEP 8](https://peps.python.org/pep-0008/) strictly for naming and structure.
- **Naming**:
  - `snake_case`: Variables, functions, and modules.
  - `PascalCase`: Classes and Types.
  - `UPPER_CASE`: Constants.
- **Automation**: Use `ruff format` to handle spacing, indentation, and line lengths (88-100 chars) automatically.

## 🏷️ Pragmatic Type Hinting (Type safety without the friction)
*Use types to catch bugs early, but don't let them make the code impossible to read.*
- **Boundary Typing**: Always type-hint function signatures (arguments and return types). This is where types provide the most value for IDEs and static analysis.
- **Avoid Overhead**:
  - Do not type-hint simple local variables unless the type is ambiguous.
  - Use `Any` or `object` sparingly but without guilt if a complex generic type becomes a maintenance burden.
  - Prioritize readability: If a type hint makes a line unreadable, consider using a `TypeAlias` or simplifying.
- **Static vs Runtime**: Rely on `mypy` for static checks. Avoid runtime type-checking libraries inside business logic to keep the code fast.
- **Tooling**: Use `mypy` with a "pragmatic" config (ignore missing imports where necessary, but enforce signature typing).

## 🏗️ Code Structure (Organizing files for scalability)
*A clear structure helps new developers find their way around the project.*
- **Src Layout**: Always use the `src/` directory pattern. It prevents import errors and ensures you test against the installed package, not the local folder.
- **Modules**: Keep files small (< 400 lines). If a file grows too large, split it by domain/responsibility, not by technical layer.
- **Imports**: absolute imports only (`from my_package.services import logic`) over relative imports (`from ..services import logic`).

## 🧪 Testing Guidelines (Ensuring the code actually works)
*Tests are your safety net. They allow you to refactor with confidence.*
- **Framework**: `pytest` is the standard.
- **Fixtures**: Use `conftest.py` for shared fixtures. Avoid global state.
- **Unit vs Integration**:
  - **Unit**: Mock external dependencies (DB, APIs). Fast.
  - **Integration**: Test the full path with test containers or local services.
- **Coverage**: Aim for high coverage in business logic (`services/`), lower in declarative code (`models/`).

## ⚡ FastAPI & API Design (Building high-performance web services)
*Leverage FastAPI's strengths to build robust and self-documenting APIs.*
- **Pydantic**: Use Pydantic models for all Request/Response bodies. Never return raw dicts.
- **Dependency Injection**: Use FastAPI's `Depends` for shared logic (DB sessions, current user, config).
- **Sync vs Async**:
  - Use `async def` for I/O bound operations (DB, external APIs).
  - Use `def` for CPU bound operations to avoid blocking the event loop.

## 📝 Documentation & logging (Communicating with other humans and tools)
*Good logs and docs are essential for debugging production issues.*
- **Docstrings**: Google Style docstrings for complex functions.
- **Logs**:
  - Use `structlog` or standard `logging` with JSON formatters in production.
  - Never use `print()`.

## 🔒 Security (Protecting your data and users)
*Security is not an afterthought; it should be baked into the development process.*
- **Secrets**: Never commit `.env` files. Use `pydantic-settings` to read from environment variables.
- **Input Validation**: Trust nothing. Let Pydantic validate all incoming data.