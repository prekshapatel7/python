#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.
#A triangle is valid if the sum of all the three angles is equal to 180 degrees
def triangle():
    a=float(input("enter the first angle"))
    b=float(input("enter the second angle"))
    c=float(input("enter the third angle"))
    sum= a+b+c
    if sum==180:
        print("valid")
    else:
        print("not valid triangle")
triangle()
