'''Given a text file, write a program to create another text file deleting
the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.'''
# Define file paths
input_file = "input.txt"    # The original text file
output_file = "output.txt"  # The new file after removing words

# List of words to be replaced
words_to_remove = ['a', 'the', 'an']

try:
    # Read the content of the input file
    with open(input_file, "r") as infile:
        content = infile.read()

    # Replace the specified words with a blank space
    for word in words_to_remove:
        content = content.replace(f" {word} ", " ")  # Replace surrounded by spaces

    # Write the modified content to the output file
    with open(output_file, "w") as outfile:
        outfile.write(content)

    print(f"Words 'a', 'the', 'an' have been removed and saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print("An error occurred:", e)
