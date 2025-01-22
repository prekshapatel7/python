#Convert bytes into KB, MB and GB, Kilobyte (KB): 1 KB = 1024 bytes
#Megabyte (MB): 1 MB = 1024 KB = 1,048,576 bytes
#Gigabyte (GB): 1 GB = 1024 MB = 1,073,741,824 bytes
def convert():
    byte=int(input("enter the number of bytes"))
    inkb=byte/1024
    inmb=inkb/1024
    ingb=inmb/1024
    print("given bytes is equivalent to kb,mb,gb",inkb,inmb,ingb)
convert()
