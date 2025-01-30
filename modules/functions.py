def get_todos(file_path='files/todo'):
    """ Read a text file and return the todo list item """
    with open(file_path, 'r') as files:
        todo_local = files.readlines()
    return todo_local


def write_todos(todos, file_path='files/todo'):
    """ Get todo list item and write in a text file """
    with open(file_path, 'w') as files:
        files.writelines(todos)


print('outside of the main function, i wont run when /'
      'this module is called')
if __name__ == 'main':
    print('inside of the main function, i wont run when /'
          'this module is called')
