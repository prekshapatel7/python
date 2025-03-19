def sum_avg():
         a=int(input("enter the marks of subject 1"))
         b=int(input("enter the marks of subject 2"))
         c=int(input("enter the marks of subject 3"))
         d=int(input("enter the marks of subject 4"))
         e=int(input("enter the marks of subject 5"))
         total=a+b+c+d+e
         average=total/5
         print("the totalis",total)
         print("äverage marks",average)

import string

def ispangram():
         string1=" the quick brown fox jumps over the lazy dogs"
         alpha=set(string.ascii_lowercase)
         set1=set(string1)
         if set1>=alpha:
                  print("is pangram")
         else:
                  print("no")

def fun():
         a=int(input("eneter a number"))
         l1=[]
         for i in range (1,a+1):
                  l1.append((i,i*i,i*i*i))
         print(l1)
fun()
