#Count no. of alphabets and no. of digits in any given string.
def count():
    a=input("enter a string")
    alphabets_count = 0
    digits_count = 0

# Loop through each character in the string
    for char in a:
        if char.isalpha():  # Check if the character is an alphabet
            alphabets_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digits_count += 1
    print(alphabets_count)
    print(digits_count)
count()
