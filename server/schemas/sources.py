from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import Spell


class SourceDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class SourceRefAllDTO(SourceDTO):
    spells: list['Spell']
