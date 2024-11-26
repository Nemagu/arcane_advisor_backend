from database import Base, session_factory, sync_engine
from models import WorkersORM


def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def insert_data():
    worker_bobr = WorkersORM(username='Bobr')
    worker_kurva = WorkersORM(username='kurva')
    with session_factory() as session:
        session.add_all((worker_bobr, worker_kurva))
        session.commit()
