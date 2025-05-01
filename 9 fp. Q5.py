'''A list contains names of Faculty Members. Write a program to filter out
those names whose length is more than 8 characters'''
user_input = input("Enter names of faculty members ")
lst = user_input.split(',')

print("Your list:", lst)
name=list(filter(lambda n:len(n)>8,lst))
print("names with more than 8 characters are",name)
