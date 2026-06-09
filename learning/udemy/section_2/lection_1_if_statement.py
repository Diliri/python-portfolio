''' If statement '''
friend = 'Rolf'
user_name = input("Enter ur name: ")

if user_name == friend:
    print('Hello, friend!')

if user_name != friend:
    print('Hello, stranger!')

# OR
if user_name == friend:
    print('Hello, friend!')
else:
    print('Hello, stranger!')

# 1 example
print(bool(5))      # True
print(bool(0))      # False

if 5:
    print('It runs.U will see it')

# 2 example
name = input('Enter ur name: ')
print(bool(name))

if name:
    print('We know ur name. ')

# 3 example
friends = ['Rolf', 'Bob', 'Anne']
family = ['Jen', 'Charlie']

user_name = input('Enter ur name: ')

if user_name in friends:
    print('Hello, friend!')

if user_name in family:
    print('Hello, family!')
else:
    print("I don't know u.")

# but we will have a problem. see it now:
# input: 'Rolf'
# output: Hello, friend! I don't know u.

# 4 example
friends = ['Rolf', 'Bob', 'Anne']
family = ['Jen', 'Charlie']

user_name = input('Enter ur name: ')

if user_name in friends:
    print('Hello, friend!')
elif user_name in family:
    print('Hello, family!')
else:
    print("I don't know u.")

# input: 'Rolf'
# output: Hello, friend!



# question from a test
'''
Вопрос 3:
The below is not working Python code, but it represents a pattern of what we could do in Python (some call it pseudocode). Can you fill in the missing word, represented by ____ ?

if <condition> is True:
    <block to run if above condition is True>
elif <condition> is True:
    <block to run if above condition is True>
else:
    <block to run if none of the other conditions are True>
'''




