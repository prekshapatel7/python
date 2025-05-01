'''Write a program to copy contents of one file to another.
While doing so, replace all lowercase characters into uppercase characters.'''# Define file paths
source_file = "source.txt"
destination_file = "destination.txt"

try:
    # Open source file in read mode
    with open(source_file, "r") as src:
        content = src.read()

    # Convert content to uppercase
    modified_content = content.upper()

    # Open destination file in write mode
    with open(destination_file, "w") as dest:
        dest.write(modified_content)

    print(f"Content copied from '{source_file}' to '{destination_file}' with uppercase conversion.")

except FileNotFoundError:
    print(f"Source file '{source_file}' not found.")
except Exception as e:
    print("An error occurred:", e)
