import functions
import streamlit as st

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key="todo"+str(index))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state["todo"+str(index)]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="A new todo",
              on_change=add_todo, key="new_todo")