user_prompt = "Enter a code:"

todo_list = []

while True:
    todo = input(user_prompt).title()
    todo_list.append(todo)
    print(todo_list)
    print('Next...')
