from fastapi import APIRouter,Depends,HTTPException
from typing import List,Annotated
from sqlalchemy.orm import Session
import database,models,schemas,hasing

db_dp = Annotated[Session,Depends(database.get_db)]


route = APIRouter(
    prefix="/user",
    tags=["/Users"]
)




@route.post('/', status_code=201,response_model=schemas.UserBase)
def create_user(user:schemas.UserBase,db:db_dp):
    
    user_dict = user.model_dump()
    user_dict['Password'] = hasing.Hash.get_pass_hash(user.Password)

    add_user = models.User(**user_dict)
    
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user






@route.post('/',status_code=201,response_model=schemas.Login)
async def Login(user:schemas.LoginBase,db:db_dp):

    get_user = db.query(models.User).filter(models.User.Email == user.Email).first()

    if get_user is None:
        raise HTTPException(status_code=404,detail="User Not Found!")
    
    valid = hasing.Hash.verify_password(user.Password,get_user.Password)
    if not valid:
        raise HTTPException(status_code=401, detail="Password Incorrect")
    return {"Massage":"Successfully Login"}




@route.get('/',status_code=200,response_model=List[schemas.UserBase])
def get_users(db:db_dp):
    get_user = db.query(models.User).all()
    return get_user
