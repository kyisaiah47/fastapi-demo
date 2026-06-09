<div align="center">

<!-- BANNER_PLACEHOLDER -->

# ⚡ FastAPI Task API

**Auto docs, async Python, Pydantic validation — modern API development done right**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

</div>

<br/>

A task management REST API built with FastAPI to demonstrate modern Python async web development. Showcases zero-config interactive Swagger documentation, full type safety via Pydantic, and a clean RESTful design with standard HTTP semantics — everything you need to understand production-grade FastAPI patterns.

## ✨ Features

- **Zero-Config Swagger UI** — Interactive API docs auto-generated at `/docs`, no setup required
- **Type Safety** — End-to-end Python type hints enforced at runtime
- **Pydantic Validation** — Automatic request and response validation with clear error messages
- **Async Performance** — Built on ASGI for high concurrency and non-blocking I/O
- **Full CRUD** — Complete task lifecycle: create, read, update, and delete endpoints
- **RESTful Design** — Standard HTTP methods and status codes throughout

## 🛠️ Tech Stack

FastAPI · Python · Pydantic · Uvicorn

## 🚀 Getting Started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs at `http://localhost:8000` — interactive docs at `http://localhost:8000/docs`.

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks` | List all tasks |
| `POST` | `/api/tasks` | Create a new task |
| `GET` | `/api/tasks/{id}` | Get a specific task |
| `PUT` | `/api/tasks/{id}` | Update a task |
| `DELETE` | `/api/tasks/{id}` | Delete a task |

## 📄 License

MIT
