import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import Database
from workflows import (
    AddTaskWorkflow,
    GetAllTasksWorkflow,
    GetTaskWorkflow,
    ToggleTaskWorkflow,
)

db_instance = Database()


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="sql-db",
        workflows=[
            AddTaskWorkflow,
            GetAllTasksWorkflow,
            GetTaskWorkflow,
            ToggleTaskWorkflow,
        ],
        activities=[
            db_instance.add_task,
            db_instance.get_all_tasks,
            db_instance.get_task_by_id,
            db_instance.toggle_task,
        ],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
