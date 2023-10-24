from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from temporalio import activity

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)


class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///todo_app.db")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    @activity.defn
    async def add_task(self, title: str) -> None:
        with self.get_session() as session:
            task = Task(title=title)
            session.add(task)
            session.commit()

    @activity.defn
    async def get_task_by_id(self, task_id: int) -> dict:
        with self.get_session() as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                return {"id": task.id, "title": task.title, "completed": task.completed}
            else:
                return None

    @activity.defn
    async def get_all_tasks(self) -> list:
        with self.get_session() as session:
            tasks = session.query(Task).all()
            return [
                {"id": t.id, "title": t.title, "completed": t.completed} for t in tasks
            ]

    @activity.defn
    async def toggle_task(self, task_id: int) -> dict:
        with self.get_session() as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                task.completed = not task.completed
                session.commit()
                return {"id": task.id, "title": task.title, "completed": task.completed}
            else:
                return None
