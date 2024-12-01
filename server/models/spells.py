from typing import TYPE_CHECKING, Optional

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .spell_durations import SpellDuration


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

    spell_duration: Mapped['SpellDuration'] = relationship(
        back_populates='spell',
    )

    @declared_attr
    def __table_args__(cls):
        return (
            *NameUniqueMaxLength50Mixin.__table_args__,
            CheckConstraint('range >= 0', name='min_length_spell_range'),
        )
