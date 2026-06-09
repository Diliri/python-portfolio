'''
String formatting

This file talks about string formatting
'''
 # instead of
 # age = 28
 # age_as_a_str = str(age)
 # print("You are " + age_as_a_str)

age = 28

# for Python 3.6 and above
print(f"You are {age}")

# f-string also have a next problem
name = 'Kateryna'
greeting = f"How are you, {name}?"
print(greeting) # will be "How are you, Kateryna?"

name = 'Diana'
print(greeting) # also will be "How are you, Kateryna?"

# How to solve it

name = 'Diana'
final_greeting = 'How are you, {}?' # without F !!!
dianas_greeting = final_greeting.format(name)
print(dianas_greeting)

katerinas_greeting = final_greeting.format('Kateryna')
print(katerinas_greeting)

# OR

name = 'Diana'
final_greeting = 'How are you, {name}?' # without F !!!
dianas_greeting = final_greeting.format(name = 'Diana')
print(dianas_greeting)

# OR

name = 'Diana'
final_greeting = 'How are you, {friend_name}?' # without F !!!
dianas_greeting = final_greeting.format(friend_name = name)
print(dianas_greeting)

# OR

name = 'Diana'
final_greeting = 'How are you, {}?' # without F !!!
print(final_greeting.format(name))

# Conclusion: f-string is simplier,
# but if you want to reuse a template - than format method is better.