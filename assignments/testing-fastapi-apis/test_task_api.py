from fastapi.testclient import TestClient

from task_api import Task, app, tasks

client = TestClient(app)


def setup_function() -> None:
    tasks.clear()
    tasks.update(
        {
            1: Task(title="Learn FastAPI"),
            2: Task(title="Write API tests", completed=True),
        }
    )


# Task 1: Write tests for GET /tasks, GET /tasks/1, and POST /tasks.
# Check the response status code and returned JSON in every test.


# Task 2: Write a test for GET /tasks/999.
# Check that it returns status code 404 and detail "Task not found".