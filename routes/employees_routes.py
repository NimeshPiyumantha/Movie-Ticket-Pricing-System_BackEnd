from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from utils.encryption_decryption_password import encrypt_password,decrypt_password
from models.employees_model import EmployeeSignIn, EmployeesModel
from config.db import collection_employees
from schemas.employees_schema import list_serial_employees
from bson import ObjectId

# Load the environment variables

key = '-PlVfIZZ7NZd6crBkdYcqAP_XS4i0im2Euy04OjzXos='

employeesRouter = APIRouter()

# Get all employees
@employeesRouter.get("/employees")
async def get_all_employees():
    employees = list_serial_employees(collection_employees.find())
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")
    for employee in employees:
        try:
            decrypted_password = decrypt_password(employee['password'], key)
            employee['password'] = decrypted_password
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data":employees, "message": "Employee load successfully"})

# Add a new employees
@employeesRouter.post("/employees")
async def add_employee(employees: EmployeesModel):
    encrypted_password = encrypt_password(employees.password, key)
    employees.password = encrypted_password
    try:
        result = collection_employees.insert_one(dict(employees))
        if not result.inserted_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add employee")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Employee added successfully."
    }


# Get a employees by id
@employeesRouter.get("/employees/{id}")
async def get_employee_by_id(id):
    employee = list_serial_employees(collection_employees.find({"_id": ObjectId(id)}))
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    encrypted_password = employee[0]['password']
    try:
        decrypted_password = decrypt_password(encrypted_password, key)
        employee[0]['password'] = decrypted_password
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return employee

# Update a employees by id
@employeesRouter.put("/employees/{id}")
async def update_employee_by_id(id:str, employees: EmployeesModel):
    encrypted_password = encrypt_password(employees.password, key)
    employees.password = encrypted_password
    try:
        result = collection_employees.update_one({"_id": ObjectId(id)}, {"$set": dict(employees)})
        if not result.modified_count:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update employee")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Employee updated successfully."
    }

# Delete a employees by id
@employeesRouter.delete("/employees/{id}")
async def delete_employee_by_id(id):
    try:
        result = collection_employees.delete_one({"_id": ObjectId(id)})
        if not result.deleted_count:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete employee")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Employee deleted successfully."
    }

# Get an employee by email
@employeesRouter.post("/employees/signIn")

async def sign_in_employee(employee_signIn: EmployeeSignIn):
    email = employee_signIn.email
    password = employee_signIn.password

    employee = list_serial_employees(collection_employees.find({"email": email}))

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    encrypted_password = employee[0]['password']

    try:
        decrypted_password = decrypt_password(encrypted_password, key)
        if decrypted_password != password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        employee[0]['password'] = decrypted_password
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {
        "status": "OK",
        "message": "Employee signed in successfully.",
        "data": employee
    }