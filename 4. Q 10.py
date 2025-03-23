# Generate N numbers of Fibonacci series
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Initializing Fibonacci series list with first two numbers
fibonacci = [0, 1]

for i in range(2, n):  # Start from index 2
    next_term = fibonacci[i - 1] + fibonacci[i - 2]  # Sum of previous two terms
    fibonacci.append(next_term)  # Add new term to the list

print(fibonacci)  # Print the Fibonacci series
