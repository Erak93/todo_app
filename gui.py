import functions
import FreeSimpleGUI as sg
import time
import os
import sys
sys.path.append(r"C:\Users\giann\PycharmProjects\todo_app\todo_app\functions.py")

if not os.path.exists("files/todo.txt"): # if file does not exists, it gets created
    with open("files/todo.txt","w") as file:
        pass

sg.theme("DarkBlue11")

clock = sg.Text("",key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10]) # dropdown menu
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]], # items put in innersquare brackets will be placed in one row
                   font=('Helvetica', 15))

while True: # without the loop the program will close after any interaction

    event,values =window.read(timeout=10)  # displays window on the screen. Returns a tuple (event,values) # time displayed every 10 millisecond
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    #print(event)
    #print(values)

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 15))

    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 15))

    elif event == "Exit":
        break

    elif event == "todos":
        window['todo'].update(value=values['todos'][0])

    elif event == sg.WIN_CLOSED:
        exit()

window.close()




