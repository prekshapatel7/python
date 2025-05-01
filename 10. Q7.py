'''If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data.'''
import pickle
from datetime import datetime

class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def __str__(self):
        return f"EmpCode: {self.empcode}, EmpName: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"

# Serialization (Saving the Employee object)
def serialize_employee(emp, filename="employee.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(emp, file)
    print("Employee object serialized and saved.")

# Deserialization (Loading the Employee object)
def deserialize_employee(filename="employee.pkl"):
    with open(filename, "rb") as file:
        emp = pickle.load(file)
    return emp

# Example: Creating an Employee object
emp1 = Employee(
    empcode="E001", 
    empname="John Doe", 
    date_of_joining=datetime(2020, 5, 1),  # Date of Joining
    salary=50000
)

# Serialize the employee
serialize_employee(emp1)

# Deserialize the employee and display
emp_from_file = deserialize_employee()
print("Deserialized Employee Data:", emp_from_file)
