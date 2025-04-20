# Write a program to create a set containing 10 random numbers
#in the range 15 to 45. Count how many of these numbers are less than 30.
#Delete all numbers that are greater than 35
import random

# Create a set of 10 random numbers between 15 and 45
set1 = set(random.randint(15, 45) for _ in range(10))
print("Original set:", set1)

# Count numbers less than 30
count = 0
for item in set1:
    if item < 30:
        count += 1
print("Numbers less than 30:", count)

# Delete numbers greater than 35
set1 = {item for item in set1 if item <= 35}
print("Set after deleting numbers > 35:", set1)
