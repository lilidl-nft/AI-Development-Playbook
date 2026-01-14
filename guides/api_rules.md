# 🌐 API Design Rules & Standards

## 🧠 Core Principles
*Design APIs that are intuitive, consistent, and easy to consume.*

1.  **Resource-Oriented**: Design around nouns (resources), not verbs.
    -   ✅ `POST /users` (Create user)
    -   ❌ `POST /createUser`
2.  **Predictable**: Use standard HTTP methods and status codes.
3.  **Stateless**: Each request must contain all necessary information (auth tokens, context).

## 🛤️ URL Structure & Versioning

-   **Base URL**: `/api/{version}/{resource}`
-   **Versioning**: Mandatory in the path.
    -   Example: `/api/v1/users`
-   **Naming**:
    -   Use `kebab-case` for URLs: `/api/v1/user-profiles`
    -   Plural nouns for collections: `/users`, `/products`
    -   IDs for specific items: `/users/{user_id}`

## 🛠️ HTTP Methods

| Method | Action | Idempotent | Success Code |
| :--- | :--- | :--- | :--- |
| **GET** | Retrieve resource(s) | Yes | `200 OK` |
| **POST** | Create a resource | No | `201 Created` |
| **PUT** | Update (Replace) | Yes | `200 OK` |
| **PATCH** | Update (Partial) | Yes | `200 OK` |
| **DELETE** | Remove a resource | Yes | `204 No Content` |

## 📦 Request & Response Standards

### JSON Everywhere
-   **ContentType**: Always `application/json`.
-   **Naming**: Use `snake_case` for JSON keys (matching Python conventions).
    -   *Note: Frontend may prefer camelCase. Configure Pydantic to handle conversion if strictly required, but consistent snake_case is preferred for backend simplicity.*

### Standard Response Envelope (Optional but recommended for consistency)
```json
{
  "data": { ... },       // The requested resource
  "meta": {              // Pagination, timing, etc.
    "page": 1,
    "total": 100
  }
}
```

### Error Handling
Return structured error responses, not just plain text.
```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "The user with ID 123 does not exist.",
    "details": "..."
  }
}
```
-   **400 Bad Request**: Validation failure (Client side).
-   **401 Unauthorized**: Missing or invalid token.
-   **403 Forbidden**: Valid token, but not allowed (Scopes/Permissions).
-   **404 Not Found**: Resource does not exist.
-   **500 Internal Server Error**: Bug in the server code (Alert on this!).

## ⚡ Performance & Pagination

-   **Pagination**: Mandatory for all list endpoints.
    -   Use `limit` and `offset` (or cursor-based for high volume).
    -   Default: `limit=20`, Max: `limit=100`.
-   **Filtering**: Use query parameters.
    -   `/users?role=admin&active=true`
-   **Sorting**:
    -   `/users?sort=-created_at` (descending)

## 🔒 Security Best Practices

-   **HTTPS**: Enforce TLS 1.2+ everywhere.
-   **Authentication**: Bearer Token (JWT) in `Authorization` header.
-   **Rate Limiting**: Implement per-user or per-IP limits to prevent abuse (e.g., 100 requests/minute).
-   **CORS**: Restrict `Access-Control-Allow-Origin` to trusted domains only.

## 📝 Documentation

-   **OpenAPI (Swagger)**: Must be auto-generated from code (FastAPI does this).
-   **Descriptions**: Every endpoint must have a summary and description.
-   **Examples**: Provide example requests and responses for every schema.
