from .base_models import Description, Id, UnieqName


class CharacterClass(Id, UnieqName, Description, table=True):
    pass
