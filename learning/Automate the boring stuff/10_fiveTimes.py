print('My name is')

for i in range(5):
    print('Jimmy Five Times ('
    + str(i)
    + ')')

'''
My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)
'''

# еквівалентний цикл while
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ('
    + str(i)
    + ')')
    i = i + 1