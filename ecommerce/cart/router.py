from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ecommerce import db
from .schema import ShowCart
from .services import add_to_cart, get_all_items, remove_cart_item

router = APIRouter(tags=["Cart"], prefix="/cart")


@router.get("/", response_model=ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db)):
    result = await get_all_items(database)
    return result


@router.get("/add", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, database: Session = Depends(db.get_db)):
    result = await add_to_cart(product_id, database)
    return result


@router.delete("/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int, database: Session = Depends(db.get_db)):
    await remove_cart_item(cart_item_id, database)
