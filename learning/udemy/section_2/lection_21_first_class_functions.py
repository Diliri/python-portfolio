# FIRST-CLASS FUNCTIONS IN PYTHON
# 1 example
def greet():
    print('Hello')

greet           # nothing
hello = greet   # nothing
hello()         # Hello

# 2 example
def average(seq):
    return sum(seq) / len(seq)

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total'," + \
    "or 'top': ")

    if operation == 'average':
        print(avg(grades))
    elif operation == 'total':
        print(total(grades))
    elif operation == 'top':
        print(top(grades))

'''
Hello
Student: Rolf
Enter 'average', 'total',or 'top': total
352
Student: Bob
Enter 'average', 'total',or 'top': average
76.0
Student: Jen
Enter 'average', 'total',or 'top': top
99
Student: Anne
Enter 'average', 'total',or 'top': top
100
'''

# 3 example
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    'average' : avg,
    'total' : total,
    'top' : top
    }

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total'," + \
    "or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))

'''
Hello
Student: Rolf
Enter 'average', 'total',or 'top': total
352
Student: Bob
Enter 'average', 'total',or 'top': average
76.0
Student: Jen
Enter 'average', 'total',or 'top': top
99
Student: Anne
Enter 'average', 'total',or 'top': top
100
'''

# 4 example
operations = {
    'average' : lambda seq: sum(seq) / len(seq),
    'total' : sum,
    'top' : max
    }

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total'," + \
    "or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))