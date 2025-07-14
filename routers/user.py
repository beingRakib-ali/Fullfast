from fastapi import APIRouter,Depends,HTTPException
from typing import List,Annotated
from sqlalchemy.orm import Session
import repository.user
import database,models,schemas,hasing
import repository

db_dp = Annotated[Session,Depends(database.get_db)]


route = APIRouter(
    prefix="/user",
    tags=["/Users"]
)




@route.post('/create', status_code=201,response_model=schemas.UserBase)
def create_user(user:schemas.UserBase,db:db_dp):
    return repository.user.create_user(user,db)
 

@route.post('/login',status_code=201,response_model=schemas.Login)
async def Login(user:schemas.LoginBase,db:db_dp):
    return repository.user.Login(user,db)


@route.get('/',status_code=200,response_model=List[schemas.UserBase])
def get_users(db:db_dp):
    return repository.user.get_all_users(db)
   

@route.get('/get_single_user', status_code=200,response_model=schemas.UserBase)
def get_single_user(id:int,db:db_dp):
    return repository.user.get_single_user(id,db)