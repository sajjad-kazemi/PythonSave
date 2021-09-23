# mehtods that adds elements to the List
list1 = ['abcd','efgh','ijkl']
list1.append('mnop')
list1.extend(['qrst','uvwx','yz'])
list1.insert(0,'alphabet:')
print(list1) # => ['alphabet:', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']
# methonds that removes elements from the List
list1.remove('alphabet:')
print(list1.pop(0))  # => abcd
list1.clear()
print(list1) # => []
# other List methods
list1 = [1,2,2,4,5,6,7,5,5]
print(list1.count(2)) # => 2
print(list1.index(5,6)) # => 7
list1.sort() ; list1.reverse()
print(list1) # => [7, 6, 5, 5, 5, 4, 2, 2, 1]
c = list1.copy() ; print(c)
del list1 ; del c
# print list1 # => SyntaxError!