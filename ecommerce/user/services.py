from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models
from . import schema


async def new_user_register(request: schema.User, database: Session) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database: Session) -> List[models.User]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id: int, database: Session) -> Optional[models.User]:
    user = database.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id: {user_id}")
    return user


async def delete_user_by_id(user_id: int, database: Session):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
