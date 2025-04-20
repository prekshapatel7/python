#A set contains names which begin either with A or with B. Write a program to
#separate out the names into two sets, one containing names beginning with A
#and another with B.
names={'ananya','bela','aarya','birva'}
seta=set()
setb=set()
for name in names:
    if name.startswith('a'):
        seta.add(name)
    else:
        setb.add(name)
print(seta)
print(setb)
