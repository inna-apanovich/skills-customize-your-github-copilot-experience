# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that lets clients create, read, update, and delete tasks. You will practice defining routes, using Pydantic models, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️	Create Task Endpoints

#### Description
Use the provided starter code to create endpoints for listing all tasks, retrieving one task by its ID, and adding a new task.

#### Requirements
Completed program should:

- Define a `Task` Pydantic model with `title` and `completed` fields.
- Return the full task list from `GET /tasks`.
- Return an individual task from `GET /tasks/{task_id}` or raise a 404 error when the ID does not exist.
- Add a task with `POST /tasks` and return a 201 Created status.

### 🛠️	Complete the Task API

#### Description
Add endpoints that allow a client to update an existing task and delete a task that is no longer needed.

#### Requirements
Completed program should:

- Update a task's title or completion status with `PUT /tasks/{task_id}`.
- Delete a task with `DELETE /tasks/{task_id}` and return a 204 No Content status.
- Raise a 404 error when an update or delete request uses an unknown task ID.
- Run the application with `uvicorn starter_code:app --reload` and verify the endpoints in FastAPI's `/docs` page.