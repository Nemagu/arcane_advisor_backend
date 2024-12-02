from typing import TYPE_CHECKING

from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO

if TYPE_CHECKING:
    from models import CharacterSubclass


class CharacterClassDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass


class CharacterClassRefAllDTO(CharacterClassDTO):
    combination_character_class_subclass: list['CharacterSubclass']
