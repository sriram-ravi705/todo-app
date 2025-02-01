import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_boc = FreeSimpleGUI.InputText(tooltip="Enter todo")
add_button = FreeSimpleGUI.Button("Add")

Window = FreeSimpleGUI.Window("My Gui Todo App", layout=[[label, input_boc],[add_button]])
Window.read()
Window.close()
