# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 🛠 Stack

- Python {{ cookiecutter.python_version }}+
- FastAPI
- uv (Dependency Management)

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the server**:
   ```bash
   uv run {{ cookiecutter.project_slug }}
   ```

3. **Check Health**:
   Visit `http://localhost:8000/api/health`

## 🧪 Testing

```bash
uv run pytest
```
