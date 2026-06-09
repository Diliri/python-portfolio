'''
and & or in Python

This file talks about and & or in Python
'''
# What means True or False

bool(0)     # False, zero
bool(13)    # True

bool('')    # False, empty string
bool('Hi')  # True

bool([])    # False, empty list
bool([1,2]) # True


# AND

age = 25
result = age > 18 and age < 65 # True and True
print(result)                  # True

age = 25
result = age < 18 and age < 65 # False and True
print(result)                  # False

age = 25
result = age < 18 and age > 65 # False and False
print(result)                  # False

# OR

age = 25
result = age > 18 or age < 65 # True or True
print(result)                 # True

age = 25
result = age < 18 or age < 65 # False or True
print(result)                 # True

age = 25
result = age < 18 or age > 65 # False or False
print(result)                 # False

# example 1
default_age = 30
age = 0

user_age = age or default_age
print(user_age)                 # 30

# example 2
default_greeting = 'there'
name = input('Enter ur name: (optional)')

user_name = name or default_greeting

print(f'Hello, {user_name}!')

'''Вопрос 5:
What would the value of cmp be at the end of this code segment?
'''

x = True
cmp = x and 18
print(cmp)          # 18

# if the value on the left of the 'and' operator is truthy,
# we get the value on the right of the operator

'''Вопрос 6:
What would the output of this code be? Imagine the user enters 16.
'''

age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job)    # True

# the conditionals evaluate first, and then 'and' and 'or'
# evaluate left to right
