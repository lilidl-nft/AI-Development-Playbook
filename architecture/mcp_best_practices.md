# 🔌 MCP Best Practices (Model Context Protocol)

## 🎯 Core Philosophy
*MCP connects AI models to the real world. Tools should be safe, atomic, and self-describing.*

1.  **Safety First**: AI agents can hallucinate. Tools must validate all inputs and prevent destructive actions without confirmation.
2.  **Atomic Operations**: Tools should do *one* thing well. Complex workflows should be composed of multiple simple tool calls.
3.  **Self-Describing**: The LLM learns how to use your tool solely from its JSON schema and description. Make them count.

## 🛠️ Tool Definition & Schema

-   **Naming**: Use `snake_case` for tool names (e.g., `get_user_profile`, `restart_server`).
    -   Avoid generic names like `run` or `execute`.
-   **Descriptions**: Write for the AI, not the human.
    -   *Bad*: "Gets data."
    -   *Good*: "Retrieves the full user profile including email and preferences by user ID. Returns null if not found."
-   **Input Schema**:
    -   Use strict JSON types (string, number, boolean).
    -   Use `enum` to constrain choices (e.g., `status: ["active", "pending"]`).
    -   Mark required fields explicitly.

## 🔒 Security & Side Effects

-   **Read vs. Write**: Distinctly categorize tools.
    -   **Read-Only**: Safe to auto-execute (e.g., `list_files`, `search_logs`).
    -   **Side-Effect**: Modifications (e.g., `write_file`, `delete_user`).
-   **Confirmation**: "Write" tools should generally trigger a user confirmation prompt in the client, or require a specific "force" flag if automated.
-   **Sandboxing**: MCP servers should ideally run in isolated environments (Docker containers) to limit filesystem access.
-   **Validation**: **Trust nothing.** Validate every parameter inside the tool implementation, even if the schema says it's a number.

## 📡 Server Implementation

-   **Transport**: Use **Stdio** for local desktop tools (e.g., connecting to a local CLI) and **SSE** (Server-Sent Events) for remote tools.
-   **Error Handling**:
    -   Do not crash the server on tool failure.
    -   Return descriptive error messages in the tool output so the LLM can self-correct.
    -   *Example*: "File not found at path /foo.txt. Did you mean /bar.txt?" instead of just "Error".
-   **Logging**: Log tool calls and arguments to stderr (if using Stdio) to debug what the LLM is attempting.

## 🧪 Testing MCP Servers

-   **Inspector**: Use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) to interactively test your tools without an LLM.
-   **Mocking**: Test your tools against mock data before connecting to live production APIs.

## 📚 Resources & Prompts

-   **Resources**: Use MCP Resources for static context (files, logs) that the LLM reads frequently.
-   **Prompts**: Define standard Prompts (templates) for common tasks to guide the LLM's behavior (e.g., "Analyze this log file").
