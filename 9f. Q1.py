#Write a program that defines a function count_lower_upper() that accepts
#a string and calculates the number of uppercase and lowercase alphabets in it.
#It should return these values as a dictionary. Call this function for some
#sample string.
def count_lower_upper():
    inputstring=input("enter the string")
    upper=0
    lower=0
    for char in inputstring:
        if char.islower():
            lower=lower+1
        elif char.isupper():
            upper=upper+1
    print("no of uppercase char are",upper)
    print("no of lowercase char are",lower)
count_lower_upper()
