'''Implement a String class containing the following functions:
a. Overloaded += operator function to perform string concatenation
b. Method toLower() to convert upper case letters to lower case.
c. Method toUpper() to convert lower case letters to upper case.'''
class String:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        if isinstance(other, String):
            self.text += other.text
        elif isinstance(other, str):
            self.text += other
        else:
            raise TypeError("Can only concatenate String or str instances")
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def __str__(self):
        return self.text

# Example usage
s1 = String("Hello")
s2 = String(" World")

print("Original s1:", s1)
print("Original s2:", s2)

# Concatenation
s1 += s2
print("After concatenation:", s1)

# Convert to lowercase
s1.toLower()
print("Lowercase:", s1)

# Convert to uppercase
s1.toUpper()
print("Uppercase:", s1)
