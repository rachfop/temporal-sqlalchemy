# ToDo app: Flask and Temporal

![](static/code-example.png)

## Documentation

This tutorial will guide you through building a simple ToDo application using Flask for the web API and Temporal for orchestrating workflows.
This app enables users to add tasks, retrieve all tasks, fetch a task by its ID, and toggle a task's completion status.

## Prerequisites:

1. Have Python installed.
2. Install Flask, SQLAlchemy, and Temporal Python SDK.
3. Familiarity with basic Flask concepts and SQLAlchemy.

## Step-by-step guide:

### 1. Database Setup with SQLAlchemy

The `activities.py` file defines the `Task` model and database-related operations.

1. **Define the Task Model**: This is the structure of the task with fields such as id, title, and completed status.
2. **Setup SQLite Database**: For this tutorial, we are using SQLite. However, you can easily switch to another database.

### 2. Building Activities with Temporal

Temporal activities are individual pieces of logic or operations in the workflow.

1. The `add_task` activity allows us to add a new task.
2. The `get_task_by_id` fetches a specific task.
3. The `get_all_tasks` fetches all tasks.
4. The `toggle_task` toggles the completed status of a task.

Each of these activities interacts with the database, and they are asynchronous.

### 3. Flask App

In the `app.py` file, the Flask routes are defined.

1. The `main` route displays the web page.
2. Other routes are API endpoints that execute corresponding workflows in Temporal.
3. The `get_temporal_client` method creates a connection to the Temporal server.

### 4. Workflows with Temporal

The `workflows.py` file defines the workflows, which are a series of steps or operations.

Each workflow corresponds to an API endpoint. The workflow uses the defined activities and sets a timeout for each operation.

### 5. Running the Temporal Worker

Temporal requires a worker to poll for tasks and execute them. The `run_worker.py` file runs a Temporal worker that listens for tasks and executes the defined workflows and activities.

### 6. Running the App

- First, start the Temporal worker using the `run_worker.py` script.
- Next, start the Flask app using the `app.py` script.

## Summary:

With Flask handling web requests and Temporal managing workflows, we've created a robust ToDo app. Flask serves the API, while Temporal ensures that operations like adding or toggling tasks are handled reliably. This separation of concerns allows for better scalability and fault tolerance. 

Remember, Temporal is suitable for applications that require reliability, as it provides features like retries, timeouts, and distributed tracing out of the box.

By following this tutorial, you've learned how to combine Flask and Temporal to build a resilient and scalable application. Now, you can expand upon this foundation by adding more features, integrating user authentication, or switching to a more scalable database.

## Start the app

To start the app, run the following command:

```bash
# terminal 1
poetry run python run_worker.py
# terminal 2
poetry run python app.py
```

Now you can interact with the app using the provided API.
Choose one of the following options:

### Use the web app

You can visit the web app at http://127.0.0.1:5000 and interact with the app.

### Use the API

The provided code showcases a Flask API integrated with Temporal.
Here's how you would interact with this API using `curl` commands:

1. **Add a Task**:

   You can use this `curl` command to add a task. This is a POST request that takes a `title` for the task.

   ```bash
   curl -X POST http://127.0.0.1:5000/add_task -H "Content-Type: application/json" -d '{"title": "Hello World!"}'
   ```

2. **Get All Tasks**:

   You can fetch all tasks with this command.
   This is a simple GET request.

   ```bash
   curl -X GET http://127.0.0.1:5000/get_all_tasks
   ```

3. **Get a Specific Task by ID**:

   For retrieving a specific task using its `task_id`, you'd use this `curl` command:

   ```bash
   curl -X GET http://127.0.0.1:5000/get_task/1
   ```

   Replace `1` with the actual task ID you wish to retrieve.

4. **Complete a Task**:

   To mark a task as completed, use this `curl` command:

   ```bash
   curl -X POST http://127.0.0.1:5000/toggle_task/1
   ```

   Replace `1` with the actual task ID you wish to complete.