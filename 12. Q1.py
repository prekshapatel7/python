'''Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition,
subtraction, multiplication and division.'''
'''a=4+3j #here j is coming 
b=3-2j
print(a,type(a))
print(b,type(b))
c=a+b
d=a-b
e=a*b
f=a/b
print(c)
print(d)
print(e)
print(f)'''
class xcomplex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def display(self):
        print(f'{self.r}{self.i:+}i')
a=xcomplex(4,3)
b=xcomplex(3,-2)
a.display()
b.display()
print(a)

