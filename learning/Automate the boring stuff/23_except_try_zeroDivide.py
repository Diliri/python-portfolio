''' except and try instruction '''
# 1 example
'''
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

          ~~~~^^^
  File "/home/DianaListen/Automate the boring
stuff/23_except_try_zeroDivide.py", line 4, in
 spam
    return 42 / divideBy
           ~~~^~~~~~~~~~
ZeroDivisionError: division by zero
'''

# 2 example
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))      # 21.0
print(spam(12))     # 3.5
print(spam(0))
# Error: Invalid argument.
# None
print(spam(1))      # 42.0



