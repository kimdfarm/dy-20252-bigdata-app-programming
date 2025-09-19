import copy

list_value = ['a','b','c','d','e','f','g','h']

new_value = list_value[::2]

print(list_value)
print(new_value)

list_value[0]='11'

print('-'*30)
print(list_value)
print(new_value)
print('='*30)

