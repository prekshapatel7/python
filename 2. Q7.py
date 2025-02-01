#Accept a year value from the user. Check whether it is a leap year or not.
def leapyear():
    year=int(input("enter the year"))
    if year%4==0:
        print("leap year")
    else:
        print("not")
leapyear()
