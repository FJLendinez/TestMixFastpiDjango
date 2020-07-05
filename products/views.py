from typing import List

from fastapi import APIRouter

from ordermaker.db_sync import database_sync_to_async
from products.models import ProductModel
from products.schemas import Product, ProductIn

router = APIRouter()


@database_sync_to_async
def get_all():
    return list(ProductModel.objects.all())


@router.get("/", response_model=List[Product])
async def list_products():
    products = await get_all()
    return products


@database_sync_to_async
def create_product_in_db(product_data: ProductIn):
    product = ProductModel.objects.create(**dict(product_data))
    return product


@router.post("/", response_model=Product)
async def create_product(product_data: ProductIn):
    product_in_db = await create_product_in_db(product_data)
    return product_in_db
