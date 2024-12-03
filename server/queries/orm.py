from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import Base, async_engine, async_session_factory
from models import CharacterClass, CharacterSubclass


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_data():
        async with async_session_factory() as conn:
            character_class1 = CharacterClass(
                name='class1',
                description='desc1',
            )
            character_class2 = CharacterClass(
                name='class2',
                description='desc2',
            )
            character_subclass1 = CharacterSubclass(
                name='subclass1',
                description='subclass1',
            )
            character_subclass2 = CharacterSubclass(
                name='subclass2',
                description='subclass2',
            )
            character_class1.character_subclasses.append(character_subclass1)
            character_class2.character_subclasses.append(character_subclass2)
            conn.add_all([
                character_class1,
                character_class2,
            ])
            await conn.commit()

    @staticmethod
    async def get_all_character_classes():
        async with async_session_factory() as conn:
            query = select(CharacterClass)
            res = await conn.execute(query)
            character_classes = res.scalars().all()
            return character_classes

    @staticmethod
    async def get_all_character_classes_all_ref():
        async with async_session_factory() as conn:
            query = (
                select(CharacterClass)
                .options(selectinload(
                    CharacterClass.character_subclasses,
                ))
            )
            res = await conn.execute(query)
            character_classes = res.scalars().all()
            return character_classes
