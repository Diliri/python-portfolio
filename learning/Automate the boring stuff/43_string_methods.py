# ЕКРАНОВАНІ СИМВОЛИ
print('Hello\'s my dear!') # Hello's my dear!
print('Hello\"s my dear!') # Hello"s my dear!
print('Hello\ts my dear!') # Hello   s my dear!
print('Hello\\s my dear!') # Hello\s my dear!
print('Hello\ns my dear!')
'''
Hello
s my dear!
'''
print('\n\n')

# СИРИЙ РЯДОК
print(r'That is Carol\'s cat.')
# That is Carol\'s cat.
print('\n\n')

# ОПЕРАТОРИ in / not in В РЯДКАХ
print('Hello' in 'Hello world')      # True
print('' in 'spam')                  # True
print('cats' not in 'cats and dogs') # False
print('\n\n')


# МЕТОДИ isupper() / islower()
print('HELLO'. isupper())       # True
print('world'.islower())        # True
spam = 'Hello world!'
print(spam.islower())           # False
print('abc12345'.islower())     # True
print('12345'.islower())        # False
print('12345'.isupper())        # False
print('Hello'.upper().lower())  # hello
print('HeLLO'.lower().islower()) # True
print('\n\n')


# РЯДКОВІ МЕТОДИ isX()
# isapha()      # True, якщо в рядку лише букви
# isalnum()     # True, якщо в рядку лише букви та цифри
# isdecimal()   # True, якщо лише цифри
# isspace()     # True, якщо в рядку лише tab, space, new line
# istitle()     # True, якщо This Is What I Mean

print('123'.isdecimal())    # True
print('This Is NOT Title Case'.istitle())    # False
print('\n\n')


# МЕТОДИ startswith() / endswith()
print('Hello world!'.startswith('Hello')) # True
print('Hello world!'.endswith('world!'))  # True
print('abc123'.startswith('abcdef'))      # False
print('abc123'.endswith('12'))            # False
print('Hello world!'.startswith('Hello world!')) # True
print('Hello world!'.endswith('Hello world!'))   # True
