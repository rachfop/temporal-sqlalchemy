import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import save_greeting, get_latest_greeting
from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="sql-db",
        workflows=[GreetingWorkflow],
        activities=[save_greeting, get_latest_greeting],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())