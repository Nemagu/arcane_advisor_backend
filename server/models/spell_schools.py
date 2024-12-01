from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .spells import Spell


class SpellSchool(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    spells: Mapped[list['Spell']] = relationship(back_populates='school')
