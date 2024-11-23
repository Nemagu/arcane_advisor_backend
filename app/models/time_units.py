from .base_models import IdEditedBy, UniqueName


class TimeUnit(IdEditedBy, UniqueName, table=True):
    pass
