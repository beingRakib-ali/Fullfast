from fastapi import HTTPException, status
import models


def create_employee(employee, db):
    addemp = models.Employee(**employee.dict())
    db.add(addemp)
    db.commit()
    db.refresh(addemp)
    return addemp

def get_employees(db, offset: int, limit: int):
    return db.query(models.Employee).offset(offset).limit(limit).all()

def get_single_employee(id: str, db):
    employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {id} not found")
    return employee

def update_employee(employee_id: str, emp, db):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {employee_id} not found")

    for key, value in emp.dict().items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(employee_id: str, db):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {employee_id} not found")
    db.delete(employee)
    db.commit()
    return {"message": "Deleted successfully"}






# def create_employee(employee,db):
#     addemp = models.Employee(**employee.model_dump())
#     db.add(addemp)
#     db.commit()
#     db.refresh(addemp)
#     return addemp

# def get_employees(db,offset,limit):
#     if offset < 0 or limit <= 0 or limit > 1000:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Offset and limit must be positive integers and less then 1000.")

#     data = db.query(models.Employee).offset(offset).limit(limit).all()
#     if data is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found!")
#     return data

# def get_single_employee(id,db):
#     employee = db.query(models.Employee).filter(models.Employee.id == id).first()
#     if employee is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"employee with id {id} not found!")
#     return employee

# def update_employee(employee_id,emp,db):
#     employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
#     if employee is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"employee with id {id} not found!")
    
#     for key,value in emp.model_dump().items():
#         setattr(employee,key,value)
#     db.commit()
#     db.refresh(employee)
#     return employee

# def delete(employee_id,db):
#     employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
#     if employee is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"employee with id {id} not found!")
#     db.delete(employee)
#     db.commit()
#     return {'massage':'Delete Successfully!'}