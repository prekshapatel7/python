'''Write a program that defines a function count_alpha_digits() that accepts
a string and calculates the number of alphabets and digits in it.
It should return these values as a dictionary.'''
def count_alpha_digits():
    n = input("Enter the string: ")
    alphabets = 0
    digits = 0

    for item in n:
        if item.isalpha():  # Check if the character is alphabet
            alphabets += 1
        elif item.isdigit():  # Check if the character is a digit
            digits += 1

    result_dict = {'alphabets': alphabets, 'digits': digits}  # Create a dictionary
    return result_dict

# Call the function and print the result
result = count_alpha_digits()
print(result)

