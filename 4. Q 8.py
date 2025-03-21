#Print factorial of a given number.
def fact():
    n=int(input("enter the number"))
    a=1
    for i in range (1,n+1):
        a=a*i

    print("the factorial of the number is",a)
fact()
