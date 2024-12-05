import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text('TIMEZONE(\'utc\', now())'),
        # server_default=func.now(),

    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text('TIMEZONE(\'utc\', now())'),
        onupdate=datetime.datetime.utcnow,
    )
