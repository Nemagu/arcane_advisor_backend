from .base_models import Description, IdEditedBy, UniqueName


class Source(IdEditedBy, UniqueName, Description, table=True):
    pass
