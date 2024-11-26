from .base_models import Description, IdEditedBy, UniqueName


class SpellComponent(IdEditedBy, UniqueName, Description, table=True):
    pass
