#Print a multiplication table of a given number.
def table():
    n=int(input("enter the number whose table you want" ))
    for i in range(1,10):
        a=i*n
        print(a)
table()                
