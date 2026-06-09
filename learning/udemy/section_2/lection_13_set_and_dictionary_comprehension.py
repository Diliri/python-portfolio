''' Set and dictionary comprehension '''

# previous 2 example - set approach without title case and order
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'micky']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))
# {'charlie', 'rolf'}

# 1 example SET COMPREHENSION
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'micky']

friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {
    name.title()
    for name in present_friends}
print(present_friends)
# {'Rolf', 'Charlie'}

# 2 example DICTIONARY COMPREHENSION
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
    }

print(long_timers)