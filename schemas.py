from pydantic import BaseModel



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
    massage:str
    class Config:
        orm_mode = True



class Massage(BaseModel):
    massage:str
    class Config:
        orm_mode = True