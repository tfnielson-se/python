todos = []
# dir(list) will display all methods available for lists
while True:
    user_action = input("Type Add / Show / Edit / Completed / Exit: ")
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
                print(f"{i}-{item}")

            number = int(input('Type Number of To-Do item to edit: '))

            if number > len(todos) - 1:
                print('item number non-existent')
            else:
                todos[number] = input('Enter edited To-Do item: ')
                print('edit successful:', todos[number])
        case 'completed':
            for i, item in enumerate(todos):
                print(f"{i}-{item}")

            item_completed = int(input('Enter number of completed item: '))

            if item_completed > len(todos) - 1:
                print('item number non-existent')
            else:
                todos.pop(item_completed)
                print('item marked as completed and removed from list')
        case 'exit':
            break
        case _:
            print('Wrong command')

print('Goodbye')