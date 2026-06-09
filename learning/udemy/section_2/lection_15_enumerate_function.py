''' The enumerate function '''
# 1 example
friends = ['Rolf', 'John', 'Anna']

counter = 0
for friend in friends:
    print(f'{counter} {friend}')
    counter = counter + 1
'''
0 Rolf
1 John
2 Anna
'''
# 2 example
friends = ['Rolf', 'John', 'Anna']

for counter, friend in enumerate(friends, start=1):
    print(f'{counter} {friend}')
'''
1 Rolf
2 John
3 Anna
'''
# 3 example
friends = ['Rolf', 'John', 'Anna']
print(list(enumerate(friends)))
# [(0, 'Rolf'), (1, 'John'), (2, 'Anna')]
print(list(zip([0,1,2], friends)))
# [(0, 'Rolf'), (1, 'John'), (2, 'Anna')]

print(dict(enumerate(friends)))
# {0: 'Rolf', 1: 'John', 2: 'Anna'}
