tasks = []

# Load tasks
try:
    with open("tasks.txt", "r",encoding="utf-8") as f:
        tasks = f.read().split("\n")
        if tasks == [""]:
            tasks = []
except:
    tasks = []

while True:
    print("\n---TO DO LIST---")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Mark task complete")
    print("5.Exit")

    choice = input("Enter Choice: ")

    # ADD
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)

        with open("tasks.txt","w",encoding="utf-8") as f:
            f.write("\n".join(tasks))

        print("Task Added!")

    # VIEW
    elif choice == "2":
        if not tasks:
            print("No task yet!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, ".", t)

    # DELETE
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)

            with open("tasks.txt", "w",encoding="utf-8") as f:
                f.write("\n".join(tasks))

            print(removed, "deleted!")
        else:
            print("Invalid number")

    # MARK COMPLETE
    elif choice == "4":
        num = int(input("Enter task to be marked as done: "))
        if 1 <= num <= len(tasks):

            if not tasks[num-1].startswith("✅"):
                tasks[num-1] = "✅ " + tasks[num-1]

            with open("tasks.txt", "w",encoding="utf-8") as f:
                f.write("\n".join(tasks))

            print("Task Marked Complete")
        else:
            print("Invalid task")

    # EXIT
    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")