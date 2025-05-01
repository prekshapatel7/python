'''Define three functions fun(), disp() and msg().
Store them in a list and call them one by one in a loop'''
# Define the functions
def fun():
    print("This is function fun()")

def disp():
    print("This is function disp()")

def msg():
    print("This is function msg()")

# Store the functions in a list
functions = [fun, disp, msg]

# Call each function in a loop
for f in functions:
    f()
