from .base_models import Description, Id, UnieqName


class CharacterSubclass(Id, UnieqName, Description, table=True):
    pass
