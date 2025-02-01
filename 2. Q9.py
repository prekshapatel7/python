#Print absolute value of a given number.
def absolute():
    a=int(input("enter the number"))
    if a<0:
        a=a*(-1)
        print("absolute value is",a)
    else :
        print("absolute value is",a)
absolute()
