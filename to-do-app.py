
def menu():
    print(f"    Todo List Menu:")
    print(f"    1. View the Tasks")
    print(f"    2. Add a Task")
    print(f"    3. Remove a Task")
    print(f"    4. Mark Complete")
    print(f"    5. Exit")


def add_tasks(user_tasks):
    while True:
        user_task = (input("Enter a new task: ")).strip()
        
        if user_task:
            user_tasks.append(user_task)
            print("Task has been added successfully")
            save_(user_task)
            break
        else:
            print("Enter a valid task. Dont just put spaces")


def view_task(user_tasks):
    if len(user_tasks) == 0:
        print("There are no tasks to display")
        return
    print("Your task are: ")
    for index, task in enumerate(user_tasks, 1):
        print(f"{index}. {task.strip()}")


def remove_task(user_tasks):
    if not user_tasks:
        print("There are no existing tasks to remove")
        return
    view_task(user_tasks)
    while True:
        user_choice = choice()

        if 0 < user_choice <= len(user_tasks):
            user_tasks.pop(user_choice - 1)
            print("Task has been successfully removed")
            return

        print("Invalid choice. Enter a valid task number to remove")


def choice() -> int:
    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            return user_choice
        except ValueError or TypeError:
            print("Invalid choice. Please enter a valid choice")


def complete(user_tasks):
    if not user_tasks:
        print("There are no existing tasks to mark as complete")
        return

    if len(user_tasks) > 0:
        view_task(user_tasks)
        print("Choose one the above tasks to marks a complete")
        user_choice = choice()
        if 0 < user_choice <= len(user_tasks):
            completed = strikethrough(user_tasks[user_choice - 1])
            user_tasks[user_choice - 1] = completed
            print("Task has been marked as complete")


def strikethrough(task):
    return ''.join([char + '\u0336' for char in task])


def save_(user_task):
    with open('mytasks.txt', 'a') as f:
        f.write(user_task + '\n')


def read_():
    with open('mytasks.txt', 'r') as f:
        task_lines = f.readlines()
        tasks = [line.strip() for line in task_lines]
        return tasks


def main():

    user_tasks: list = read_()
    print()
    menu()
    print()
    while True:
        user_choice = choice()
        if user_choice not in range(1, 6):
            continue
        elif user_choice == 2:
            add_tasks(user_tasks)
        elif user_choice == 1:
            view_task(user_tasks)
        elif user_choice == 3:
            remove_task(user_tasks)
        elif user_choice == 4:
            complete(user_tasks)
        else:
            print("Exiting the application")
            exit(code=21)


if __name__ == "__main__":
    main()
