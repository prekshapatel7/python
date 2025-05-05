'''Create a class Weather that has a list containing weather parameters.
Define an overloaded in operator that checks whether an item is present in the
list. (Hint: define the function __contains__( )in a class.)'''
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters  # Store weather parameters in a list

    def __contains__(self, item):
        return item in self.parameters

    def __str__(self):
        return f"Weather Parameters: {', '.join(self.parameters)}"

# Example usage
today_weather = Weather(["Rain", "Wind", "Humidity", "Cloudy"])

print(today_weather)

# Check if certain parameters are present using 'in'
print("Rain" in today_weather)       # True
print("Snow" in today_weather)       # False
print("Humidity" in today_weather)   # True
