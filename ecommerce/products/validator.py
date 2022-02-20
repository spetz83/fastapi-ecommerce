from typing import Optional

from sqlalchemy.orm import Session
from .models import Category


async def verify_category_exist(category_id: int, database: Session) -> Optional[Category]:
    return database.query(Category).filter(Category.id == category_id).first()
