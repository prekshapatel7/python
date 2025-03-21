def reverse_natural_numbers():
    n = int(input("Enter the number: "))  # Get user input

    for i in range(n, 0, -1):  # Loop from n down to 1
        print(i)  

reverse_natural_numbers()  # Call the function

