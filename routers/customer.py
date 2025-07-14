from fastapi import APIRouter,Depends,HTTPException,status
from typing import List,Annotated
from sqlalchemy.orm import Session
import repository.customer
import database,models,schemas,hasing,repository

db_dp = Annotated[Session,Depends(database.get_db)]


route = APIRouter(
    prefix="/customer",
    tags=["/Customer"]
)




@route.post('/',status_code=201,response_model=schemas.CustomerBase)
def create_customer(customer:schemas.CustomerBase,db:db_dp):
    return repository.customer.create_customer(customer,db)


@route.get("/",status_code=200,response_model=List[schemas.CustomerViewBase])
def get_customers(db:db_dp):
    return repository.customer.get_customers(db)


@route.get('/get_single/{id}',status_code=status.HTTP_200_OK,response_model=schemas.CustomerViewBase)
async def get_single_customer(id:int,db:db_dp):
    return repository.customer.get_single_customer(id,db)

@route.put('/update_customer/{customer_id}',status_code=status.HTTP_200_OK,response_model=schemas.CustomerBase)
async def update_customer(customer_id: int, customer:schemas.CustomerBase, db:db_dp):
    return repository.customer.update_customer(customer_id,customer,db)

@route.delete('/delete_customer/{id}',status_code=status.HTTP_200_OK,response_model=schemas.Massage)
async def delete_customer(customer_id:int,db:db_dp):
    return repository.customer.delete(customer_id,db)