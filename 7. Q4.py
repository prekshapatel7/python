#Write a program that reads a string from the keyboard
#and creates dictionary containing frequency of each character
#occurring in the string.
input_string = input("Enter the string: ")
char_freq = {}  

for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequency:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}")

