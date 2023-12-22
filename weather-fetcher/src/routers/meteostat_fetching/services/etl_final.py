import asyncio

from src.routers.meteostat_fetching.models.request_settings import (
    ParseSettings,
)
from src.routers.meteostat_fetching.services.db_interaction import (
    fetch_stores_from_db,
)
from src.routers.meteostat_fetching.services.fetching import (
    parse_points_weather,
    stores_to_points,
)


def parse_weather_from_meteostat(parse_settings: ParseSettings) -> None:
    """Парсинг погоды с meteostat."""
    stores = fetch_stores_from_db()
    points = stores_to_points(stores)
    asyncio.run(
        parse_points_weather(
            points,
            parse_settings.date_from,
            parse_settings.date_to,
        ),
    )
