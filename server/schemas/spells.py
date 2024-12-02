from typing import TYPE_CHECKING, Optional

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import (
        Source,
        SpellCastingTime,
        SpellComponent,
        SpellDuration,
        SpellLevel,
        SpellSchool,
        TypeDamage
    )


class SpellDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    range: int
    next_level: Optional[str]
    ritual: bool
    concetration: bool


class SpellRefAllDTO(SpellDTO):
    school: 'SpellSchool'
    level: 'SpellLevel'
    type_damage: 'TypeDamage'
    source: 'Source'
    duration: 'SpellDuration'
    casting_time: 'SpellCastingTime'
