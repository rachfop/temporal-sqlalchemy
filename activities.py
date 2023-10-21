from temporalio import activity

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()



# Define our model for the database
class Greeting(Base):
    __tablename__ = 'greetings'
    id = Column(Integer, primary_key=True)
    message = Column(String)

# Set up a SQLite database for simplicity.
engine = create_engine('sqlite:///hello_world.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@activity.defn
async def save_greeting(message: str) -> None:
    """Activity to save greeting in the database."""
    session = Session()
    greeting = Greeting(message=message)
    session.add(greeting)
    session.commit()
    session.close()

@activity.defn
async def get_latest_greeting() -> str:
    """Activity to fetch the latest greeting from the database."""
    session = Session()
    last_greeting = session.query(Greeting).order_by(Greeting.id.desc()).first()
    session.close()
    return last_greeting.message if last_greeting else "<no greeting>"