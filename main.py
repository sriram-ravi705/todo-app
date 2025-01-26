todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = input('Enter todo: ') + "\n"
        with open('files/todo', 'r') as file:
            todo_list = file.readlines()
        todo_list.append(todo)
        todo_list.sort()
        with open('files/todo', 'w') as file:
            file.writelines(todo_list)
    elif user_action.startswith('show'):
        with open('files/todo', 'r') as file:
            todo_list = file.readlines()
        for index, todo_items in enumerate(todo_list):
            todo_items = todo_items.strip("\n")
            print(f'{index + 1}-{todo_items.title()}')
        print(f'Total todo: {len(todo_list)}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            new_todo = input('Enter new todo: ')
            todo_list[number] = new_todo + "\n"
            with open('files/todo', 'w') as file:
                file.writelines(todo_list)
            print('Todo updated')
        except ValueError:
            print("your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            removed_todo = todo_list[number - 1].strip("\n")
            todo_list.pop(number - 1)
            with open('files/todo', 'w') as file:
                file.writelines(todo_list)
            print(f'Todo {removed_todo} removed ')
        except IndexError:
            print("There is not item with the number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('action you prefer is not valid')
print('Bye')
