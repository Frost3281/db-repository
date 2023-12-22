from typing import Any, Type, TypeVar

import pandas as pd
from pydantic import BaseModel

T_Model = TypeVar('T_Model', bound=BaseModel)


def df_to_list_of_models(
    df_data: pd.DataFrame,
    model: Type[T_Model],
    **additional_model_kwargs: Any,
) -> list[T_Model]:
    """Преобразование датафрейма в список моделей."""
    return [
        model(**additional_model_kwargs, **row)
        for row in _convert_df_to_dict(
            run_meteostat_daily_df_preprocessing(df_data),
        )
    ]


def _convert_df_to_dict(df_data: pd.DataFrame) -> list[dict[str, Any]]:
    """Преобразование датафрейма в словарь."""
    return df_data.to_dict('records')


def run_meteostat_daily_df_preprocessing(
    df_data: pd.DataFrame,
) -> pd.DataFrame:
    """Препроцессинг датафрейма."""
    return df_data.pipe(_replace_nan_with_none).pipe(
        _set_index_date_column_to_df_column,
    )


def _replace_nan_with_none(df_data: pd.DataFrame) -> pd.DataFrame:
    return df_data.where((pd.notna(df_data)), None)


def _set_index_date_column_to_df_column(df_data: pd.DataFrame) -> pd.DataFrame:
    return df_data.reset_index().rename(columns={'time': 'day_date'})
