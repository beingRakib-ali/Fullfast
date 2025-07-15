from fastapi import APIRouter,Depends,HTTPException,status
from typing import List,Annotated
from sqlalchemy.orm import Session
import repository.customer
import database,schemas,repository,oauth2

db_dp = Annotated[Session,Depends(database.get_db)]


get_current_user = Annotated[schemas.UserBase ,Depends(oauth2.get_current_user)]

route = APIRouter(
    prefix="/customer",
    tags=["/Customer"]
)



@route.post('/',status_code=201,response_model=schemas.CustomerBase)
def create_customer(customer:schemas.CustomerBase,db:db_dp,current_user:get_current_user):
    return repository.customer.create_customer(customer,db)


@route.get("/",status_code=200,response_model=List[schemas.CustomerViewBase])
def get_customers(db:db_dp,current_users:get_current_user,offset:int=0,limit:int=100):
    return repository.customer.get_customers(db,offset=offset,limit=limit)


@route.get('/get_single/{id}',status_code=status.HTTP_200_OK,response_model=schemas.CustomerViewBase)
async def get_single_customer(id:int,db:db_dp,current_user:get_current_user):
    return repository.customer.get_single_customer(id,db)

@route.put('/update_customer/{customer_id}',status_code=status.HTTP_200_OK,response_model=schemas.CustomerBase)
async def update_customer(customer_id: int, customer:schemas.CustomerBase, db:db_dp,current_user:get_current_user):
    return repository.customer.update_customer(customer_id,customer,db)

@route.delete('/delete_customer/{id}',status_code=status.HTTP_200_OK,response_model=schemas.Massage)
async def delete_customer(customer_id:int,db:db_dp,current_user:get_current_user):
    return repository.customer.delete(customer_id,db)