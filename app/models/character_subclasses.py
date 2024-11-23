from .base_models import Description, IdEditedBy, UniqueName


class CharacterSubclass(IdEditedBy, UniqueName, Description, table=True):
    pass
