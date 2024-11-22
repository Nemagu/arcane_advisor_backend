from .base_models import Description, Id, UniqueName


class SpellSchool(Id, UniqueName, Description, table=True):
    pass
