#Delete an element of a tuple.
my_tuple = ("Burger", 11.99, "Fries")

# Create a new tuple excluding index 1
new_tuple = my_tuple[:1] + my_tuple[2:]

print(new_tuple)  # Output: ('Burger', 'Fries')
