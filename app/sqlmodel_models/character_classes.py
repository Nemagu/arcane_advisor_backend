from .base_models import Description, IdEditedBy, UniqueName


class CharacterClass(IdEditedBy, UniqueName, Description, table=True):
    pass
