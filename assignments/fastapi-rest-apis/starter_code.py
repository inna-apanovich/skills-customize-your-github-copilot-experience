from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks: dict[int, Task] = {
    1: Task(title="Learn FastAPI"),
    2: Task(title="Build a REST API", completed=True),
}
next_task_id = 3


# Task 1: Add GET /tasks, GET /tasks/{task_id}, and POST /tasks endpoints.
# Return HTTPException(status_code=404) when a requested task does not exist.


# Task 2: Add PUT /tasks/{task_id} and DELETE /tasks/{task_id} endpoints.
# The delete endpoint should return Response(status_code=status.HTTP_204_NO_CONTENT).