x = input('enter the word: ')
i=''
list1 = []
for i in x:
    list1.insert(0,i)

word = ''
i = 0
for i in list1:
    word += i
    print(i,end='')

print('\n'+word)