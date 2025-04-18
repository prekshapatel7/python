#modify an element of tuple
# Original tuple
food = ("Burger", 11.99)

# Convert to list
food_list = list(food)

# Modify the element (change price)
food_list[1] = 12.99

# Convert back to tuple
food = tuple(food_list)

print(food)  # Output: ('Burger', 12.99)
