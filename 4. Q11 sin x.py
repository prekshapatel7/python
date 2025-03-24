import math

n1 = float(input("Enter the value of x in degrees: "))
n2 = math.radians(n1)  # Convert degrees to radians

terms = 10  # Number of terms to use in the series
sin_x = 0  # Initialize sum

for i in range(terms):
    term = ((-1) ** i) * (n2 ** (2 * i + 1)) / math.factorial(2 * i + 1)
    sin_x += term  # Accumulate sum

print(f"Approximated sin({n1}°) = {sin_x}")
print(f"math.sin({n1}°) = {math.sin(n2)}")  # Compare with built-in function


