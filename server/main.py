from contextlib import asynccontextmanager

from fastapi import FastAPI

from queries import AsyncORM
from routers import character_classes


@asynccontextmanager
async def lifespan(server: FastAPI):
    await AsyncORM.create_tables()
    await AsyncORM.insert_data()
    yield


server = FastAPI(lifespan=lifespan)
server.include_router(character_classes.router)
