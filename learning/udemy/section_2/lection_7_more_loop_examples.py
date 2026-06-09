'''A couple more loop examples !
Repeating a loop 20 times
As a reminder, here's how you can use a
for loop with range() to repeat something
a certain number of times:
'''
for i in range(20):
  print(i)
'''
In this case, what we're repeating is the print(),
but we could repeat anything 20 times.
'''

'''
Looping to use values in a collection
Here's an example of a for loop that doesn't just
repeat something a number of times:
'''

kid_ages = (3, 7, 12)
for age in kid_ages:
  print(f'I have a {age} year old kid.')
'''
In this case we're doing this 3 times,
but that's because our collection has 3 elements.
Really the loop is being used to do something
for each value in our collection, kid_ages .
'''