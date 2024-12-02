from .base_classes import CreatedAtUpdatedAtDTO, IdDTO, NameDescriptionDTO


class SpellComponentDTO(IdDTO, CreatedAtUpdatedAtDTO, NameDescriptionDTO):
    pass
