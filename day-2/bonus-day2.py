def ask_name():
    user_input = input("Enter name: ")
    return user_input

# Create a program that prompts the user to input their name once.
# Then, the program prints out the name once with the first letter capitalized.


user = ask_name().capitalize()
print(user)


# Create a program that prompts the user to input their name once.
# Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
    print(user)


# Create a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
    user = ask_name().capitalize()
    print(user)