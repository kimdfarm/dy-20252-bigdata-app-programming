my_book = 2010 , 'C언어' , 100
your_book = [2010 , '자바' , 100]

print(my_book)
print(your_book)

your_book.append('자바책입니다.')
your_book.remove('자바')
print((your_book))
new_book = your_book
print(my_book)
print(your_book)
print(new_book)

print(id(my_book))
print(id(your_book))
print(id(new_book))

"""
year ,title , size= my_book

print(year)
print(title)
print(size)
print('-'*30)
print(my_book[0])
print(my_book[1])
print(my_book[2])
print('-'*30)
print(my_book[-1])
print(my_book[-2])
print(my_book[-3])
print('-'*30)"""
