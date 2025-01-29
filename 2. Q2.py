#Print largest and smallest values out of three.
def compare():
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=int(input("enter the third number"))
    if a>b and a>c:
        print("the largest is ",a)
    elif b>c and b>a:
        print("the largest is ",b)
    else:
        print("the largest is",c)
compare()
