from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)

if TYPE_CHECKING:
    from .character_classes import CharacterClass
    from .spells import Spell


class CharacterSubclass(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    character_class_id: Mapped[int] = mapped_column(
        ForeignKey('characterclass.id', ondelete='CASCADE'),
    )
    character_class: Mapped['CharacterClass'] = relationship(
        back_populates='character_subclasses',
    )
    spells: Mapped[list['Spell']] = relationship(
        back_populates='character_subclasses',
        secondary='refspellcharactersubclass',
    )
