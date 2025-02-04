#Write a function that removes one string from another string, if present.
#E.g. Onestring = “abcdef”, removestring = “cd”.
#The finalstring should contain “abef”
def remove_substring(onestring, removestring):
    # Check if removestring is in onestring
    if removestring in onestring:
        # Replace removestring with an empty string
        finalstring = onestring.replace(removestring, "")
        return finalstring
    else:
        return onestring  # Return the original string if removestring is not found

# Accept input from the user
onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")

# Call the function and display the result
finalstring = remove_substring(onestring, removestring)
print(f"The final string is: {finalstring}")
