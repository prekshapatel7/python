'''Write a program that defines a function convert() that receives a string
containing a sequence of whitespace separated words and returns a string
after removing all duplicate words and sorting them alphanumerically.
Hint: use set(), list () , sorted(), join().'''
def convert(input_str):
    # Split the string into words
    words = input_str.split()
    
    # Remove duplicates using set and sort the result
    unique_sorted_words = sorted(set(words))
    
    # Join the sorted words back into a string
    result = ' '.join(unique_sorted_words)
    
    return result

# Example usage
input_string = "banana apple orange banana mango apple"
output = convert(input_string)
print(output)  # Output: apple banana mango orange

    
