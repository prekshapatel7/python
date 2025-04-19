#Create a dictionary with dept no, employee roll no. and salary.
#Find out department wise min and maximum of salary.
# Dictionary format: {emp_roll_no: (dept_no, salary)}
employee_data = {
    'E001': (101, 45000),
    'E002': (101, 52000),
    'E003': (102, 48000),
    'E004': (102, 61000),
    'E005': (103, 39000),
    'E006': (103, 47000),
}

# Create a new dictionary to hold department-wise salaries
dept_salaries = {}

for emp_id, (dept_no, salary) in employee_data.items():
    if dept_no not in dept_salaries:
        dept_salaries[dept_no] = []
    dept_salaries[dept_no].append(salary)

# Display the min and max salary for each department
print("Department-wise Min and Max Salaries:\n")
for dept_no, salaries in dept_salaries.items():
    print(f"Department {dept_no}: Min = {min(salaries)}, Max = {max(salaries)}")
