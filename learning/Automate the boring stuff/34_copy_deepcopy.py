# COPY vs DEEPCOPY
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)     # ['A', 'B', 'C', 'D']
print(cheese)   # ['A', 42, 'C', 'D']

spam = [['A', 'B', 'C'], [1,2,3,4,5]]
cheese = copy.copy(spam)
cheese[1][0] = 32
print(spam)     # [['A', 'B', 'C'], [32, 2, 3, 4, 5]]
print(cheese)   # [['A', 'B', 'C'], [32, 2, 3, 4, 5]]

spam = [['A', 'B', 'C'], [1,2,3,4,5]]
cheese = copy.deepcopy(spam)
cheese[1][0] = 32
print(spam)     # [['A', 'B', 'C'], [1, 2, 3, 4, 5]]
print(cheese)   # [['A', 'B', 'C'], [32, 2, 3, 4, 5]]