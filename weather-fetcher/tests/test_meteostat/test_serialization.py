from datetime import datetime

import pandas as pd

from src.routers.meteostat_fetching.models.db import DailyWeather
from src.routers.meteostat_fetching.services.serialization import df_to_list_of_models

SAMPLE_DAILY_DATA = [
    {
        'tavg': 1.8,
        'tmin': -0.4,
        'tmax': 4.0,
        'prcp': 0.0,
        'snow': 0.0,
        'wdir': None,
        'wspd': 8.7,
        'wpgt': 0.0,
        'pres': 1030.7,
        'tsun': None,
    },
]


def test_serialization_to_model():
    """Проверка сериализации."""
    weather = DailyWeather(
        **SAMPLE_DAILY_DATA[0],
        store_id=1,
        day_date=datetime(2018, 1, 1),
    )
    assert weather.average_temperature == SAMPLE_DAILY_DATA[0]['tavg']
    assert weather.minimum_temperature == SAMPLE_DAILY_DATA[0]['tmin']


def test_serialization_from_df(meteostat_df: pd.DataFrame):
    """Проверка сериализации в список моделей."""
    daily_data_models = df_to_list_of_models(
        meteostat_df,
        DailyWeather,
        store_id=1,
    )
    assert isinstance(daily_data_models, list)
    assert len(daily_data_models) == 5
    assert daily_data_models[0].average_temperature == 1.8
