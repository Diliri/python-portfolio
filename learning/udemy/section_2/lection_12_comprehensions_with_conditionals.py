''' comprehensions with conditionals '''
# 1 example
ages = [22,35,27,21,20]
odds = [age for age in ages if age % 2 == 1]

print(odds)     # [35, 27, 21]

# 2 example - set approach without title case and order
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'micky']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))
# {'charlie', 'rolf'}

# 3 example list comprehension
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'micky']

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
    ]
print(present_friends)
# ['Rolf', 'Charlie']