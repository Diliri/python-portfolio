message = 'It was a bright day in April, +\
and the clocks were striking thirteen.'
count = { }

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
# {'I': 1, 't': 6, ' ': 12, 'w': 2, 'a': 4, 's':
# 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'd
#': 2, 'y': 1, 'n': 4, 'A': 1, 'p': 1, 'l': 2,
#',': 1, '+': 1, 'e': 5, 'c': 2, 'o': 1, 'k': 2
#, '.': 1}