#Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter.
def find():
    l=40
    b=10
    area=l*b
    perimeter = 2*(l+b)
    if area>perimeter:
        print("area is greater than perimeter ")
    else:
        print("not")
find()
