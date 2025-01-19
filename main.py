todo_list = []

while True:
    user_action = input("Type add. show, or exit: ")

    match user_action:
        case 'add':
            todo = input('Enter todo: ').strip()
            todo_list.append(todo)
        case 'show' | 'display':
            for todo_items in todo_list:
                print('-', todo_items.title())
        case 'exit':
            break
        case _:
            print("you have entered a wrong command")
print('Bye')
