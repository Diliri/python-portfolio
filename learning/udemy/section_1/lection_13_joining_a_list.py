friends = ['Rolf', 'Ann', 'Charlie']
print(f'My friends are {friends}.')
# My friends are ['Rolf', 'Ann', 'Charlie'].

comma_separated = ', '.join(friends)
print(f'My friends are {comma_separated}.')
# My friends are Rolf, Ann, Charlie.

comma_separated = ' & '.join(friends)
print(f'My friends are {comma_separated}.')
# My friends are Rolf & Ann & Charlie.