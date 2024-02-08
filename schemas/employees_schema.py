def individual_serial_employees(employees: dict) -> dict:
    return {
        "id": str(employees["_id"]),
        "roleType": employees["roleType"],
        "name": employees["name"],
        "address": employees["address"],
        "email": employees["email"],
        "mobileNumber": employees["mobileNumber"],
        "dob": employees["dob"],
        "password": employees["password"],
        "gender": employees["gender"],
    }

def list_serial_employees(employees) -> list:
    return [individual_serial_employees(employee) for employee in employees]
