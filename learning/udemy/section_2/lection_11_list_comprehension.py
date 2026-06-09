''' List Comprehension '''
# 1 example
numbers = [0,1,2,3,4]
doubled_numbers = [ ]

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)  # [0, 2, 4, 6, 8]

# 2 example
numbers = [0,1,2,3,4]
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)  # [0, 2, 4, 6, 8]

# 3 example
doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)  # [0, 2, 4, 6, 8]

# 4 example
doubled_numbers = [3 for _ in range(5)]
print(doubled_numbers)  # [3, 3, 3, 3, 3]

# 5 example
friend_ages = [22,31,35,37]
age_strings = [f'My friend is {age} years old.'
                for age in friend_ages]

print(age_strings)
'''
['My friend is 22 years old.', 'My friend is 31 years old
.', 'My friend is 35 years old.', 'My friend is 37 years
old.']
'''

# 6 example
names = ['Rolf', 'Bob', 'Jen']
lower = [name.lower() for name in names]
print(lower)    # ['rolf', 'bob', 'jen']

# 7 example with title() casing
friend = input('Enter your friends name: ')
friends = ['Rolf', "Bob", 'Jen', 'Anna']
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")