from typing import Optional

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)


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

    @declared_attr
    def __table_args__(cls):
        return (
            *NameUniqueMaxLength50Mixin.__table_args__,
            CheckConstraint('range >= 0', name='min_length_spell_range'),
        )
