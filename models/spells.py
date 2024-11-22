from sqlmodel import Field

from .base_models import Description, Id, UniqueName
from .consts import MIN_VALUE_SPELL_CASTING_TIME, MIN_VALUE_SPELL_RANGE


class Spell(Id, Description, UniqueName, table=True):
    # Уточнить у Дениса
    casting_time: int = Field(
        min_items=MIN_VALUE_SPELL_CASTING_TIME,
        title='Заклинания',
        description='Заклинания D&D.',
    )
    spell_range: int = Field(
        min_length=MIN_VALUE_SPELL_RANGE,
        title='Дальность',
        description='Дальность заклинания.',
    )
    next_level: str | None = Field(
        default=None,
        title='Бафы для сдующего уровня',
        description=(
            'Бафы использования заклинания при использовании ячейки '
            'следующего уровня.'
        ),
    )
    ritual: bool | None = Field(
        default=False,
        title='Ритуал',
        description='Нужно ли производить для заклинания ритуал.',
    )
    concentration: bool | None = Field(
        default=False,
        title='Концентрация',
        description='Требуется для заклинания концентрация.',
    )
