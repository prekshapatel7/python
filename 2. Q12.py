'''Given the coordinates (x,y) of center of a circle and its radius,
determine whether a point lies inside the circle, on the circle or outside
the circle. (Hint: Use sqrt( ), pow( ) )'''
import math

# Circle center and radius
x_center = float(input("Enter x coordinate of circle center: "))
y_center = float(input("Enter y coordinate of circle center: "))
radius = float(input("Enter radius of the circle: "))

# Point coordinates
x_point = float(input("Enter x coordinate of the point: "))
y_point = float(input("Enter y coordinate of the point: "))

# Calculate distance between point and center
distance = math.sqrt(math.pow(x_point - x_center, 2) + math.pow(y_point - y_center, 2))

# Compare with radius
if distance < radius:
    print("The point lies inside the circle.")
elif distance == radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
