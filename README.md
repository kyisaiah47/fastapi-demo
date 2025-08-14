# FastAPI Task Management API

A simple task management API built with FastAPI to demonstrate modern Python web development.

## 🚀 Features

- **Automatic API Documentation** - Interactive docs at `/docs`
- **Type Safety** - Full Python type hints with Pydantic
- **Data Validation** - Automatic request/response validation
- **Async Performance** - Built for high concurrency
- **RESTful Design** - Standard HTTP methods and status codes

## 📦 Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd fastapi-task-api

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Start the development server
uvicorn main:app --reload

# Server will start at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

## 🧪 API Endpoints

- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

## 💾 Example Usage

```bash
# Create a task
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"Build awesome APIs","priority":"high"}'

# Get all tasks
curl "http://localhost:8000/api/tasks"
```

## 🛠 Tech Stack

- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI web server

## 🔄 Development Workflow

1. Make changes to `main.py`
2. Server auto-reloads (thanks to `--reload` flag)
3. Test at http://localhost:8000/docs
4. Commit changes to git

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## 📝 License

MIT License
