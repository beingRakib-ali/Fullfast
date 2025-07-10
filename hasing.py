from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
  def get_pass_hash(password:str):
    return pwd_context.hash(password)
  
  def verify_password(plain_password:str, hashed:str):
    data = pwd_context.verify(plain_password,hashed)
    return data