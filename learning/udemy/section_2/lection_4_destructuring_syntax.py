'''
DESTRUCTURING SYNTAX IN PYTHON
'''
# 1 example
currencies = 0.8, 1.2 # to pounds!
# this is a tuple !
# also we can define it like :
# currencies = (0.8, 1.2)
usd, eur = currencies

# 2 example
# now we have a list of tuples
friends = [
    ('Rolf',25), ('Ann',37), ('Charlie',31), ('Bob', 22)
    ]

for name, age in friends:
    print(f'{name} is {age} years old.')

'''
Rolf is 25 years old.
Ann is 37 years old.
Charlie is 31 years old.
Bob is 22 years old.
'''
# 3 example
friends = [
    ('Rolf',25), ('Ann',37), ('Charlie',31), ('Bob', 22)
    ]

for friend in friends:
    name, age = friend
    print(f'{name} is {age} years old.')

# 4 example
friends = [
    ('Rolf',25), ('Ann',37), ('Charlie',31), ('Bob', 22)
    ]

for friend in friends:
    name = friend[0]
    name = friend[1]
    print(f'{name} is {age} years old.')

