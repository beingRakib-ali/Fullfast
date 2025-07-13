from sqlalchemy import Column, Integer, Float,String,Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import Relationship

class User(Base):
    __tablename__ = "user"
    UserID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String)
    Password = Column(String)
    # CustomerID = Column(Integer,ForeignKey("Customer.CustomerID"))
    # creator = Relationship("User",back_populates="Customer")


class Customer(Base):
    __tablename__ = "customer"
    CustomerID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Address = Column(String)
    Phone = Column(String)
    Email = Column(String)
    # UserID = Column(Integer, ForeignKey("user.UserID"))
    # creator = Relationship("User",back_populates="Customer")