import streamlit as st
from modules import functions

read_todo = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    read_todo.append(todo)
    functions.write_todos(todo)


st.title("Todo list")
for todo in read_todo:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter Todo", on_change=add_todo, key='new_todo')
