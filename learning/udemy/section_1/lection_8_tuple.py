'''
Tuples

This file talks about tuples in Python
'''

# they are keeping unchanged
short_tuple = 'Rolf', 'Bob'
a_bit_clearer = ('Rolf', 'Bob')

# ordinary list with 2 elements
NO_tuple_in_a_list = ['Rolf', 'Bob']
tuple_in_a_list = [('Rolf', 'Bob')]

NOT_a_tuple = 'Rolf'    # statement
a_tuple = 'Rolf',       # tuple

# Example 1
friends = ('Rolf', 'Bob', 'Ann')
#friends.append('Jen') # <- will occure an error

''' How to add to a tuple, if you can't append to it? '''
friends = friends + ('Jen',) # create a new tuple
print(friends)

''' Tuples are useful for when u wanna keep them unchanged.'''