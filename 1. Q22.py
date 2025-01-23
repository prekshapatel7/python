#Calculate net sales where net sales = gross sales – 10% discount of gross sales.
def netsales():
    grosssales=float(input("enter the gross sales"))
    g1=0.1*grosssales
    
    netsales=grosssales-g1
    print("the net sale is",netsales)
netsales()
