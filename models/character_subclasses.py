from .base_models import Description, Id, UniqueName


class CharacterSubclass(Id, UniqueName, Description, table=True):
    pass
