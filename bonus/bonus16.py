import FreeSimpleGUI

to_file_label = FreeSimpleGUI.Text("Select files to compress: ")
to_file_input = FreeSimpleGUI.InputText()
to_button = FreeSimpleGUI.FolderBrowse("Choose")

from_file_label = FreeSimpleGUI.Text("Select files from compress: ")
from_file_input = FreeSimpleGUI.InputText()
from_button = FreeSimpleGUI.FolderBrowse("Choose")

compress_button = FreeSimpleGUI.Button("Compress")

window = FreeSimpleGUI.Window("File Zipper",
                              layout=[[to_file_label, to_file_input, to_button],
                                      [from_file_label, from_file_input, from_button], [compress_button]])
window.read()
window.close()
