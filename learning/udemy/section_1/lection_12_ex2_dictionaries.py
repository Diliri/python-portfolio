'''
Exercise: dictionaries (Python 3.10)
You're reaching the end of the first section!

Lottery numbers

lottery_numbers = {13, 21, 22, 5, 8}

A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).


For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
'''

lottery_numbers = {13, 21, 22, 5, 8}

player_1 = {
    'name': 'Diana Lysenko',
    'numbers': {1, 2, 3, 5, 8}
}

player_2 = {
    'name': 'Solomiya Lysenko',
    'numbers': {13, 21, 22, 4, 5}
}

players = [player_1, player_2]
for player in players:
    wins = len(lottery_numbers.intersection(player['numbers']))
    print(f"Player {player['name']} got {wins} numbers right.")


# OR (це моє старе рішення колись цієї задачі)

lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name' : 'Serhiy',
        'numbers' : {20, 3, 97, 19, 2}
        },
    {
        'name' : 'Diana',
        'numbers' : {9, 7, 25, 12, 1}
    }
    ]


name1 = players[0]['name'].title()
name2 = players[1]['name'].title()
num1 = len(players[0]['numbers'].intersection(lottery_numbers))
num2 = len(players[1]['numbers'].intersection(lottery_numbers))
print(f'Player {name1} got {num1} numbers right.')
print(f'Player {name2} got {num2} numbers right.')

# OR зразок від автора курсу на юдемі
lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        "name": "Rolf",
        "numbers": {1, 3, 8, 22, 21}
    },
    {
        "name": "Jose",
        "numbers": {4, 9, 10, 12, 15}
    }
]


name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")

name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")