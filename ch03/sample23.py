data = {
    'bgnde':'2025.03.01'
    ,'endde':'2025.03.01','endde':'2025.03.01'
    ,'endde':'2025.03.01','endde':'2025.03.01'

    ,'sj':'삼일절'
}
print(data)
print(type(data))
print(len(data))

print(data.keys())
print(type(data.keys()))

print('-'*30)
for k in data.keys():
    print(k)

print('-'*30)
print(data.values())
print(type(data.values()))
for k in data.values():
    print(k)

print('-'*30)
print(data.items())
print(type(data.items()))
for k in data.items():
    print(k)