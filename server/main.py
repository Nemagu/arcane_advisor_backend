import asyncio

from queries import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_data()


if __name__ == '__main__':
    asyncio.run(main())
