#Write your own functions (without using built-in functions)
#to convert all characters of a string into lower case/upper case/toggle case
def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # If uppercase letter
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # Keep other characters unchanged
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # If lowercase letter
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep other characters unchanged
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        else:
            result += char  # Keep other characters unchanged
    return result

# Accept input from the user
user_input = input("Enter a string: ")

# Test functions
print("Lowercase:", to_lowercase(user_input))
print("Uppercase:", to_uppercase(user_input))
print("Toggle Case:", toggle_case(user_input))

    
