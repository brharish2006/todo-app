import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('To-do App',
                   layout=[[label, input_box, add_button]],
                   font= ('Arial', 10))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            newtodo = value['todo'] + '\n'
            todos.append(newtodo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()