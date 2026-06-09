'''
Exercise: an improved lottery! (Python 3.10)
Welcome to this coding exercise!

For this exercise we've provided you with a list of lottery players,
and also with 6 random lottery numbers.

Find out the player with the most correct numbers,
and print out their winnings and their name.

The random numbers are generated in a separate file called `config.py`.
You don't need to modify this file.
(I know we've not looked at the import keyword yet, bear with me on that one!):

import config

# This line loads a set of 6 random numbers from the config file
lottery_numbers = config.lottery_numbers
And the list of players we've given you are:

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
Your task is to find who matched the most numbers,
and print out a string with their name and the amount they won.
For this exercise, assume there will only be 1 winner.
Don't worry about two players matching the same amount of numbers.

For example:

Jen won 1000.

The winnings are calculated with this formula:

winnings = 100 ** len(numbers_matched)

Good luck!
'''

# config.py
# Don't change this file.
# It uses the random module to generate 6 random numbers in a Python set.

# import random

# lottery_numbers = set(random.sample(range(22), 6))


import config

# This line loads a set of 6 random numbers from the config file
lottery_numbers = config.lottery_numbers

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

a_list_of_winnings = [ ]
for player in players:
    numbers_matched = len(lottery_numbers.intersection(player['numbers']))
    winnings = 100 ** numbers_matched
    a_list_of_winnings.append(winnings)

max_win = 0
for win in a_list_of_winnings:
    if win > max_win:
        max_win = win

index = a_list_of_winnings.index(max_win)
print(f"{players[index]['name'].title()} won {max_win}.")

'''Your task is to find who matched the most numbers,
and print out a string with their name and the amount they won.
For this exercise, assume there will only be 1 winner.
Don't worry about two players matching the same amount of numbers.'''


# Jen won 1000.

# The winnings are calculated with this formula:
# winnings = 100 ** len(numbers_matched)


# моє старе рішення
import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

a_list_of_winnings = []
for player in players:
    numbers_matched = lottery_numbers.intersection(player['numbers'])
    winnings = 100 ** len(numbers_matched)
    a_list_of_winnings.append(winnings)

max_win = max(a_list_of_winnings)
index = a_list_of_winnings.index(max_win)

print(f'{players[index]["name"]} won {max_win}.')
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

# рішення Jose

# config.py
# Don't change this file.
# It uses the random module to generate 6 random numbers in a Python set.

# import random

# lottery_numbers = set(random.sample(range(22), 6))
import config

# This line creates a variable to store the numbers defined by the other file (which you shouldn't change)
lottery_numbers = config.lottery_numbers

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]  # start by saying "the top matching player is the first one"

for player in players:  # Go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player

# Calculate their winnings using the formula!
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))

print(f"{top_player['name']} won {winnings}.")