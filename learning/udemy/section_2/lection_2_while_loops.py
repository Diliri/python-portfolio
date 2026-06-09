''' While loop '''

# 1 example
is_learning = True

while is_learning:
    print("Ur learning!")
    is_learning = False

# 2 example
is_learning = True

while is_learning:
    print("Ur learning!")
    is_learning = input('R u still learning? ')
    # Enter will occure the False !!!

# 3 example
is_learning = True

while is_learning:
    print("Ur learning!")
    user_input = input('R u still learning? ')
    is_learning = user_input == 'yes'

# 4 example
user_input = input('Do u wish to run the program? (yes/no): ')

while user_input == 'yes':
    print("We are running!")
    user_input = input('Do u wish to run the program? (yes/no): ')

print('We stopped running.')