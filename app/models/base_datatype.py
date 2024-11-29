import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

primaryk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text('TIMEZONE(\'utc\', now())'),
)]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text('TIMEZONE(\'utc\', now())'),
    onupdate=datetime.datetime.utcnow,
)]

unique_name_60 = Annotated[str, mapped_column(
    unique=True,
)]
