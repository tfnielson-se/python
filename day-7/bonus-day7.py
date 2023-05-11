# Coding Exercise 1
names = ["john smith", "jay santi", "eva kuki"]

# Extend the code above so the code capitalizes all the names and surnames of the list and then prints the new list.
# The output of your code should be as below:
# ['John Smith', 'Jay Santi', 'Eva Kuki']
names = [name.title() for name in names]
print(names)

# Coding Exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]

# Extend the code above so the code prints out a list containing the number of characters for each username.
# The output of your code should be as below:
# [9, 11, 11]
username_length = [(len(username)) for username in usernames]
print(username_length)

# Coding Exercise 3
user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out a list containing the same items as floats.
# The output of your code should be as below:
# [10.0, 19.1, 20.0]
user_entries = [float(entry) for entry in user_entries]
print(user_entries)

# Coding Exercise 4
user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.
# The output of your code should be as below:
# 49.1

# entry_sum = 0
# for entry in user_entries:
#     entry_sum += float(entry)
#
# print(entry_sum)

entry_sum = [(float(entry)) for entry in user_entries]
print((sum(entry_sum)))
# Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all numbers. For more info, try help(sum).
