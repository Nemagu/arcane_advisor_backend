from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from .base_models import IdEditedBy

if TYPE_CHECKING:
    from .spell_components import SpellComponent
    from .spells import Spell


class SpellComponentLink(IdEditedBy, table=True):
    spell: 'Spell' = Relationship(
        back_populates='spell_component_link'
    )
    spell_id: Optional[int] = Field(
        default=None,
        foreign_key='spell.id',
        primary_key=True,
    )
    component: 'SpellComponent' = Relationship(
        back_populates='spell_component_link'
    )
    component_id: Optional[int] = Field(
        default=None,
        foreign_key='component.id',
        primary_key=True,
    )
