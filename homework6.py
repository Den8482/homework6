my_dict = {'Denis': 1981, 'Vadim': 2004, 'Danila': 2015}
print(my_dict)
print(my_dict['Vadim'])
my_dict['Vlad'] = 1967
print(my_dict)
my_dict.update({'Svetlana': 1964, 'Oleg': 1982})
print(my_dict)
del my_dict['Danila']
print(my_dict.get('Danila'))
print(my_dict)
my_set = {1,2,3,4,1,3,5,'Name',(1,2,3)}
print(my_set)
print(my_set.add(8))
print(my_set.add(9))
print(my_set)
print(my_set.remove('Name'))
print(my_set)