from pydantic import BaseModel

class EmployeesModel(BaseModel):
    roleType: str
    name: str
    address: str
    email: str
    mobileNumber: str
    dob: str
    password: str
    gender: str

class EmployeeSignIn(BaseModel):
    email: str
    password: str