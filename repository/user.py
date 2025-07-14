from fastapi import HTTPException,status
import database,models,schemas,hasing


def get_all_users(db):
    get_user = db.query(models.User).all()
    return get_user

def get_single_user(id,db):
    get_user = db.query(models.User).filter(models.User.UserID == id).first()
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User Not found with id {id}")
    return get_user


def create_user(user,db):
    user_dict = user.model_dump()
    user_dict['Password'] = hasing.Hash.get_pass_hash(user.Password)
    add_user = models.User(**user_dict)
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user


def Login(user,db):
    get_user = db.query(models.User).filter(models.User.Email == user.Email).first()
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found!")
    valid = hasing.Hash.verify_password(user.Password,get_user.Password)
    if not valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password Incorrect")
    return {"massage":"Successfully Login"}