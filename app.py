from flask import Flask, jsonify, render_template, request
from temporalio.client import Client

from workflows import (
    AddTaskWorkflow,
    GetAllTasksWorkflow,
    GetTaskWorkflow,
    ToggleTaskWorkflow,
)

app = Flask(__name__)


async def get_temporal_client():
    return await Client.connect("localhost:7233")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/add_task", methods=["POST"])
async def add_task() -> str:
    data = request.get_json()
    title = data.get("title")
    client = await get_temporal_client()
    await client.execute_workflow(
        AddTaskWorkflow.add_task,
        title,
        id="add-task-workflow-id",
        task_queue="sql-db",
    )
    return jsonify({"message": f"{title} added successfully!"}), 201


@app.route("/get_all_tasks", methods=["GET"])
async def get_all_tasks() -> str:
    client = await get_temporal_client()
    result = await client.execute_workflow(
        GetAllTasksWorkflow.get_all_tasks,
        id="all-tasks-workflow-id",
        task_queue="sql-db",
    )
    print(f"Tasks: {result}")
    return jsonify({"message": "Tasks: ", "tasks": result}), 201


@app.route("/get_task/<int:task_id>", methods=["GET"])
async def get_task_by_id(task_id: int) -> str:
    client = await get_temporal_client()
    task = await client.execute_workflow(
        GetTaskWorkflow.get_task_by_id,
        task_id,
        id=f"task-{task_id}",
        task_queue="sql-db",
    )
    if task:
        task["success"] = True
        return jsonify(task), 200
    else:
        return jsonify({"success": False, "message": "Task not found"}), 404


@app.route("/toggle_task/<int:task_id>", methods=["POST"])
async def toggle_task(task_id: int) -> str:
    client = await get_temporal_client()
    result = await client.execute_workflow(
        ToggleTaskWorkflow.toggle_task,
        task_id,
        id=f"task-{task_id}",
        task_queue="sql-db",
    )
    print(f"Task: {result}")
    return jsonify({"message": "Task: ", "task": result}), 201


if __name__ == "__main__":
    app.run(debug=True)
