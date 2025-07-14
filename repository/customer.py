from fastapi import HTTPException,Depends,status
import models



def create_customer(customer,db):
    addcs = models.Customer(**customer.model_dump())
    db.add(addcs)
    db.commit()
    db.refresh(addcs)
    return addcs

def get_customers(db):
    data = db.query(models.Customer).all()
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found!")
    return data

def get_single_customer(id,db):
    customer = db.query(models.Customer).filter(models.Customer.CustomerID == id).first()
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"customer with id {id} not found!")
    return customer

def update_customer(customer_id,cs,db):
    customer = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"customer with id {id} not found!")
    
    for key,value in cs.model_dump().items():
        setattr(customer,key,value)
    db.commit()
    db.refresh(customer)
    return customer



def delete(customer_id,db):
    customer = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"customer with id {id} not found!")
    db.delete(customer)
    db.commit()
    return {'massage':'Delete Successfully!'}
