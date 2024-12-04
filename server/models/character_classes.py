from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .character_subclasses import CharacterSubclass
    from .spells import Spell


class CharacterClass(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    character_subclasses: Mapped[list['CharacterSubclass']] = relationship(
        back_populates='character_class',
    )
    spells: Mapped[list['Spell']] = relationship(
        back_populates='character_classes',
        secondary='refspellcharacterclass',
    )
