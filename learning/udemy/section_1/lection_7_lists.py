'''
Lists in Python

This file talks about lists
'''

friends = ['Bob', 'Anne', 'Rolf']
print(friends[0])
print(friends[1])

print(len(friends))     # 3 elements

# about lists in list

friends = [
    ['Bob',20],
    ['Anne',40],
    ['Rolf', 35],
]
print(friends[0][0])    # Bob
print(friends[0][1])    # 20

# add to the END OF A LIST
friends = ['Bob', 'Anne', 'Rolf']
friends.append('Jen')
print(friends)

# REMOVE from a list
friends.remove('Jen')
print(friends)

friends = [
    ['Bob',20],
    ['Anne',40],
    ['Rolf', 35],
]
friends.remove(['Anne',40]) # WE MUST REMOVE ALL THE ENTIRE LIST
print(friends)
