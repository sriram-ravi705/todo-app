# todo_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case 'add':
            todo = input('Enter todo: ') + "\n"

            file = open('files/todo', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open('files/todo', 'w')
            file.writelines(todo_list)
            file.close()
        case 'show' | 'display':
            file = open('files/todo', 'r')
            todo_list = file.readlines()
            file.close()

            for index, todo_items in enumerate(todo_list):
                todo_items = todo_items.strip("\n")
                print(type(todo_items))
                print(f'{index + 1}-{todo_items.title()}')
            print(f'Total todo: {len(todo_list)}')
        case 'edit':
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todo_list[number] = new_todo
            print('Todo updated')
        case 'complete':
            number = int(input("number of todo to completed: "))
            todo_list.pop(number - 1)
            print('Todo updated')
        case 'exit':
            break
        case _:
            print("you have entered a wrong command")
print('Bye')
