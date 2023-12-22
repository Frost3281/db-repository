from typing import Any

from meteostat import Point as MeteoStatPoint
from pydantic import BaseModel


class Coordinates(BaseModel):
    """Координаты."""

    latitude: float
    longitude: float


class Point(MeteoStatPoint):
    """Point с добавленным ID магазина."""

    def __init__(self, store_id: int, *args: Any, **kwargs: Any) -> None:
        """Инициализация."""
        self.store_id = store_id
        super().__init__(*args, **kwargs)
