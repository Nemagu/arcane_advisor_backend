from .base_models import Description, IdEditedBy, UniqueName


class SpellSchool(IdEditedBy, UniqueName, Description, table=True):
    pass
