import math

class Cylinder:
    def __init__(self):
        self.radius = 0
        self.height = 0

    def accept_data(self):
        self.radius = float(input("Enter the radius of the cylinder: "))
        self.height = float(input("Enter the height of the cylinder: "))

    def surface_area(self):
        sa = 2 * math.pi * self.radius * (self.radius + self.height)
        return sa

    def volume(self):
        vol = math.pi * self.radius ** 2 * self.height
        return vol

# Example usage:
cyl = Cylinder()
cyl.accept_data()

print(f"\nSurface Area of Cylinder: {cyl.surface_area():.2f}")
print(f"Volume of Cylinder: {cyl.volume():.2f}")
