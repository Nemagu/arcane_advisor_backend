from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import Spell


class TypeDamageDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class TypeDamageRefAllDTO(TypeDamageDTO):
    spells: list['Spell']
