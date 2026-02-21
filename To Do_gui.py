import tkinter as tk
tasks=[]

#-------Functions-------
def add_task():
    task=entry.get()

    if task!="":
       tasks.append(task)
       listbox.insert(tk.END,task)
       entry.delete(0,tk.END)

#---------Window----------
root=tk.Tk()
root.title("To Do App")
root.geometry("400x500")

#--------INPUT------------
entry=tk.Entry(root,width=30)
entry.pack(pady=10)

#----------BUTTON---------
add_btn=tk.Button(root,text="Add Task",command=add_task)
add_btn.pack()

#---------LISTBOX--------
listbox=tk.Listbox(root,width=40,height=15)
listbox.pack(pady=20)

root.mainloop()