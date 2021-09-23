user=input('enter username: ')
age = input('enter age: ')
str1 = 'my name is {username} and im {age} years old!'.format(username = user,age = age)
print(str1)
str2= 'sajjad Kazemi'
print(str2.capitalize())  #=> Sajjad kazemi
print(str2.casefold())  #=> sajjad kazemi
print('abcdefg'.upper())  #=> ABCDEFG
print('  sajjad    '.center(18))  #=>    sajjad
print(str2.count('a'))  #=> 3
print(str2.encode())  #=> b'sajjad Kazemi'
print(str2.endswith('i'))  #=> True
print(str2.startswith('s'))  #=> True
print('H\tE\tL\tL\tO'.expandtabs(2))  #=> H E L L O
print(str2.find('e'))  #=> 10
# print(str2.format_map())  #=> unknown!
print(str2.index('i'))  #=> 12
print(str2.isalnum())  #=> False
print(str2.isalpha())  #=> doesn't apply space! => False
print(str2.isascii())  #=> True
print(str2.isdecimal())  #=> False
print('9567946'.isdigit()) #=> True
print(str2.isidentifier())  #=> False
print(str2.islower())  #=> False
print(str2.isnumeric())  #=> False
print(str2.isprintable())  #=> True
print('     '.isspace())  #=> True (str2.isspace) => False
print(str2.istitle())  #=> False
print(str2.isupper())  #=> False
print(str2.join([' 1 ' , ' 2 ' , ' 3 ']))  #=>  1 sajjad Kazemi 2 sajjad Kazemi 3
print(str2.ljust(25), 'is 19 years old')  #=>sajjad Kazemi             is 19 years old
print('HELLO'.lower())  #=>  hello
print(str2.lstrip('asj'))  #=> d Kazemi

x = str2.maketrans('sajd','molh')
print(str2.translate(x))  #=> molloh Kozemi

print('i could had a better day if i decided that'.partition('decided'))
# => ('i could had a better day if i ', 'decided', ' that')

print('i could had a better day if i decided that'.partition('apple'))
# => ('i could had a better day if i decided that', '', '')

print(str2.replace('Kazemi' , 'ghasemi'))  #=>  sajjad ghasemi
print("i realy love the real life".rfind('real'))  #=> 17
print("i realy love the real life".rindex('real'))  #=>17
print(str2.rjust(20,'='))  #=> =======sajjad Kazemi

print('i could had a better day if i decided that'.rpartition('decided'))
# => ('i could had a better day if i ', 'decided', ' that')

print('i caould had a better day if i decided that'.rpartition('apple'))
# => ('', '', 'i caould had a better day if i decided that')

print('python is easy'.split(' '))  #=> ['python', 'is', 'easy']
print('python is easy'.split(' ',1))  #=> ['python', 'is easy']
print('python is easy'.rsplit(' '))  #=> ['python', 'is', 'easy'] 
print('python is easy'.rsplit(' ',1))  #=> ['python is', 'easy']

print('    apple     '.strip())  #=>  apple
print('--23.....apple....'.strip('-23.'))  #=> apple
print('    apple    '.rstrip())  #=>     apple
print('12...----apple.....'.rstrip('12-.'))  #=> 12...----apple
# string.lstrip()
print('hello\nworld'.splitlines())  #=> ['hello', 'world']
print('hello\nworld'.splitlines(True))  #=> ['hello\n', 'world']
print('abcABC'.swapcase())  #=> ABCabc
print('python is easy'.title())  #=> Python Is Easy

dict1 = {115:82,75:108} #ascii codes
print(str2.translate(dict1))  #=> Rajjad lazemi
print(str2.zfill(18))  #=> 00000sajjad Kazemi