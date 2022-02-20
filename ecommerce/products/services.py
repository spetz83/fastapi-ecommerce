from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models
from . import schema


async def create_new_category(request: schema.Category, database: Session) -> models.Category:
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def get_all_categories(database: Session) -> List[models.Category]:
    categories = database.query(models.Category).all()
    return categories


async def get_category_by_id(category_id: int, database: Session) -> models.Category:
    category = database.query(models.Category).get(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found.")
    return category


async def delete_category_by_id(category_id: int, database: Session):
    database.query(models.Category).filter(models.Category.id == category_id).delete()
    database.commit()


async def create_new_product(request: schema.Product, database: Session) -> models.Product:
    new_product = models.Product(
        name=request.name,
        quantity=request.quantity,
        description=request.description,
        price=request.price,
        category_id=request.category_id,
    )
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database: Session) -> List[models.Product]:
    products = database.query(models.Product).all()
    return products


async def get_product_by_id(product_id: int, database: Session) -> models.Category:
    product = database.query(models.Product).get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found.")
    return product


async def delete_product_by_id(product_id: int, database: Session):
    database.query(models.Product).filter(models.Product.id == product_id).delete()
    database.commit()
