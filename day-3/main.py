todos = []

while True:
    user_action = input("Type Add / Show / Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo:')
            todos.append(todo)
        case 'show' | 'display': # <- BITWISE OR operator
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print('Wrong command')

print('Goodbye')