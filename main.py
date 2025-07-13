from fastapi import FastAPI
import models
from database import engine,get_db
from routers import user,customer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.route)
app.include_router(customer.route)


# @app.post('/user/', status_code=201,tags=['Users'],response_model=schemas.UserBase)
# def create_user(user:schemas.UserBase,db:db_dp):
    
#     user_dict = user.model_dump()
#     user_dict['Password'] = hasing.Hash.get_pass_hash(user.Password)

#     add_user = models.User(**user_dict)
    
#     db.add(add_user)
#     db.commit()
#     db.refresh(add_user)
#     return add_user


# @app.post('/login/',status_code=201,response_model=schemas.Login,tags=['Users'])
# async def Login(user:schemas.LoginBase,db:db_dp):

#     get_user = db.query(models.User).filter(models.User.Email == user.Email).first()

#     if get_user is None:
#         raise HTTPException(status_code=404,detail="User Not Found!")
    
#     valid = hasing.Hash.verify_password(user.Password,get_user.Password)
#     if not valid:
#         raise HTTPException(status_code=401, detail="Password Incorrect")
#     return {"Massage":"Successfully Login"}


# @app.get('/users/main',status_code=200,response_model=List[schemas.UserBase],tags=['Users'])
# def get_users(db:db_dp):
#     get_user = db.query(models.User).all()
#     return get_user




# @app.post('/customer/',status_code=201,response_model=schemas.ShowUser)
# def create_customer(customer:schemas.CustomerBase,db:db_dp):
#     addcs = models.Customer(**customer.model_dump())
#     db.add(addcs)
#     db.commit()
#     db.refresh(addcs)
#     return addcs

