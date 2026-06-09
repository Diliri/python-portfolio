def add(x, y=3):    # y is default parameter
    total = x + y
    return total

print(add(1, 1))        # 2
print(add(1))           # 4
print(add(x=1))         # 4
print(add(x=0, y=1))    # 1 named arguments

# print(add(x=0, 1))    # syntax error
print(add(5, y=2))      # OK !!!!

# print(add(y=7))       # type error
# because we have typed only named/keyword argument (y)
# and NO positional argument (x)

print(1, 2, 3, 4, 5)
# 1 2 3 4 5
print(1, 2, 3, 4, 5, sep = ' - ')
# 1 - 2 - 3 - 4 - 5