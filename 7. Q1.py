#Write a program to create three dictionaries
#and concatenate them to create fourth dictionary.
animals = { 'Tiger' : 141, 'Lion' : 663, ' leopard' : 110 }

birds = { 'Eagle' : 38, 'Sparrow' : 450, 'Parrot' : 200 }
humans={'Preksha':29, 'Harsh':17}

combined = { ** animals, ** birds,**humans }

print (combined)
