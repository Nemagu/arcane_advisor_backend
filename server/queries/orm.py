from database import Base, async_engine, async_session_factory
from models import Spell


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_data():
        async with async_session_factory() as conn:
            spell_1 = Spell(name='spell_1')
            spell_2 = Spell(name='spell_2')
            conn.add_all([spell_1, spell_2])
            await conn.commit()
