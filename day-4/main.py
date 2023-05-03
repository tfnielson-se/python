todos = []

while True:
    user_action = input("Type Add / Show / Edit / Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo:')
            todos.append(todo)
        case 'show' | 'display': # <- BITWISE OR operator
            for item in todos:
                print(item)
        case 'edit':
            for i, item in enumerate(todos):
                print(i, item)

            number = int(input('Type Number of To-Do item to edit: '))

            if number > len(todos) - 1:
                print('item number non-existent')
            else:
                todos[number] = input('Enter edited To-Do item: ')
                print('edit successful:', todos[number])
        case 'exit':
            break
        case _:
            print('Wrong command')

print('Goodbye')