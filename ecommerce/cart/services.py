from operator import and_
from fastapi import HTTPException, status, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.cart import schema
from ecommerce.products.models import Product
from ecommerce.user.models import User
from .models import Cart, CartItems


async def add_to_cart(product_id: int, database: Session):
    product = database.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    if product.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item out of stock.")

    user = database.query(User).filter(User.email == "derp@derp.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user.id).first()

    if not cart:
        new_cart = Cart(user_id=user.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(cart.id, product_id, database)
    else:
        await add_items(cart.id, product_id, database)
    return {"status": "Item added to cart"}


async def add_items(cart_id: int, product_id: int, database: Session):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def get_all_items(database: Session) -> schema.ShowCart:
    user = database.query(User).filter(User.email == "derp@derp.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user.id).first()
    return cart


async def remove_cart_item(cart_item_id: int, database: Session) -> None:
    user = database.query(User).filter(User.email == "derp@derp.com").first()
    cart = database.query(Cart).filter(User.id == user.id).first()
    database.query(CartItems).filter(and_(CartItems.id == cart_item_id, CartItems.cart_id == cart.id)).delete()
    database.commit()
    return
