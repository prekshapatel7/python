#. Calculate net salary,where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary.
def netsalary():
    grosssalary=float(input("enter the gross salarry"))
    allowance=float(input("enter the allowance"))
    deduction=float(input("enter the gross deduction"))
    netsalary=grosssalary+allowance-deduction
    print("the net salary is",netsalary)
netsalary()

    
