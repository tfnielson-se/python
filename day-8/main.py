while True:
    user_action = input("Type Add / Show / Edit / Completed / Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo:') + "\n"

            #  with context manager
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display': # <- BITWISE OR operator
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for i, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{i} - {item}")

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for i, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{i}-{item}")

            number = int(input('Type Number of To-Do item to edit: '))

            if number > len(todos) - 1:
                print('item number non-existent')
            else:
                todos[number] = todos[number].strip('\n')
                todos[number] = input(f"current to-do as: ' {todos[number]} ', please enter edit: ") + '\n'
                print('edit successful:', todos[number])

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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