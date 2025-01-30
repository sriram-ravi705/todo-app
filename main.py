from modules.functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        todos.sort()
        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, todo_items in enumerate(todos):
            todo_items = todo_items.strip("\n")
            print(f'{index + 1}-{todo_items.title()}')
        print(f'Total todo: {len(todos)}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + "\n"
            write_todos(todos)
            print('Todo updated')
        except ValueError:
            print("your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            removed_todo = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            write_todos(todos)
            print(f'Todo {removed_todo} removed ')
        except IndexError:
            print("There is not item with the number")
            continue
        except ValueError:
            print("Please enter item number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('action you prefer is not valid')
print('Bye')
