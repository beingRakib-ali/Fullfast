from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
import schemas


SECRET_KEY = "f3b870eb448a15ac6b3b9506b681f3e5f866874e9a3d709d56f6a1702801dbb1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def Verify_token(token,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
