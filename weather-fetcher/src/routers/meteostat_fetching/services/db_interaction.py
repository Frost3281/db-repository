from typing import Sequence, cast

from sqlmodel import Session, select

from src.routers.meteostat_fetching.models.db import BristolStore


def fetch_stores_from_db(session: Session) -> Sequence[BristolStore]:
    """Получаем список магазинов."""
    return session.exec(select(BristolStore)).all()


def fetch_store_from_db(session: Session, store_id: int) -> BristolStore:
    """Получаем магазин."""
    store = session.get(BristolStore, store_id)
    if not store:
        msg = f'Магазин с ID = {store_id} не найден'
        raise ValueError(msg)
    return cast(BristolStore, store)
