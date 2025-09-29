from typing import Optional
from pydantic import BaseModel
from datetime import datetime


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
    username:str
    password:str
    class Config:
        orm_mode = True




class Login(BaseModel):
    # Name:str
    massage:str
    class Config:
        orm_mode = True



class Massage(BaseModel):
    massage:str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str 




class EmployeeBase(BaseModel):
    id: int
    extraID: int
    civilId: str
    nameArabic: str
    jobArabic: str
    companyArabic: str
    nationalityArabic: str
    categoryArabic: str
    issueDate: datetime
    endDate: datetime
    profilePhoto: str
    createdAt: Optional[datetime] = None  # optional, will default in SQLAlchemy


    class Config:
        orm_mode = True



class Message(BaseModel):
    message: str