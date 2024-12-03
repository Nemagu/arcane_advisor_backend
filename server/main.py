import asyncio

from fastapi import FastAPI

from queries import AsyncORM
from routers import character_classes


async def create_db():
    await AsyncORM.create_tables()
    await AsyncORM.insert_data()


server = FastAPI()
server.include_router(character_classes.router)

if __name__ == '__main__':
    asyncio.run(create_db())
