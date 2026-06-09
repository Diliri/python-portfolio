# values, items and keys methods
spam = {'color': 'red', 'age': 42}

for _ in spam:
    print(_)
# color
# age

for k in spam.keys():
    print(k)
# color
# age

for v in spam.values():
    print(v)
# red
# 42

for i in spam.items():
    print(i)
''' КОРТЕЖІ
('color', 'red')
('age', 42) '''

spam = {'color': 'red', 'age': 42}
print(spam.keys())
# dict_keys(['color', 'age'])

print(list(spam.keys()))
# ['color', 'age']

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
'''
Key: color Value: red
Key: age Value: 42
'''

#  ПЕРЕВІРКА ІСНУВАННЯ КЛЮЧА АБО ЗНАЧЕННЯ В СЛОВНИКУ
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam)           # True
print('name' in spam.keys())    # True
print('color' in spam.values()) # False
print(7 not in spam.values())   # False

# МЕТОД get()
# приймає 2 аргумента: перший - це ключ, якого може й не бути
# другий - це значення за замовчуванням, якщо даного ключа немає в словнику

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# I am bringing 2 cups.
# I am bringing 0 eggs.

# МЕТОД setdefault()
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)
# {'name': 'Pooka', 'age': 5, 'color': 'black'}

spam = {'name': 'Pooka', 'age': 5}
print(spam)
# {'name': 'Pooka', 'age': 5}

spam.setdefault('color', 'white')
print(spam)
# {'name': 'Pooka', 'age': 5, 'color': 'white'}
spam.setdefault('color', 'red')
print(spam)
# {'name': 'Pooka', 'age': 5, 'color': 'white'}