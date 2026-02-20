tasks=[]
#Load Tasks when file starts
try:
    f=open("tasks.txt","r")
    tasks=f.read().split("\n")
    if tasks==[" "]:
        tasks=[]
    f.close()
except:
    tasks=[]

while True:
    print("\n---TO DO LIST---")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    
    #ADD TASKS
    choice=input("Enter Choice:")
    if choice=="1":
       task=input("Enter new task:")
       tasks.append(task)

       #SAVE
       f=open("tasks.txt","w")
       f.write("\n".join(tasks))
       f.close()

       print("Task Added!")

    #VIEW TASKS
    elif choice=="2":
       if len(tasks)==0:
          print("No task yet!")
       else:    
         for i , t in enumerate(tasks, start=1):
                print(i, ".", t)
    
    #DELETE TASKS 
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)

            f=open("tasks.txt","w")
            f.write("\n".join(tasks))
            f.close()

            print(removed, "deleted!")
        else:
            print("Invalid number")

    # EXIT
    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")

print("Hehe Guys(winks)")