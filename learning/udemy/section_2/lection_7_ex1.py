'''
Udemy
The Complete Python Course | Learn Python by Doing in 2025
Exercise: FizzBuzz (Python 3.10)
I'm really excited for this challenge, and you should be too!

This is a common challenge that you could be asked to complete
when you apply for graduate and entry-level programming jobs.
It's not an impossible challenge—I'm sure you'll be able to do it—
but it requires some careful thinking and following the instructions
provided to the letter.

The FizzBuzz challenge

In this exercise, print out 100 numbers, from 1 to 100 (both inclusive).
But:

Instead of printing multiples of 3, print "Fizz"

Instead of printing multiples of 5, print "Buzz"

Instead of printing multiples of both 3 and 5, print "FizzBuzz".

That means your program will print a combination of numbers, Fizz , Buzz , and FizzBuzz .

For example:

1
2
Fizz , since  3 is a multiple of 3
4
Buzz , since  5 is a multiple of 5
Fizz , since  6 is a multiple of 3
7
8
Fizz , since  9 is a multiple of 3
Buzz , since  10 is a multiple of 5
11
Fizz , since  12 is a multiple of 3
13
14
FizzBuzz , since  15 is a multiple of BOTH 3 AND 5
16
17
Fizz , since  18 is a multiple of 3
19
Buzz , since 20 is a multiple of 5
Continue up to (and including) 100

Make sure your program prints from 1 to 100, both inclusive!
'''
# моє нове рішення:
for i in range(1,101):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print('Buzz')


# моє старе рішення:
# Print out numbers from 1 to 100 (including 100).
a_list = [i for i in range(1,101)]
for i in a_list:
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)
# for i in a_list:
#     print(i)
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

# 3 варіант
for i in range(1,101):
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)

# 4 варіант Solution: FizzBuzz
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 5 варіант Артур
arr = [i for i in range(1,101)]
result = [(el % 3 == 0) * 'Fizz'
        + (el % 5 == 0) * 'Buzz'
        + (el % 3 != 0 and el % 5 != 0) * str(el)
        for el in arr]

'''
result = []
for el in arr:
    result.append((el % 3 == 0) * 'Fizz' + (el % 5 == 0) * 'Buzz' + (el % 3 != 0 and el % 5 != 0) * str(el))
result = [el for el in arr]
'''
print(result)