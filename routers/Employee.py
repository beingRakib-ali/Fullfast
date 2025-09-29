from fastapi import APIRouter,Depends,HTTPException,status
from typing import List,Annotated
from sqlalchemy.orm import Session
import repository.Employee
import database,schemas,repository,oauth2

# db_dp = Annotated[Session,Depends(database.get_db)]


# get_current_user = Annotated[schemas.UserBase ,Depends(oauth2.get_current_user)]

route = APIRouter(
    prefix="/employee",
    tags=["/employee"]
)
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import repository.Employee as employee_repo
import database, schemas

route = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@route.post("/", response_model=schemas.EmployeeBase)
def create_employee(employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    return employee_repo.create_employee(employee, db)

@route.get("/", response_model=List[schemas.EmployeeBase])
def get_employees(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return employee_repo.get_employees(db, offset, limit)

@route.get("/{id}", response_model=schemas.EmployeeBase)
def get_single_employee(id: str, db: Session = Depends(get_db)):
    return employee_repo.get_single_employee(id, db)

@route.put("/{employee_id}", response_model=schemas.EmployeeBase)
def update_employee(employee_id: str, employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    return employee_repo.update_employee(employee_id, employee, db)

@route.delete("/{employee_id}", response_model=schemas.Message)
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    return employee_repo.delete_employee(employee_id, db)
