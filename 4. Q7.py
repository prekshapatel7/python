# Print nCr and nPr.

# Function to calculate factorial using a for loop
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Function to calculate nCr (Combinations)
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Function to calculate nPr (Permutations)
def nPr(n, r):
    return factorial(n) // factorial(n - r)

# Taking inputs from the user
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Calculating nCr and nPr
combinations = nCr(n, r)
permutations = nPr(n, r)

# Displaying the results
print(f"nCr (Combinations) = {combinations}")
print(f"nPr (Permutations) = {permutations}")
 

 
