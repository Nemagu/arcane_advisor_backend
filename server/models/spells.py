from typing import TYPE_CHECKING, Optional

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .sources import Source
    from .spell_casting_time import SpellCastingTime
    from .spell_components import SpellComponent
    from .spell_durations import SpellDuration
    from .spell_levels import SpellLevel
    from .spell_schools import SpellSchool
    from .type_damage import TypeDamage


class Spell(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    range: Mapped[int]
    next_level: Mapped[Optional[str]]
    ritual: Mapped[bool] = mapped_column(default=False)
    concetration: Mapped[bool] = mapped_column(default=False)

    school_id: Mapped[int] = mapped_column(
        ForeignKey('spellschool.id'),
        primary_key=True,
    )
    school: Mapped['SpellSchool'] = relationship(back_populates='spells')

    level_id: Mapped[int] = mapped_column(
        ForeignKey('spelllevel.id'),
        primary_key=True,
    )
    level: Mapped['SpellLevel'] = relationship(back_populates='spells')

    type_damage_id: Mapped[int] = mapped_column(
        ForeignKey('typedamage.id'),
        primary_key=True,
    )
    type_damage: Mapped['TypeDamage'] = relationship(back_populates='spells')

    source_id: Mapped[int] = mapped_column(
        ForeignKey('source.id'),
        primary_key=True,
    )
    source: Mapped['Source'] = relationship(back_populates='spells')

    components: Mapped[list['SpellComponent']] = relationship(
        back_populates='spells',
        secondary='refspellcomponent',
    )
    duration: Mapped['SpellDuration'] = relationship(
        back_populates='spell',
    )
    casting_time: Mapped['SpellCastingTime'] = relationship(
        back_populates='spell',
    )

    @declared_attr
    def __table_args__(cls):
        return (
            *NameUniqueMaxLength50Mixin.__table_args__,
            CheckConstraint('range >= 0', name='min_value_spell_range'),
        )
