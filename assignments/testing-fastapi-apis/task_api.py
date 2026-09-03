from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks: dict[int, Task] = {
    1: Task(title="Learn FastAPI"),
    2: Task(title="Write API tests", completed=True),
}
next_task_id = 3


@app.get("/tasks")
def list_tasks() -> dict[int, Task]:
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task) -> Task:
    global next_task_id
    tasks[next_task_id] = task
    next_task_id += 1
    return task