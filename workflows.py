import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import save_greeting, get_latest_greeting

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        greeting_message = f"Hello, {name}!"

        # Save the greeting in the database
        await workflow.execute_activity(
            save_greeting,
            greeting_message,
            start_to_close_timeout=timedelta(seconds=10),
        )

        # Retrieve and return the greeting from the database
        return await workflow.execute_activity(
            get_latest_greeting,
            start_to_close_timeout=timedelta(seconds=10),
        )