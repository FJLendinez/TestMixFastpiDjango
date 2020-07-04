from typing import List

from fastapi import APIRouter

from products.models import ProductModel
from products.schemas import Product, ProductIn

router = APIRouter()


@router.get("/", response_model=List[Product])
def list_products():
    products = list(ProductModel.objects.all())
    return products

@router.post("/", response_model=Product)
def create_product(product_data: ProductIn):
    product_in_db = ProductModel.objects.create(**dict(product_data))
    return product_in_db

