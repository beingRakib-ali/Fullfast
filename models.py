import datetime
from sqlalchemy import Column, DateTime, Integer, Float,String,Boolean, ForeignKey
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

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    extraID = Column(Integer, nullable=False)
    civilId = Column(Integer, unique=True, nullable=False)
    nameArabic = Column(String, nullable=False)
    jobArabic = Column(String, nullable=True)
    companyArabic = Column(String, nullable=True)
    nationalityArabic = Column(String, nullable=True)
    categoryArabic = Column(String, nullable=True)
    issueDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    profilePhoto = Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)