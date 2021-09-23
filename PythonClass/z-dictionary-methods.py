# mehtods that adds or changes elements in the Dictionary
dict1 = {'name': 'sajjad', 'age': 19, 'programming lang': 'Python'}
dict1.update({'name': 'Sajjad Kazemi'})
print(dict1)
#=> {'name': 'Sajjad Kazemi', 'age': 19, 'programming lang': 'Python'}
# methonds that removes elements from the Dictionary
dict1.pop('programming lang') ; dict1.popitem()
print(dict1)#=> {'name': 'Sajjad Kazemi'}
#other methods for Dictionary
print(dict1.get('name'))#=> Sajjad Kazemi
print(dict1.values())#=> dict_values(['Sajjad Kazemi'])
print(dict1.keys())#=> dict_keys(['name'])
print(dict1.items())#=> dict_items([('name', 'Sajjad Kazemi')]) 
dict1.setdefault('married?','no')
print(dict1)#=> {'name': 'Sajjad Kazemi', 'married?': 'no'}
k = ('key1','key2','key3') ; v = 0
dict2 = dict.fromkeys(k,v)
print(dict2)#=> {'key1': 0, 'key2': 0, 'key3': 0}
dict2.clear() ; print(dict2)#=> {}
y = dict1.copy()
print(y)#=> {'name': 'Sajjad Kazemi', 'married?': 'no'}