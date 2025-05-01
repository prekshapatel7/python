'''. Generate the list of 10 different random numbers between -15 and 15.
Create a new list by obtaining square of all numbers in a list.'''
import random
random_numbers = [random.randint(-15, 15) for _ in range(10)]
square=list(map(lambda x:x*x , random_numbers))
print("the list of random numbers is ",random_numbers)
print("their suares",square)
