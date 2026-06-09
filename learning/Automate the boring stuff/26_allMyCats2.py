''' СПИСКИ '''

catNames = []
while True:
    print('Enter the name of cat ' +
    str(len(catNames) + 1) +
    ' Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)

'''
Enter the name of cat 1 Or enter nothing to stop.):
Thomas
Enter the name of cat 2 Or enter nothing to stop.):
Shyshka
Enter the name of cat 3 Or enter nothing to stop.):
The cat names are:
 Thomas
 Shyshka
'''