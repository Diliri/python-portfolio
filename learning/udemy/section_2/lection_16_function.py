''' Functions in python '''
def greet():        # defining a function
    name = input('Enter your name: ')
    print(f"Hello, {name}!")

greet()

print(name)
'''
Enter your name: Diana's
Hello, Diana's!
Traceback (most recent call last):
  File "/home/DianaListen/udemy/section 2/lection_16_function.py",
line 8, in <module>
    print(name)
          ^^^^
NameError: name 'name' is not defined
'''