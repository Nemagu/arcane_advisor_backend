from .base_models import Description, Id, UniqueName


class SpellComponent(Id, UniqueName, Description, table=True):
    pass
