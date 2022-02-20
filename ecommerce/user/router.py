from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=["Users"], prefix="/user")


@router.get("/", response_model=List[schema.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.all_users(database)


@router.get("/{user_id}", response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(status_code=400, detail=f"A user with the email address {request.email} already exists.")

    new_user = await services.new_user_register(request, database)
    return new_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_by_user_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_user_by_id(user_id, database)