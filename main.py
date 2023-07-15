def main():
    todo_list = load_todo_list()

    print("To-Do List Manager!")

    display_todo_list(todo_list)
    
    while True:
        user_input = input("Enter a command: ")

        if user_input == "add":
            add_task(todo_list)
        elif user_input == "delete":
            delete_task(todo_list)
        elif user_input == "complete":
            complete_task(todo_list)
        elif user_input == "display":
            display_todo_list(todo_list)
        elif user_input == "save":
            save_todo_list(todo_list)
        elif user_input == "quit":
            break
        else:
            print("Invalid command. Please try again.")

    print("Exit!")