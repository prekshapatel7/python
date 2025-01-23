#Convert celcius into Fahrenheit. F = (9/5 * C) + 32, Convert Fahrenheit into celcius. C = 5/9 * (F – 32),
#question 14,15
def celcius_fahrenheit():
    celcius=int(input("enter the temperature in celcius:"))
    fahrenheit=(9/5*celcius)+32
    print("the value in fahrenheit is :",fahrenheit )
celcius_fahrenheit()
def fahrenheit_celcius():
    fahrenheit=int(input("enter the temperature in fahrenheit:"))
    celcius=5/9 * (fahrenheit - 32)
    print("the value in celcius is :",celcius )
    
fahrenheit_celcius()
