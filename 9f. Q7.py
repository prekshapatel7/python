'''A palindrome is a word or phrase that reads the same in both directions.
Write a program that defines a function ispalindrome() which checks whether
a given string is a palindrome or not. Ignore spaces and case mismatch
while checking for palindrome.'''
def palindrome():
    s=input("enter the string")
    s=s.lower()
    a=s[::-1]

    if a==s:
        print("yes")
    else:
        print("no")
    
palindrome()
