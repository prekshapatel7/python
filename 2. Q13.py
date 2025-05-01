'''Convert number 0 to 19 to its equivalent words. E.g. 0 à zero, 19ànineteen'''
# List of words from 0 to 19
number_words = [
    "zero", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

# Get input from user
num = int(input("Enter a number (0 to 19): "))

# Check and print the corresponding word
if 0 <= num <= 19:
    print("The number in words is:", number_words[num])
else:
    print("Number out of range! Please enter between 0 and 19.")
