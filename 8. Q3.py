#Create an empty set. Write a program that adds five
#new names to this set, modifies one existing name and
#deletes two names from it.

# Create an empty set
name_set = set()

# Add five new names
name_set.update(['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print("After adding 5 names:", name_set)

# Modify one name: Let's change 'Charlie' to 'Chris'
# (Since sets don't support direct modification, remove and re-add)
if 'Charlie' in name_set:
    name_set.remove('Charlie')
    name_set.add('Chris')
print("After modifying 'Charlie' to 'Chris':", name_set)

# Delete two names: Let's remove 'Bob' and 'Eva'
name_set.discard('Bob')   # discard() won't throw an error if the name doesn't exist
name_set.discard('Eva')
print("After deleting 'Bob' and 'Eva':", name_set)
