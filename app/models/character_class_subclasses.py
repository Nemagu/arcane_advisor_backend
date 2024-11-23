from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from .base_models import IdEditedBy

if TYPE_CHECKING:
    from .character_classes import CharacterClass
    from .character_subclasses import CharacterSubclass


class CharacterClassSubclass(IdEditedBy, table=True):
    character_class: 'CharacterClass' = Relationship(
        back_populates='character_classes'
    )
    character_class_id: Optional[int] = Field(
        default=None,
        foreign_key='character_class.id',
    )

    character_subclass: Optional['CharacterSubclass'] = Relationship(
        back_populates='character_subclasses'
    )
    character_subclass_id: Optional[int] = Field(
        default=None,
        foreign_key='character_subclass.id',
    )
