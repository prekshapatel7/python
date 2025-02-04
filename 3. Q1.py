#Count how many vowels are there in a string. Accept the string from the user
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0  # Initialize count

    # Loop through each character in the string
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment count if it's a vowel

    return count  # Return the final count

# Accept input from user
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)

print(f"Number of vowels in the string: {vowel_count}")
