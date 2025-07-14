from fastapi.security import OAuth2PasswordBearer
# from fastapi.security import APIKeyHeader
from fastapi import Depends,HTTPException,status
from typing import Annotated
from routers.authenticate import db_dp
import JWTtoken,models


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# oauth2_scheme = APIKeyHeader(name="Authorization")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db:db_dp):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_data = JWTtoken.Verify_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.Email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

