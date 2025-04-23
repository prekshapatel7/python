'''Write a program that defines a function create_array() to create
and return a 3D array whose dimensions are passed to the function.
Also initialize each element of this aray to a value passed to the function.
e.g. create_array(3,4,5,n) where first three arguments are 3D array dimensions
and 4th value is for initialing each value of the 3D array.'''
def create_array(x, y, z, value):
    # Create a 3D array using nested list comprehensions
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

# Example usage
array = create_array(3, 4, 5, 7)

# Print the 3D array
for i, layer in enumerate(array):
    print(f"Layer {i}:")
    for row in layer:
        print(row)

    
