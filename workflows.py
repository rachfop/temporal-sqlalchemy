from datetime import timedelta

from temporalio import workflow

from activities import Database

db_instance = Database()


@workflow.defn
class AddTaskWorkflow:
    @workflow.run
    async def add_task(self, title: str) -> list:
        return await workflow.execute_activity(
            db_instance.add_task,
            title,
            start_to_close_timeout=timedelta(seconds=10),
        )


@workflow.defn
class GetAllTasksWorkflow:
    @workflow.run
    async def get_all_tasks(self) -> list:
        return await workflow.execute_activity(
            db_instance.get_all_tasks,
            start_to_close_timeout=timedelta(seconds=10),
        )


@workflow.defn
class GetTaskWorkflow:
    @workflow.run
    async def get_task_by_id(self, task_id: int) -> dict:
        return await workflow.execute_activity(
            db_instance.get_task_by_id,
            task_id,
            start_to_close_timeout=timedelta(seconds=10),
        )


@workflow.defn
class ToggleTaskWorkflow:
    @workflow.run
    async def toggle_task(self, task_id: int) -> dict:
        return await workflow.execute_activity(
            db_instance.toggle_task,
            task_id,
            start_to_close_timeout=timedelta(seconds=10),
        )
