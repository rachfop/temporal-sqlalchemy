import asyncio

from temporalio.client import Client
from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "first greeting",
        id="hello-activity-workflow-id",
        task_queue="sql-db",
    )
    print(f"Result: {result}")
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "second greeting",
        id="hello-activity-workflow-id",
        task_queue="sql-db",
    )
    print(f"Result: {result}")
if __name__ == "__main__":
    asyncio.run(main())