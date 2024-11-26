from typing import Optional

from sqlmodel import Field

from .base_models import IdEditedBy


class SpellCharacterClassLink(IdEditedBy, table=True):
    character_class_id: Optional[int] = Field(
        default=None,
        foreign_key='character_class.id',
    )
    spell_id: Optional[int] = Field(
        default=None,
        foreign_key='spell.id',
    )
