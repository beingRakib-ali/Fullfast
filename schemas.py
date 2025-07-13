from pydantic import BaseModel
import models
from database import Base



class UserBase(BaseModel):
   
    Name:str
    Email:str
    Password:str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    Name:str
    Email:str
    # Password:str
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
   
    Name: str
    Address: str
    Phone:str
    Email: str
    # Creator:ShowUser
    # class Config:
    #     orm_mode = True

class CustomerViewBase(BaseModel):
   
    Name: str
    Address: str
    Phone:str
    Email: str
    # Creator:ShowUser
    class Config:
        orm_mode = True

class LoginBase(BaseModel):
    # Name:str
    Email:str
    Password:str
    class Config:
        orm_mode = True





class Login(BaseModel):
    # Name:str
    Massage:str
    class Config:
        orm_mode = True