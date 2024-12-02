from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import Spell


class SpellSchoolDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class SpellSchoolRefAllDTO(SpellSchoolDTO):
    spells: list['Spell']
