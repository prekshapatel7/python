#Given three points (x1,y1), (x2,y2) and (x3,y3),
#check if all the three points fall on one straight line.
def points():
    x1=int(input("x1="))
    x2=int(input("x2="))
    x3=int(input("x3="))
    y1=int(input("y1="))
    y2=int(input("y2="))
    y3=int(input("y3="))

    a= (y2-y1)/(x2-x1)
    b=(y3-y2)/(x3-x2)
    if a==b:
        print("points lie on straight line")
    else:
        print("not")
points()
