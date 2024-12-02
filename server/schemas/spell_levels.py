from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, DescriptionDTO, IdDTO

if TYPE_CHECKING:
    from models import Spell


class SpellLevelDTO(IdDTO, CreatedAtUpdatedAtDTO, DescriptionDTO):
    level: int


class SpellLevelRefAllDTO(SpellLevelDTO):
    spells: list['Spell']
