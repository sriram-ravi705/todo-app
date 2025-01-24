todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case 'add':
            todo = input('Enter todo: ') + "\n"
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            todo_list.append(todo)
            with open('files/todo', 'w') as file:
                file.writelines(todo_list)
        case 'show' | 'display':
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            for index, todo_items in enumerate(todo_list):
                todo_items = todo_items.strip("\n")
                print(f'{index + 1}-{todo_items.title()}')
            print(f'Total todo: {len(todo_list)}')
        case 'edit':
            number = int(input("number of todo to edit: "))
            number = number - 1
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            new_todo = input('Enter new todo: ')
            todo_list[number] = new_todo + "\n"
            with open('files/todo', 'w') as file:
                file.writelines(todo_list)
            print('Todo updated')
        case 'complete':
            number = int(input("number of todo to completed: "))
            with open('files/todo', 'r') as file:
                todo_list = file.readlines()
            removed_todo = todo_list[number - 1].strip("\n")
            todo_list.pop(number - 1)
            with open('files/todo', 'w') as file:
                file.writelines(todo_list)
            print(f'Todo {removed_todo} removed ')
        case 'exit':
            break
        case _:
            print("you have entered a wrong command")
print('Bye')
