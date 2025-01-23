#Calculate area of a circle. A = 22/7 * R * R
# Calculate area of a triangle. A = H*L/2
#question 19,20
def area_circle():
    r=float(input("enter the radius of circle"))
    area=22/7*r*r
    print("the area of circle is", area)
area_circle()
def area_triangle():
    h=int(input("height"))
    l=int(input("length"))
    area=h*l*0.5
    print("area",area)
area_triangle()

    

