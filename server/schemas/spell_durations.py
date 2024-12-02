from typing import TYPE_CHECKING

from .base_classes import IdDTO

if TYPE_CHECKING:
    from models import Spell, UnitDuration


class SpellDurationDTO(IdDTO):
    count: int


class SpellDurationRefAllDTO(SpellDurationDTO):
    unit_duration: 'UnitDuration'
    spell: 'Spell'
