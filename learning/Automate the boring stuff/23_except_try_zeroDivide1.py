# another example
# of try / except instruction

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))  # 21.0
    print(spam(12)) # 3.5
    print(spam(0))  # Error: Invalid argument.
    print(spam(1))  # НЕ ВИКОНАЛАСЬ !!!
except ZeroDivisionError:
    print('Error: Invalid argument.')