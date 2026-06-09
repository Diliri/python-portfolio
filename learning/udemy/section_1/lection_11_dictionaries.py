''' Dictionaries

the difference between dictionaties and sets,
that dictionaries DO keep the order, as of Python 3.7

But like in sets, u cannot have duplicate keys
in a dictionary.'''

friend_ages = {'Rolf': 24, 'Adam': 30, 'Ann': 27}
print(friend_ages['Rolf'])  # 24

friend_ages['Bob'] = 20     # add a key with a key
friend_ages['Rolf'] = 25    # 25 SO WE CHANGE A VALUE  !!!!!!!!!

print(friend_ages)

# Example 1
# A tuple of our friends
friends = (
    {'name':'Rolf Pun', 'age': 24},     # indentation = four spaces
    {'name':'Adam Smith', 'age': 30},
    {'name':'Ann Sklyar', 'age': 27}

    )

print(friends[0]['name'])   # Rolf Pun
print(friends[1]['name'])   # Adam Smith
print(friends[2]['name'])   # Ann Sklyar

# OR

friend = friends[0]
print(friend['name'])       # Rolf Pun

# Example 2
# here we have a list of tuples
# we can turn this into a dict

friends = [('Rolf', 25), ('Adam', 30), ('Ann', 27), ('Bob', 20)]
friend_ages = dict(friends)
print(friend_ages)      # {'Rolf': 25, 'Adam': 30, 'Ann': 27, 'Bob': 20}

# Example 3

my_friends = {
    'Jose': {'last_seen': 6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}


print(my_friends['Jose']['last_seen'])  # 6


# Example 4
players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])        # (13, 22, 3, 6, 9)
print(players[0]['numbers'][0])     # 13 because of a TUPLE
