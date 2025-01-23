#. Calculate average of three subjects along with their total.
def avg():
    s1=int(input("enter the marks of subject 1"))
    s2=int(input("enter the marks of subject 2"))
    s3=int(input("enter the marks of subject 3"))
    avg=(s1+s2+s3)/3
    print("average is ",avg)
avg()
# Swap two values.
def swap():
    a=int(input("first value"))
    b=int(input("second value"))
    a,b=b,a
    print(a)
    print(b)
swap()               
            
