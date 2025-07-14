from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import Session
import schemas,models,hasing
from JWTtoken import create_access_token
from database import get_db

route = APIRouter(
    prefix=('/login'),
    tags=['Authenticate']
)

db_dp = Annotated[Session,Depends(get_db)]


@route.post('/',status_code=201,response_model=schemas.Token)
async def Login(db: db_dp, user: OAuth2PasswordRequestForm=Depends()):
    get_user = db.query(models.User).filter(models.User.Email == user.username).first()
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found!")
    valid = hasing.Hash.verify_password(user.password,get_user.Password)
    if not valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password Incorrect")
    
    access_token = create_access_token(data={"sub": user.username})

    return {"access_token":access_token, "token_type":"bearer"}