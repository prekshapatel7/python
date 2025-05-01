'''Read the data stored in MS-Excel file and convert it into a dictionary.
The record contains rollno, name of student, marks of three subjects. Also
calculate total. Display the dictionary data on the monitor.'''
import openpyxl

# Load the Excel workbook and sheet
wb = openpyxl.load_workbook("students.xlsx")
sheet = wb.active

# Dictionary to store data
students_data = {}

# Skip the header row and iterate through the rest
for row in sheet.iter_rows(min_row=2, values_only=True):
    rollno, name, sub1, sub2, sub3 = row
    total = sub1 + sub2 + sub3
    students_data[rollno] = {
        "name": name,
        "sub1": sub1,
        "sub2": sub2,
        "sub3": sub3,
        "total": total
    }

# Display the dictionary
for roll, data in students_data.items():
    print(f"Roll No: {roll}, Name: {data['name']}, Marks: {data['sub1']}, {data['sub2']}, {data['sub3']}, Total: {data['total']}")
