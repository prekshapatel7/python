import random

# Generate 20 random integers between 1 and 10
random_list = [random.randint(1, 10) for _ in range(20)]
print("Generated List:", random_list)

# Get input from the user
num = int(input("Enter a number to find its positions in the list: "))

# Find and print all positions of the number
positions = [index for index, value in enumerate(random_list) if value == num]

if positions:
    print(f"The number {num} is found at positions: {positions}")
else:
    print(f"The number {num} is not found in the list.")
