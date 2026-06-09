''' The zip function that makes tuples '''
# previous 2 example DICTIONARY COMPREHENSION
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
    }

print(long_timers)  # {'ruth': 7, 'charlie': 15, 'Jen': 11}

# 1 example with zip function
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
time_since_seen = [3,7,15,11]

long_timers = dict(zip(friends, time_since_seen))
print(long_timers)  # {'Rolf': 3, 'ruth': 7, 'charlie': 15, 'Jen': 11}

# 2 example
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
time_since_seen = [3,7,15,11]

long_timers = list(zip(friends, time_since_seen))
print(long_timers)  # [('Rolf', 3), ('ruth', 7), ('charlie', 15), ('Jen', 11)]
long_timers = list(zip(friends, time_since_seen,[1,2,3,4,5]))
print(long_timers)
# [('Rolf', 3, 1), ('ruth', 7, 2), ('charlie', 15, 3),
# ('Jen', 11, 4)]

# 3 example
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
time_since_seen = [3,7,15,11]

long_timers = zip(friends, time_since_seen)
print(long_timers)      # <zip object at 0x7f62ddd0b4c0>