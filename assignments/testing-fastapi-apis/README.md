# 📘 Assignment: Testing a FastAPI Task API

## 🎯 Objective

Write automated tests for a FastAPI task API using `pytest` and FastAPI's `TestClient`. You will verify successful responses and error handling without starting a web server.

## 📝 Tasks

### 🛠️	Test Successful Requests

#### Description
Use the provided `client` fixture to test the API endpoints that list tasks, retrieve a task, and create a new task.

#### Requirements
Completed program should:

- Test that `GET /tasks` returns a 200 status and the two sample tasks.
- Test that `GET /tasks/1` returns the task named `Learn FastAPI`.
- Test that `POST /tasks` returns a 201 status and includes the submitted title.

### 🛠️	Test Error Responses

#### Description
Add tests for requests that use task IDs not stored in the API. Check both the status code and the error message returned to the client.

#### Requirements
Completed program should:

- Test that `GET /tasks/999` returns a 404 status.
- Test that the missing-task response includes the message `Task not found`.
- Run all tests with `pytest` and ensure every test passes.