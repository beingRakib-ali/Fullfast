
from fastapi import APIRouter,Depends,HTTPException
from typing import List,Annotated
from sqlalchemy.orm import Session
import database,models,schemas,hasing

db_dp = Annotated[Session,Depends(database.get_db)]


route = APIRouter(
    prefix="/customer",
    tags=["/Customer"]
)




@route.post('/',status_code=201,response_model=schemas.CustomerBase)
def create_customer(customer:schemas.CustomerBase,db:db_dp):
    addcs = models.Customer(**customer.model_dump())
    db.add(addcs)
    db.commit()
    db.refresh(addcs)
    return addcs


@route.get("/",status_code=200,response_model=List[schemas.CustomerViewBase])
def get_customers(db:db_dp):
    data = db.query(models.Customer).all()
    return data

