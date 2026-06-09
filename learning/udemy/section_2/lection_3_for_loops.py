''' FOR loop '''

# 1 example
friends = ['Rolf', 'Jen', 'Ann']

for friend in friends:      # could be tuple, set or dictionary
    print(friend)

# 2 example
elements = [0,1,2,3,4,5,6,7,9]

for index in elements:
    print(index)

# 3 example
elements = [0,1,2,3,4,5,6,7,9]

for index in elements:
    print('Hello, world!')

# 4 example
elements = [0,1,2,3,4,5,6,7,9]

for _ in elements:
# underscore shows that u don't wanna use variable's name
    print('Hello, world!')

# 5 example
for _ in range(10):
    print('Hello, world!')

# 6 example
for index in range(5, 10):      # from 5 to 9
    print(index)

# 7 example
for index in range(2, 20, 3):      # 2,5,8,11,14,17
    print(index)

# 8 example
students = [
    {'name': 'Rolf', 'grade': 90},
    {'name': 'Bob', 'grade': 78},
    {'name': 'Jen', 'grade': 100},
    {'name': 'Ann', 'grade': 80},
]

for student in students:
    name = student['name']
    grade = student['grade']

    print(f'{name} has a grade of {grade}.')

'''
Rolf has a grade of 90.
Bob has a grade of 78.
Jen has a grade of 100.
Ann has a grade of 80.
'''