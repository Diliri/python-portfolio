# Моє старе рішення:
# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.


# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...
user_input = input("Please, enter 'p' to see 'Hello' or 'q' to terminate the program")

# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
while user_input != 'q':
    if user_input == 'p':
        print('Hello')
    user_input = input("Please, enter 'p' to see 'Hello' or 'q' to terminate the program")
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...

# Рішення викладача
user_input = input("Enter q or p: ")

# Now we must repeat until they type 'q':
while user_input != "q":
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == "p":
        print("Hello")
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input = input("Enter q or p: ")