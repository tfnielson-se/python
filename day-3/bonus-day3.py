# Create a program that does the following:
#
# 1. Prompts the user to input the country they are from.
user_input = input('Enter Nationality: ')
user_input = user_input.lower()
# 2. If the user enters the word USA, the program prints out Hello.
match user_input:
    case 'usa':
        print('Hello')
# 3. If the user enters the word  India, the program prints out Namaste.
    case 'india':
        print('Namaste')
# 4. If the user enters the word Germany, the program prints out Hallo.
    case 'germany':
        print('Hallo')
    case _:
        print('Sorry, Language not supported')
