from typing import Protocol

from src.routers.meteostat_fetching.models.data_structures import Point


class Store(Protocol):
    """Магазин."""

    @property
    def store_id(self) -> int:
        """ID магазина."""

    @property
    def latitute(self) -> float:
        """Широта."""

    @property
    def longitude(self) -> float:
        """Долгота."""

    def to_point(self) -> Point:
        """Получаем объект Point."""
        return Point(self.store_id, self.latitute, self.longitude)
