from datetime import datetime
from typing import Union

from pydantic import BaseModel


class ParseSettings(BaseModel):
    """Настройки парсинга."""

    date_from: datetime
    date_to: datetime
    store_id: Union[int, None] = None
