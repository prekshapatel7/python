from datetime import date

# Define two dates as tuples (day, month, year)
date1 = (10, 3, 2024)  # 10th March 2024
date2 = (25, 3, 2024)  # 25th March 2024

# Convert tuples to date objects
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

# Calculate the difference
difference = abs((d2 - d1).days)

# Print the result
print(f"Number of days between {date1} and {date2} is {difference} days.")
