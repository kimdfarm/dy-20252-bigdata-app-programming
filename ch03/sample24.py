data =  {
    'bgnde'
    ,'endde'
    ,'endde'

    ,'sj'
}
print(data)
print(type(data))

data.add('title')
data.add('desc')
data.add('sj')

print(data)
print(type(data))

data.remove('sj')
print(data)
"""
if 'sj'in data:
    data.remove('sj')
    print(data)
else:
    print(None)
print(data)"""

data.discard('sj')
data.discard('sj')
data.discard('sj')
print(data)