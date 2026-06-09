name = ''
while not name:     # while not name!='' or while not FALSE or while True
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())

if numOfGuests:     # numOfGuests != 0
    print('Be sure to have enough room for all your guests.')
print('Done.')