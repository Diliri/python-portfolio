'''
Booleans

This file talks about booleans
'''

truthy = True
falsy = False

# comparison

age = 20
is_over_age = age >= 18   # True
is_under_age = age < 18   # False
is_twenty = age == 20     # True


# another comparison

my_number = 5
user_number = int(input('Enter a number: '))

print(my_number == user_number)

# to make it looks better

my_number = 5
user_number = int(input('Enter a number: '))

matches = my_number == user_number

print(f'U got it right: {matches}.')
