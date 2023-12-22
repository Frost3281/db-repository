import asyncio
from datetime import datetime
from typing import Sequence

import pandas as pd
from meteostat import Daily

from src.routers.meteostat_fetching.models.data_structures import Point
from src.routers.meteostat_fetching.models.protocols import Store


async def parse_points_weather(
    points: list[Point],
    date_from: datetime,
    date_to: datetime,
) -> list[pd.DataFrame]:
    """Парсим погоду по точкам."""
    return await asyncio.gather(
        *[
            asyncio.to_thread(
                fetch_store_data_from_meteostat,
                point,
                date_from,
                date_to,
            )
            for point in points
        ],
    )


def stores_to_points(stores: Sequence[Store]) -> list[Point]:
    """Получаем список Point для дальнейшего парсинга."""
    return [store.to_point() for store in stores]


def fetch_store_data_from_meteostat(
    point: Point,
    date_from: datetime,
    date_to: datetime,
) -> pd.DataFrame:
    """Получаем датафрейм с данными метеостата по одной ТТ."""
    return Daily(point, date_from, date_to).fetch()
