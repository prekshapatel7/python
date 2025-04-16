#Generate 30 random numbers and put them in a list. Create two more lists –
#one containing only +ve numbers and another with –ve nos.
import random

# Generate 30 random numbers and put them in a list
random_list = [random.randint(-100, 100) for _ in range(30)]
print("The generated list is:", random_list)

# Create two lists: one for positive numbers and one for negative numbers
positive_list = []
negative_list = []

# Loop through the random list and categorize the numbers
for item in random_list:
    if item < 0:
        negative_list.append(item)
    elif item > 0:
        positive_list.append(item)
    else:
        # If the number is 0, do nothing or print it
        pass

# Print the lists
print("The positive numbers are:", positive_list)
print("The negative numbers are:", negative_list)

