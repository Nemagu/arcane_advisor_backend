from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import Base, async_engine, async_session_factory
from models import (
    CharacterClass,
    CharacterSubclass,
    Source,
    Spell,
    SpellCastingTime,
    SpellComponent,
    SpellLevel,
    SpellSchool,
    TypeDamage,
    UnitDuration
)


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_data():
        spell_test = Spell(
            name='spell_test',
            description='spell_test',
            range=1,
            next_level='description_next_level',
        )
        character_class_test = CharacterClass(
            name='character_class_test',
            description='character_class_test',
        )
        character_subclass_test = CharacterSubclass(
            name='character_subclass_test',
            description='character_subclass_test',
        )
        character_class_test.character_subclasses.append(
            character_subclass_test,
        )
        spell_school_test = SpellSchool(
            name='spell_school_test',
            description='spell_school_test',
        )
        spell_level_test = SpellLevel(
            level=1,
            description='spell_level_test',
        )
        type_damage_test = TypeDamage(
            name='type_damage_test',
            description='type_damage_test',
        )
        source_test = Source(
            name='source_test',
            description='source_test',
        )
        component_test = SpellComponent(
            name='component_test',
            description='component_test',
        )

        async with async_session_factory() as conn:
            conn.add_all([
                character_class_test,
                spell_school_test,
                spell_level_test,
                type_damage_test,
                source_test,
                component_test,
            ])
            # print(spell_school_test.id, '\n\n\n\n\n')
            await conn.flush()
            # print(spell_school_test.id, '\n\n\n\n\n')
            await conn.refresh(spell_school_test)
            # print(spell_school_test.id, '\n\n\n\n\n')
            await conn.refresh(spell_level_test)
            await conn.refresh(type_damage_test)
            await conn.refresh(source_test)

            spell_test.school = spell_school_test
            spell_test.level = spell_level_test
            spell_test.type_damage = type_damage_test
            spell_test.source = source_test
            conn.add(spell_test)
            await conn.flush()
            await conn.refresh(spell_test)
            await conn.refresh(character_class_test)
            await conn.refresh(character_subclass_test)
            await conn.refresh(component_test)
            # spell_test.character_classes.append(character_class_test)
            # spell_test.character_subclasses.append(character_subclass_test)
            # spell_test.components.append(component_test)
            character_class_test.spells.append(spell_test)
            conn.add(character_class_test)
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
