# iterate over dictionary
friend_ages = {'Rolf': 25, "Ann": 37, 'Charlie': 31, 'Bob': 22}

for name in friend_ages:        # iterating over keys
    print(name)

for age in friend_ages.values():    # iterate over values
    print(age)

for name, age in friend_ages.items():     # tuple
    print(f"{name} is {age} years old.")

'''
Rolf is 25 years old.
Ann is 37 years old.
Charlie is 31 years old.
Bob is 22 years old.
'''