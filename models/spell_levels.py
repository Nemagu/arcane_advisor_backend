from sqlmodel import Field

from .base_models import Description, Id
from .consts import MAX_VALUE_SPELL_LEVEL, MIN_VALUE_SPELL_LEVEL


class SpellLevel(Id, Description, table=True):
    level: int = Field(
        min_length=MIN_VALUE_SPELL_LEVEL,
        max_length=MAX_VALUE_SPELL_LEVEL,
        title='Уровень заклинания',
        description='Уровень заклинания.',
    )
