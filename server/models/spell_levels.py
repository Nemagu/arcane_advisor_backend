from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base

from .mixins import DescriptionMixin, TimestampMixin

if TYPE_CHECKING:
    from .spells import Spell


class SpellLevel(
    DescriptionMixin,
    TimestampMixin,
    Base,
):
    level: Mapped[int] = mapped_column(unique=True)

    spells: Mapped[list['Spell']] = relationship(back_populates='level')

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint('level >= 0', name='min_value_spell_level'),
            CheckConstraint('level <= 9', name='max_value_spell_level'),
        )
