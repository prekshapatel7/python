# List of temperatures in Fahrenheit
fahrenheit_list = [32, 68, 77, 100, 104]

# Convert each to Celsius
celsius_list = [(f - 32) * 5 / 9 for f in fahrenheit_list]

# Print results
print("Fahrenheit:", fahrenheit_list)
print("Celsius:", celsius_list)
