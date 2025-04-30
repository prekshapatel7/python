'''Write a program that defines a function called frequency() which computes
the frequency of words present in a string passed to it. The frequencies should
be returned in sorted order of words in the string.'''
from collections import Counter

def frequency():
    n = input("Enter the string: ")
    
    # Split the string into words
    words = n.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Sort the dictionary by word (key)
    sorted_word_count = dict(sorted(word_count.items()))
    
    return sorted_word_count

# Call the function and print the result
result = frequency()
print(result)

    
    
