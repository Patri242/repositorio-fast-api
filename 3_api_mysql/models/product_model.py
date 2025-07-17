from pydantic import BaseModel



class Product(BaseModel):
    id:int
    title:str
    price:float
    quantity:int
    status:int

class ProductCreate(BaseModel): #especifico del propio framework. como funciona FastApi
    title:str
    price:float
    quantity:int
    status:int