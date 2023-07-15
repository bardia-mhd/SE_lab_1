def main():

    task_manager = TaskManager()

    while True:
        print("Commands: add <task>, done <task index>, delete <task index>, list, clear, quit")
        command = input("> ").split()
        operation = command[0]

        if operation == "add":
            task_manager.add(' '.join(command[1:]))
        elif operation == "delete":
            task_manager.delete(int(command[1]))
        elif operation == "done":
            task_manager.mark_done(int(command[1]))
        elif operation == "list":
            task_manager.list_tasks()
        elif operation == "clear":
            task_manager.clear()
        elif operation == "quit":
            break

if __name__ == "__main__":
    main()