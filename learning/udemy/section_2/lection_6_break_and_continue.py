# break and continue
# we use them ONLY in while and for loops

# 1 example
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        break
    print(f"This car is {status}.")

'''
This car is ok.
This car is ok.
This car is ok.
Stopping the production line!
'''

# 2 example
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line!')
        break
    print(f"This car is {status}.")

    print('Shipping a new car to customer!')

'''
This car is ok.
Shipping a new car to customer!
This car is ok.
Shipping a new car to customer!
This car is ok.
Shipping a new car to customer!
Stopping the production line!
'''

# 3 example
# 2 example
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Found faulty car, skipping...')
        continue
    print(f"This car is {status}.")

    print('Shipping a new car to customer!')

'''
This car is ok.
Shipping a new car to customer!
This car is ok.
Shipping a new car to customer!
Found faulty car, skipping...
This car is ok.
Shipping a new car to customer!
This car is ok.
Shipping a new car to customer!
'''