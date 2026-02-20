tasks=[]
while True:
    print("\n---TO DO LIST---")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")

    choice=input("Enter Choice:")
    if choice=="1":
       task=input("Enter new task:")
       tasks.append(task)
       print("Task Added!")
    elif choice=="2":
       if len(tasks)==0:
          print("No task yet!")
       else:
          for i , t in enumerate(tasks, start=1):
                print(i, ".", t)
    
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(removed, "deleted!")
        else:
            print("Invalid number")

    # EXIT
    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
      
       