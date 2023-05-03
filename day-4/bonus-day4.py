# How to edit strings
filenames = ['1.item', '2.item', '3.item']

#use .replace function
for filename in filenames:
    filename = filename.replace('.', '-')
    print(filename)

# Create a program that:

# 1. Prompts the user to input a (dollar) amount.
dollar_amount = int(input('Enter $ amount: '))
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
dollar_amount = dollar_amount * 0.95

# 3. Prints out the amount in euros, as shown in the screenshot below.
print('$EU: ', dollar_amount)