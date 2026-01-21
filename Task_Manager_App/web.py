import streamlit as st
from functions import get_todos, write_todo

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    print(todo)
    todos.append(todo)
    write_todo(todos)    
    
todos = get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will increase your productivity")

for todo in todos: 
    st.checkbox(todo)

st.text_input(label= "" ,placeholder="Add a new Todo...",
              on_change=add_todo, key="new_todo")

print('hello')
