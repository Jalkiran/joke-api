import tkinter as tk
entries={}
fields=["field1","field2","field3"]
root=tk.Tk()
root.title("Forms")
root.geometry("400x500")
for field in fields:
    label=tk.Label(root,text ="Field")
    label.pack(pady=5)
    entry=tk.Entry(root)
    entry.pack(pady=5)
    entries[field]=entry



def submit():
    data={}
    for fields in entries:
        data=entries[field].get()
    print(data)

submit_btn=tk.Button(root,text ="Submit",command=submit)
submit_btn.pack(pady=5)
root.mainloop()