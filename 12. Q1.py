'''Write a program to create a class that represents Complex numbers containing
real and imaginary parts and then use it to perform complex number addition,
subtraction, multiplication and division.'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def divide(self, other):
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            return "Division by zero is not allowed."
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

# Example usage:
c1 = Complex(4, 5)
c2 = Complex(2, 3)

print("c1 =", c1)
print("c2 =", c2)
print("Addition:", c1.add(c2))
print("Subtraction:", c1.subtract(c2))
print("Multiplication:", c1.multiply(c2))
print("Division:", c1.divide(c2))
