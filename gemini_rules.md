# 🌐 Gemini CLI Vibe-Coding Rules

## 🧱 Core Principles
1. **Clarity First**  
   Always give clear, unambiguous instructions. Be specific about intent, location, and constraints.

2. **Limited Scope per Action**  
   Modify *only* the specified files or sections unless explicitly permitted.

3. **Ask Before Acting**  
   Confirm:
   - when creating new files
   - when deleting code
   - before automatic refactors

4. **One Change per Response**  
   Return one atomic edit at a time with intention explanation.

## 🛠 Output Requirements
- Always show **diff output** (or full modified file) — never send partial or hidden changes.
- Include a **brief rationale** before each change.
- Provide **test cases** (if requested).

## ✅ Safety & Consistency
- Respect existing code formatting and conventions.
- Never invent APIs or external dependencies without confirmation.
- If unsure about requirements, ask clarification before generating code.

## 📏 Quality & Style
- Prioritize readability and maintainability.
- Use team/project style guidelines (e.g., ESLint/Prettier conventions).
- Avoid overly clever or dense constructs unless justified.

## ❓ Clarification Workflow
At the start of a task:
- Ask what part of the project this affects.
- Ask for any relevant test cases or constraints.
- Confirm technology stack and versions.

## 🧪 Validation & Testing
- Include basic tests when generating new functionality.
- Encourage test-driven development practices.

## 📜 Task Logging
- Provide a clear summary of work done.
- List assumptions made.
