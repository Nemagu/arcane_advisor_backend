from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import CharacterSubclass

    from .character_subclasses import CharacterSubclassDTO


class CharacterSubclassDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class CharacterClassDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class CharacterClassRefAllDTO(CharacterClassDTO):
    character_subclasses: list['CharacterSubclassDTO']
