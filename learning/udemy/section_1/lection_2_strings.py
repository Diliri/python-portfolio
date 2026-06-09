'''
Strings

This file talks about strings
'''

string = 'Hello world!'
print(string)

str_with_quotes = "Hello, it's me"  # double quotes
another_with_quotes = 'He said "U r amazing!" yesterday.'
print(another_with_quotes)

another_with_quotes = "He said \"U r amazing!\" yesterday."
# notice back slash \"  names ESCAPING

multiline_string = '''Hello world.

My name's Diana. Welcome to my program.
'''
print(multiline_string)

name = 'Diana'
greeting = 'Hello, ' + name
print(greeting)

age = 28
age_as_a_str = str(age)
print("U r " + age_as_a_str)