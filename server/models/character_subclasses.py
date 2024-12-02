from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .character_class_subclasses import CharacterClassSubclass


class CharacterSubclass(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    character_class: Mapped[
        'CharacterClassSubclass'
    ] = relationship(
        back_populates='combination_character_class_subclass',
        secondary='characterclasssubclass',
    )
