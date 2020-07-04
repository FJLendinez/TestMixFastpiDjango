from typing import List

from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str


class Product(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True