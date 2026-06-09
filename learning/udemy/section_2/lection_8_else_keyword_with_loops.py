''' The else keyword with loops '''

# 1 example
# a naive approach
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']
all_successful = True

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        all_successful = False
        break
    print(f'This car is {status}.')
    print("Shipping new car to customer!")

if all_successful:
    print('All cars built successfully. No faulty cars!')

# 2 example
# The else keyword with loops
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        all_successful = False
        break
    print(f'This car is {status}.')
    print("Shipping new car to customer!")
else:
    print('All cars built successfully. No faulty cars!')

''' So the else keyword can actually be applied to loops,
both the for loop and the while loop. And it means that
this code here will run if the loop runs to completion,
i.e. there are no breaks and no errors.
This is actually something that not a lot of people know.
'''