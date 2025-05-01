'''Consider the following list:
lst = ['madam','Python',"malayalam",12321]
Write a program to print those strings which are palindromes.'''

lst = ['madam','Python',"malayalam",12321]
reverse_lst=list(filter(lambda text:str(text) == str(text)[::-1],lst))
print("palindrom ",reverse_lst)
