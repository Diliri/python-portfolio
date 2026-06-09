'''
User input

This file talks about user input
'''

my_name = 'Diana'
ur_name = input('Please enter ur name: ')

print(f'Hello {ur_name}. My name is {my_name}.')

# input function ALWAYS converts into string

age = input('Enter ur age: ')
print(f'You have lived for {age*12} months.') # output will be 333333333333 e.g.

# better variant is

age = input('Enter ur age: ')
age_num = int(age)
print(f'You have lived for {age_num*12} months.') # output will be OK

# OR
age = int(input('Enter ur age: '))
print(f'You have lived for {age*12} months.') # output will be OK

# OR
age = int(input('Enter ur age: '))
months = age * 12
print(f'You have lived for {months} months.') # output will be OK