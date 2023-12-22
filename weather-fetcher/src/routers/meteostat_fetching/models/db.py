from datetime import date
from typing import Union

from sqlmodel import Field, SQLModel

from src.routers.meteostat_fetching.models.data_structures import Point


class DailyWeather(SQLModel):
    """Дневные данные."""

    store_id: int
    day_date: date
    average_temperature: Union[float, None] = Field(default=None, alias='tavg')
    minimum_temperature: Union[float, None] = Field(default=None, alias='tmin')
    maximum_temperature: Union[float, None] = Field(default=None, alias='tmax')
    precipitation: Union[float, None] = Field(default=None, alias='prcp')
    snowfall: Union[float, None] = Field(default=None, alias='snow')
    wind_direction: Union[float, None] = Field(default=None, alias='wdir')
    wind_speed: Union[float, None] = Field(default=None, alias='wspd')
    peak_gust_wind_speed: Union[float, None] = Field(
        default=None,
        alias='wpgt',
    )
    pressure: Union[float, None] = Field(default=None, alias='pres')
    sunshine_duration: Union[float, None] = Field(default=None, alias='tsun')


class BristolStore(SQLModel, table=True):
    """Магазин."""

    __table_name__ = 'bristol_store'
    __table_args__ = {'schema': 'mgp_bristol'}

    store_id: int = Field(primary_key=True)
    latitude: float
    longitude: float

    def to_point(self) -> Point:
        """Получаем объект Point."""
        return Point(self.store_id, self.latitude, self.longitude)
