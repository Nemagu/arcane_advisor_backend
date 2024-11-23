from .base_models import Description, IdEditedBy, UniqueName


class DamegeType(IdEditedBy, UniqueName, Description, table=True):
    pass
