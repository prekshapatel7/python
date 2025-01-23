#Calculate interest where I = PRN/100 , question 16
def interest():

    p=int(input("enter the principal amount"))
    r=int(input("enter the rate of interest"))
    t=int(input("enter the time period"))
    I = p*r*t/100
    print("the simple interest:",I)
interest()
