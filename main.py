todo_list = []

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action:
        case 'add':
            todo = input('Enter todo: ').strip()
            todo_list.append(todo)
        case 'show' | 'display':
            for index, todo_items in enumerate(todo_list):
                print(index + 1, '-', todo_items.title())
        case 'edit':
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todo_list[number] = new_todo
            print('Todo updated')
        case 'exit':
            break
        case _:
            print("you have entered a wrong command")
print('Bye')
