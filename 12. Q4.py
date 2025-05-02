import math

class Shape:
    def __init__(self):
        self.shape = None

    def input_data(self):
        self.shape = input("Enter shape (square/rectangle/circle/triangle): ").lower()

        if self.shape == "square":
            self.side = float(input("Enter side length of the square: "))

        elif self.shape == "rectangle":
            self.length = float(input("Enter length of the rectangle: "))
            self.breadth = float(input("Enter breadth of the rectangle: "))

        elif self.shape == "circle":
            self.radius = float(input("Enter radius of the circle: "))

        elif self.shape == "triangle":
            self.side = float(input("Enter side length of the equilateral triangle: "))

        else:
            print("Unsupported shape")

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.side
        elif self.shape == "rectangle":
            return 2 * (self.length + self.breadth)
        elif self.shape == "circle":
            return 2 * math.pi * self.radius
        elif self.shape == "triangle":
            return 3 * self.side
        else:
            return None

    def area(self):
        if self.shape == "square":
            return self.side ** 2
        elif self.shape == "rectangle":
            return self.length * self.breadth
        elif self.shape == "circle":
            return math.pi * self.radius ** 2
        elif self.shape == "triangle":
            return (math.sqrt(3) / 4) * self.side ** 2
        else:
            return None

# Example usage
shape = Shape()
shape.input_data()

p = shape.perimeter()
a = shape.area()

if p is not None and a is not None:
    print(f"Perimeter/Circumference = {p:.2f}")
    print(f"Area = {a:.2f}")
else:
    print("Calculation could not be performed.")
