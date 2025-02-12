#A list contains names of boys and girls as its elements.
#Boys’ names are stored as tuples.
#Write a program to find out number of boys and girls in the list.
#(Hint: use isinstance(ele,tuple))
list=['Preksha' , 'Rudra', 'Hetvi' , ('Harsh', 'Siddharth')]
count1=0
count2=0
for i in list:
    if isinstance(i,tuple):
        count1=count1+len(i)
    else:
        count2+=1
print("number of boys=",count1)
print("number of girls",count2)
    

