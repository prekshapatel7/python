'''Write a program to create a csv file that we can directly open in MS-Excel.'''
import csv

# Data to write (list of rows)
data = [
    ["Name", "Age", "City"],
    ["Alice", 23, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 25, "Mumbai"]
]

# Create and write to CSV file
with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully.")
