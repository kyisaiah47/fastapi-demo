from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple task management API built with FastAPI",
    version="1.0.0"
)

# Enums for validation (like NestJS)
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"

# Pydantic models (these are like NestJS DTOs!)
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: str = Field(..., min_length=1, max_length=500, description="Task description")
    priority: Priority = Field(..., description="Task priority level")

class TaskCreate(TaskBase):
    status: Optional[Status] = Field(Status.pending, description="Task status")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    priority: Optional[Priority] = None
    status: Optional[Status] = None

class Task(TaskBase):
    id: int
    status: Status
    created_at: datetime
    
    class Config:
        # This allows the model to work with ORM objects
        from_attributes = True

# In-memory storage (like our NestJS version)
tasks_db: List[Task] = [
    Task(
        id=1,
        title="Sample Task",
        description="This is a sample task",
        priority=Priority.high,
        status=Status.pending,
        created_at=datetime.now()
    )
]
next_id = 2

# Helper function to find task
def find_task_by_id(task_id: int) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Task with ID {task_id} not found"
    )

# API Routes (compare to NestJS controllers!)

@app.get("/", tags=["Root"])
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}

@app.get("/api/tasks", response_model=List[Task], tags=["Tasks"])
async def get_all_tasks():
    """Retrieve all tasks"""
    return tasks_db

@app.get("/api/tasks/{task_id}", response_model=Task, tags=["Tasks"])
async def get_task(task_id: int):
    """Retrieve a specific task by ID"""
    return find_task_by_id(task_id)

@app.post("/api/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
async def create_task(task_data: TaskCreate):
    """Create a new task"""
    global next_id
    
    new_task = Task(
        id=next_id,
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        status=task_data.status or Status.pending,
        created_at=datetime.now()
    )
    
    tasks_db.append(new_task)
    next_id += 1
    
    return new_task

@app.put("/api/tasks/{task_id}", response_model=Task, tags=["Tasks"])
async def update_task(task_id: int, task_data: TaskUpdate):
    """Update an existing task"""
    task = find_task_by_id(task_id)
    
    # Update only provided fields
    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    return task

@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
async def delete_task(task_id: int):
    """Delete a task"""
    global tasks_db
    
    task = find_task_by_id(task_id)
    tasks_db = [t for t in tasks_db if t.id != task_id]
    
    return None

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)