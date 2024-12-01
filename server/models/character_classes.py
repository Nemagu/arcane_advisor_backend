from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .charcter_class_subclasses import CharacterClassSubclass


class CharacterClass(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    combination_character_class_subclass: Mapped[
        'CharacterClassSubclass'
    ] = relationship(
        back_populates='character_class',
    )
