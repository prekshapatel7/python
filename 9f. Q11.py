'''Write a function create_list() that creates and returns
a list which is an intersection of two lists passed to it.'''
def create_list(list1, list2):
    # Convert lists to sets and find the intersection
    intersection = list(set(list1) & set(list2))
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = create_list(list1, list2)
print(result)
