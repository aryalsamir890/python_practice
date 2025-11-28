
def add_task():
    name=input("enter the task name:")
    f=open("task.txt","a+")
    f.write(name +"\n")
    f.close()

def view_tasks():
    f=open("task.txt","r")
    data=f.read()
    print(data)
    f.close()

def delete_task():    
    f=open("task.txt","r")
    data=input("enter the task u want to delete:")
    val=f.read()
    newlist=val.split("\n")#returns the list 
    newlist.remove(data)
    f.close()
#     Splits that big string at each newline \n
# Returns a list of strings, one string per line, without the \n
    f=open("task.txt","w")
    for i in newlist:
        f.write(i + "\n")   # each task goes on a new line
    f.close()

choose={
    "1":add_task,
    "2":view_tasks,
    "3":delete_task,
    "5":"exit"
}

print("hello this is a to-do list:")
todo=input("choose what to perform :1.add,2.view,3.delete,4.save,5.exit")
for i in range(50):
    if "5" not in todo:
        choose[todo]()
        todo=input("choose another number!!!!")
    else:
        print("app exited sucessfully!!")
        break



# chatgpts code 
# -----------------------------
# Simple To-Do List CLI
# -----------------------------

TASK_FILE = "task.txt"  # file to store tasks

# Add a new task
def add_task():
    task = input("Enter the task name: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    with open(TASK_FILE, "a") as f:  # append mode
        f.write(task + "\n")
    print(f'Task "{task}" added successfully!')

# View all tasks
def view_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = f.read().splitlines()  # get list of tasks
    except FileNotFoundError:
        tasks = []

    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

# Delete a task
def delete_task():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        print("No tasks to delete.")
        return

    if not tasks:
        print("No tasks to delete.")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            with open(TASK_FILE, "w") as f:
                for t in tasks:
                    f.write(t + "\n")
            print(f'Task "{removed_task}" deleted successfully!')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! Exiting the app.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the app
if __name__ == "__main__":
    main()



    
