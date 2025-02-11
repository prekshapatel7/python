import random

# Step 1: Generate 50 random numbers in the range 1 to 30
random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list with duplicates:", random_numbers)

# Step 2: Remove duplicates by converting to a set and back to a list
unique_numbers = list(set(random_numbers))
print("List after removing duplicates:", unique_numbers)
