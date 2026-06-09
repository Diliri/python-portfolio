''' Introduction to list slicing '''
# 1 example
friends = ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen']

print(friends[2:4])     # ['Anna', 'Bob']
print(friends[1:])      # ['Charlie', 'Anna', 'Bob', 'Jen']
print(friends[:2])      # ['Rolf', 'Charlie']
print(friends[:])       # it is a NEW LIST!
                        # ['Charlie', 'Anna', 'Bob', 'Jen']
print(friends[-3:])     # counting from the end
                        # ['Anna', 'Bob', 'Jen']
print(friends[:-2])     # ['Rolf', 'Charlie', 'Anna']
print(friends[-3:-1])   # ['Anna', 'Bob']