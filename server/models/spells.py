from typing import Optional

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base
from .mixins import (DescriptionMixin, TimestampMixin,
                     UniqueNameMaxLength50Mixin)


class Spell(
    TimestampMixin,
    UniqueNameMaxLength50Mixin,
    DescriptionMixin,
    Base,
):
    range: Mapped[int]
    next_level: Mapped[Optional[str]]
    ritual: Mapped[bool] = mapped_column(default=False)
    concetration: Mapped[bool] = mapped_column(default=False)

    @declared_attr
    def __table_args__(cls):
        return (
            *UniqueNameMaxLength50Mixin.__table_args__,
            CheckConstraint('range > -1', name='min_length_spell_range'),
        )
