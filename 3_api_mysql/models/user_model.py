from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    email:EmailStr
    register_date: Optional[datetime]=None
    status:int
    password:str
    rol: str


class UserCreate(BaseModel):
    name:str
    surname:str
    age:int
    email:EmailStr
    password:str
    rol: str