#A list contains names of boys and girls as its elements.
#Boys’ names are stored as tuples.
#Write a program to find out number of boys and girls in the list.
#(Hint: use isinstance(ele,tuple))
list=['preksha', 'rudra' , 'hetvi' ,('harsh','ram'),'bela',('samik','rahul','rohit')]
countboys=0
countgirls=0

for i in list:
    if isinstance( i, tuple):
        countboys=countboys+len(i)
    else:
        countgirls=countgirls+1

print("no of boys are",countboys)
print("no of girls",countgirls)
