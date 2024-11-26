from database import session_factory, sync_engine
from models import WorkersORM, metadata_obj
from sqlalchemy import insert


def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


def insert_data():
    worker_bobr = WorkersORM(username='Bobr')
    worker_kurva = WorkersORM(username='kurva')
    with session_factory() as session:
        session.add_all((worker_bobr, worker_kurva))
        session.commit()
