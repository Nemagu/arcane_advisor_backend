from .base_models import Description, Id, UniqueName


class CharacterClass(Id, UniqueName, Description, table=True):
    pass
