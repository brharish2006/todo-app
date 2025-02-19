from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Add, Show, Edit, Complete or Exit? ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        new_todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(new_todo)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index+1}-{todo}"
            print(row)
        print(f"Total number of todos: {len(todos)}")

    elif user_action.startswith("complete"):
        try:
            user_complete_number = int(user_action[9:]) - 1

            todos = get_todos()

            todo_to_remove = todos[user_complete_number].strip('\n')
            todos.pop(user_complete_number)

            write_todos(todos)

            print(f"Todo {todo_to_remove} was removed.")

        except IndexError:
            print("Task not found.")
        continue

    elif user_action.startswith("edit"):
        try:
            number = user_action[5:]
            number = int(number)

            todos = get_todos()

            number = number - 1
            todos[number] = input("Edited todo: ") + '\n'

            write_todos(todos)

        except ValueError:
            print("Command is invalid.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command invalid. Try again.")

print("Exit successful.")