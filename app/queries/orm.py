from config import (Base, async_engine, async_session_factory, session_factory,
                    sync_engine)
from models import Spell


async def create_tables():
    async with async_engine.begin() as session:
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)


async def insert_data():
    async with session_factory() as session:
        spell_1 = Spell(unique_name='ddasfskflj')
        spell_2 = Spell(unique_name='ajasdfsdf')
        session.add_all([spell_1, spell_2])
        # session.add(spell_1)
        # session.add(spell_2)
        await session.commit()
