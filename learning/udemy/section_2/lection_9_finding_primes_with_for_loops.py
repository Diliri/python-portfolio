''' finding primes with for loops '''

# 1 example
for n in range(2,10):       # 5
    for x in range(2,n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print('f{n} is a prime number.')

# 2 example
import math

for n in range(2,10):       # Erastothenes' sieve (решето Ератосфена)
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number.')

'''
2 is a prime number.
3 is a prime number.
4 equals 2 * 2
5 is a prime number.
6 equals 2 * 3
7 is a prime number.
8 equals 2 * 4
9 equals 3 * 3
'''