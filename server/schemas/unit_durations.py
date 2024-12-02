from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDTO

if TYPE_CHECKING:
    from models import SpellCastingTime, SpellDuration


class UnitDurationDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDTO):
    pass


class UnitDurationRefAllDTO(UnitDurationDTO):
    spell_durations: list['SpellDuration']
    spell_casting_times: list['SpellCastingTime']
