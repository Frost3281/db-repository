from typing import Iterator

import pandas as pd
import pytest
from sqlalchemy import StaticPool, text
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(
    'sqlite://',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
    future=True,
)


@pytest.fixture(name='db_session', scope='session')
def db_session_fixture() -> Iterator[Session]:
    """Сессия для тестов."""
    with Session(engine) as session:
        session.execute(text("ATTACH DATABASE ':memory:' AS brl_apex;"))
        for table_metadata in SQLModel.metadata.tables.values():
            table_metadata.schema = 'brl_apex'
        SQLModel.metadata.create_all(engine)
        yield session


@pytest.fixture(name='meteostat_df')
def meteostat_df_sample() -> pd.DataFrame:
    """Датафрейм."""
    data = {
        'time': [
            '2018-01-01',
            '2018-01-02',
            '2018-01-03',
            '2018-01-04',
            '2018-01-05',
        ],
        'tavg': [1.8, 1.8, 2.3, 4.1, 7.6],
        'tmin': [-0.4, -0.4, 1.2, 1.6, 5.7],
        'tmax': [4.0, 3.9, 3.4, 6.6, 9.5],
        'prcp': [0.0, 0.0, 0.0, 0.0, 30.4],
        'snow': [0.0, 0.0, None, 0.0, 0.0],
        'wdir': [None, None, None, None, None],
        'wspd': [8.7, 7.1, 6.8, 6.1, 10.0],
        'wpgt': [0.0, 0.0, 0.0, 0.0, 0.0],
        'pres': [1030.7, 1028.5, 1022.5, 1016.7, 1014.5],
        'tsun': [None, None, None, None, None],
    }
    df_data = pd.DataFrame(data)
    df_data['time'] = pd.to_datetime(df_data['time'])
    return df_data.set_index('time')
