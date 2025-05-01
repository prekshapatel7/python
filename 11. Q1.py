'''Write a program for the following:

o Write a program that receives an integer an input.
If a string is entered instead of an integer, then report an error and give
another chance to user to enter an integer. Continue this process till correct
input is supplied.'''
def get_integer_input():
    while True:  # Loop until valid integer input is given
        try:
            user_input = int(input("Please enter an integer: "))  # Try to convert input to integer
            return user_input  # Return the valid integer
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")  # Catch non-integer inputs

# Call the function and get valid input
valid_integer = get_integer_input()

print(f"You have entered a valid integer: {valid_integer}")
