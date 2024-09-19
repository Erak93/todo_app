from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"  # slicing after add and space

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif 'show' in user_action:

        todos = get_todos()

        # new_todos = []
        # for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append((new_item)) # this is to avoid the double space line. a for loop automatically create a break line but we added a /n ourselves when user type add

        # new_todos = [item.strip("\n") for item in todos] # better use a list comprehension

        for index, item in enumerate(todos):
            item = item.title().strip("\n")
            print(f'{index + 1}.{item}')

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])  # slicing after edit and space
            number = number - 1  # this is because the user does not know list indexing

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:  # if user does not write todo number instead of Value error the code below will run
            print("Your command is not valid")
            continue  # while loop continues


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])  # slicing after complete and space

            todos = get_todos()
            todo_to_remove = todos[number - 1].strip("\n")

            number = number - 1  # this is because the user does not know list indexing
            todos.pop(number)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:

            # just in case the user enters a number out of range
            print("There is no item with that number")
            continue
    elif 'exit' in user_action:
        print("Bye")
        break
    else:
        print("Command is not valid")

