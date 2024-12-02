from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import CharacterClass


class CharacterSubclassDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class CharacterSubclassRefAllDTO(CharacterSubclassDTO):
    character_class: 'CharacterClass'
