from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from .base_models import Count, IdEditedBy

if TYPE_CHECKING:
    from .spells import Spell
    from .time_units import TimeUnit


class SpellCastingTime(IdEditedBy, Count, table=True):
    unit_time: 'TimeUnit' = Relationship(back_populates='spell_casting_times')
    unit_time_id: Optional[int] = Field(
        default=None,
        foreign_key='unit_time.id',
        title='Единица измерения времени',
        description='Единица измерения времени.',
    )
    spell: 'Spell' = Relationship(back_populates='spell_casting_times')
    spell_id: Optional[int] = Field(
        default=None,
        foreign_key='spell.id',
        title='Заклинание',
        description='Заклинание.',
    )
