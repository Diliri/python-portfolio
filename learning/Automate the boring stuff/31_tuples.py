# Tuple vs Lists
# Кортежі відрізняються від списків тим,
# що їх не можна змінювати

print(type(('hello' ,)))    # <class 'tuple'>
print(type('hello'))        # <class 'str'>

# перетворення у список або кортеж
a_list = ['cat', 'dog', 5]
print(tuple(a_list))        # ('cat', 'dog', 5)
print(a_list)               # ['cat', 'dog', 5]

a_tuple = ('cat', 'dog', 5)
print(list(a_tuple))        # ['cat', 'dog', 5]
print(list('hello'))        # ['h', 'e', 'l', 'l', 'o']


