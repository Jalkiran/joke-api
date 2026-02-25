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
    for field in entries:
          value=entries[field].get()
          if value.strip()=="":
              print(f"{field}cannot be empty")
              return 
          data[field]=value
    print(data)
    print("Success!")
    for field in data:
        entry.delete(0,tk.END)
submit_btn=tk.Button(root,text ="Submit",command=submit)
submit_btn.pack(pady=5)
root.mainloop()