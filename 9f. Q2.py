#Write a program that defines a function compute() that calculates the value of
#n + nn + nnn + nnnn, where n is digit received by the function.
#test the function for digits 4 to 7.
def compute(n):
    
    answer=n+ n*n+ n*n*n+ n*n*n*n
    print(answer)
compute(4)
compute(5)
compute(6)
compute(7)
    
