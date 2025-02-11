import random

# Step 1: Generate a list of 5 random odd integers
odd_numbers = [random.randint(1, 50) * 2 + 1 for _ in range(5)]
print("List of 5 random odd integers:", odd_numbers)

# Step 2: Generate a list of 4 random even integers
even_numbers = [random.randint(1, 50) * 2 for _ in range(4)]
print("List of 4 random even integers:", even_numbers)

# Step 3: Replace the third element of odd_numbers with even_numbers
odd_numbers[2] = even_numbers
print("After replacing the third element of odd list with even list:", odd_numbers)

# Step 4: Flatten the list
flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)  # Unpack list elements
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

# Step 5: Sort the flattened list
flattened_list.sort()
print("Sorted list:", flattened_list)
