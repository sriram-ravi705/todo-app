import FreeSimpleGUI
from modules import functions

label = FreeSimpleGUI.Text("Type in a to-do")
input_boc = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")


Window = FreeSimpleGUI.Window("My Gui Todo App", layout=[[label, input_boc], [add_button]],
                              font=('Helvetica', 20))

while True:
    event, values = Window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break

Window.close()
