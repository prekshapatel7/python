#A list contains tuples containing roll no., name and age of student.
#Write a python program to create three lists separately for roll no., name and age
list=[(213,'preksha',18),(163,'hetvi',19)]
rollno=[student[0] for student in list]
name=[student[1] for student in list]
age=[student[2] for student in list]
print("name list",name)
print("roll no list",rollno)
print("age list",age)

