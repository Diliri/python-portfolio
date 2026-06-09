# групове присвоювання
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# комбіновані оператори присвоювання
spam = 42.0
spam += 1   # spam = spam + 1
print(spam) # 43.0
spam -= 1   # 42.0
print(spam)
spam *= 2   # 84.0
print(spam)
spam /= 2   # 42.0
print(spam)
spam %= 4   # остача від ділення - буде 2
print(spam)

# конкатенація та реплікація за допомогою
# комбінованих операторів присвоєння
spam = 'Hello'
spam += ' world'    # Hello world
print(spam)
bacon = ['Thomas']
bacon *= 3   # ['Thomas', 'Thomas', 'Thomas']
print(bacon)

# кожен тип даних має свій набір методів.
# метод - це те саме, що функція, але викликається для значень.

# пошук у списку за допомогою методу index()
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))  # 0
# spam.index('privet') # ValueError: 'privet' is not in list
spam = ['hello', 'hi', 'hello', 'hi']
print(spam.index('hi'))  # 1
# тобто за наявності дублікатів - виводиться найперше, що зустрічається

# додавання значень у список
# за допомогою методів append() & insert()
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
# ['cat', 'dog', 'bat', 'moose']
spam.insert(-2, 'chicken')
print(spam)
# ['cat', 'dog', 'chicken', 'bat', 'moose']

# видалення значення зі списку
# за допомогою метода remove()
# якщо знаємо ще й індекс, то тоді
# інструкція del
# причому в обох випадках при дублюючих значеннях
# - видаляється найперше, яке зустрічається
spam = ['cat', 'dog', 'dog', 'chicken', 'bat', 'moose']
spam.remove('dog')
print(spam) # ['cat', 'dog', 'chicken', 'bat', 'moose']
del spam[-1]
print(spam) # ['cat', 'dog', 'chicken', 'bat']

# сортування списку методом sort()
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)     # [-7, 1, 2, 3.14, 5]
spam = ['ants', 'dogs', 'cats', 'elephants']
spam.sort()
print(spam)     # ['ants', 'cats', 'dogs', 'elephants']

# сортування в зворотньому порядку
spam.sort(reverse=True)
print(spam)     # ['elephants', 'dogs', 'cats', 'ants']

# сортування відбувається згідно із кодом ASCII
spam = ['ants', 'ALICE', 'bob', 'dogs', 'Bob', 'cats', 'elephants']
spam.sort()
print(spam)
# ['ALICE', 'Bob', 'ants', 'bob', 'cats', 'dogs', 'elephants']

# як обійти сортування по ASCII (де спочатку великі букви, а потім - малі)
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)     # ['a', 'A', 'z', 'Z']