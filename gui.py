import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events= True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window('To-do App',
                   layout=[[label, input_box, add_button], [list_box, edit_button, complete_button],[exit_button]],
                   font= ('Arial', 10))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            newtodo = value['todo'] + '\n'
            todos.append(newtodo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_edit = value["todos"][0]
            newtodo = value['todo']

            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = newtodo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Complete:":
            todo_to_complete = value['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=value['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()