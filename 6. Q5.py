#Remove empty tuple(s) from the list of tuples.
tuple_list = [("Pizza", 14.75), (), ("Burger", 11.99), (), ("Fries", 4.25)]
cleaned_list = [t for t in tuple_list if t]
print(cleaned_list)
