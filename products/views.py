from typing import List

from fastapi import APIRouter, Depends

from products.models import ProductModel
from products.schemas import Product, ProductIn
from users.utils import get_current_user, get_admin_user

router = APIRouter()


@router.get("/", response_model=List[Product])
def list_products(user=Depends(get_current_user)):
    products = list(ProductModel.objects.all())
    return products


@router.post("/", response_model=Product)
def create_product(product_data: ProductIn, user=Depends(get_admin_user)):
    product_in_db = ProductModel.objects.create(**dict(product_data))
    return product_in_db
