# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
name = input('Enter you name: ')
print(f'Hello, {name.title()}')
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
age = input('What is your age?')
print(f'You have lived fotd for {int(age)*12} months')



# Solution: communicating with users

# First, as the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!
user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
user_age = int(input("Enter your age: "))
print(user_age * 12)