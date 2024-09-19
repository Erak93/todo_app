import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # this deletes the todo rom session state
        st.rerun() # this reload the checkboxes


st.text_input(label="enter todo ", placeholder="Add new todo...",
              on_change=add_todo,label_visibility="hidden", key="new_todo")


#st.session_state # just to be used in production