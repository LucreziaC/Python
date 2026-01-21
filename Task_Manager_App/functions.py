import os
import sys

BASE_DIR = os.path.dirname(sys.executable)
FILEPATH = os.path.join(BASE_DIR, "todos.txt")

def get_todos(filepath=FILEPATH):
    """read a text file and return the list of to-do items
    Args:
        filepath (str, optional): _description_. Defaults to "todos.txt".
    Returns:
        _type_: _description_
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todos_arg, filepath="todos.txt") :
    """Write the todo items list in the text file.
    Args:
        todos_arg (_type_): _description_
        filepath (str, optional): _description_. Defaults to "todos.txt".
    """
    with open(filepath, "w") as file:
            file.writelines(todos_arg)  