set1 = {1,2,3,4,5,1,2,3}
print(set1)
set1 = list(set1)
print(set1)
tuple1 = (1,2,3,True,False)
print(tuple1[1])
print('name', 'age') # , = ' ' (space)
# name = input('Firstname:') +' '+ input('Lastname:') # or next line
name = input('enter the firstname and the lastname with space bitween: ')
sent1 = 'the firstname is {fn} and the lastname is {ln}'.format(fn = name.split(' ')[0],ln = name.split(' ')[1])
print(sent1)