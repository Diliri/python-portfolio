# наступні два рядки еквівалентні
# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))
# це ф-ції корисні, коли сам словник містить
# вкладені списки або словники.

import pprint
message = 'It was a bright day in April, \
and the clocks were striking thirteen.'
count = { }

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
'''
{' ': 12,
 '+': 1,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 2,
 'd': 2,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 2,
 'n': 4,
 'o': 1,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
'''