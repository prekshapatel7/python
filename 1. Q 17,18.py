#Calculate area & perimeter of a square. A = L^2, P = 4L
# Calculate area & perimeter of a rectangle. A = L*B, P = 2 (L+B)
#question 17 and 18
def area_sq():
    s=int(input("enter the side of square"))
    area=s*s
    print("the area of sqaure is :",area)
area_sq()
def perimeter_sq():
    s=int(input("enter the value of side of square"))
    perimeter= 4*s
    print("perimeter=",perimeter)
perimeter_sq()
def area_rectangle():
    
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))

    area=b*l
    print("the area of rectangle is :",area)
area_rectangle()
def perimeter_rectangle():
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))

    perimeter= 2*(l+b)
    print("perimeter=",perimeter)
perimeter_rectangle()
