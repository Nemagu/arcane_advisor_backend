from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base

from .mixins import DescriptionMixin, TimestampMixin


class SpellLevel(
    DescriptionMixin,
    TimestampMixin,
    Base,
):
    level: Mapped[int] = mapped_column(unique=True)

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint('level >= 0', name='min_value_spell_level'),
            CheckConstraint('level <= 9', name='max_value_spell_level'),
        )
