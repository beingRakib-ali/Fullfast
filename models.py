from sqlalchemy import Column, Integer, Float,String,Boolean, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "user"
    UserID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String)
    Password = Column(String)

class Customer(Base):
    __tablename__ = "customer"
    CustomerID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Address = Column(String)
    Phone = Column(String)
    Email = Column(String)
    UserID = Column(Integer, ForeignKey("user.UserID"))