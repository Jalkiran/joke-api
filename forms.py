
import tkinter as tk 
def create_forms(fields,title):
 
 entries={} 
 #--------WINDOWS----- 
 root=tk.Tk()
 root.title(title) 
 root.geometry("400x500")
 #-------Field------- 
 for field in fields:
  label=tk.Label(root,text= field) 
  label.pack(pady=5) 
  entry=tk.Entry(root) 
  entry.pack(pady=5) 
  entries[field]=entry 
#--------SUBMIT-------- 
 status_label=tk.Label(root,text="",fg="red")
 status_label.pack(pady=5)
 def submit(): 
     data={} 
     for field in entries:
         value=entries[field].get()
         if value.strip()=="":
             status_label.config(text="All fields must be filled",fg="red")
             return
         data[field]=value
     print(data)
     status_label.config(text="Submitted",fg="green")
     for field in entries:
         entries[field].delete(0,tk.END)
#-------BUTTON---------
 submit_btn=tk.Button(root,text="Submit",command= submit)
 submit_btn.pack(pady=5) 

 root.mainloop()

create_forms(["Name","Age","DOB","Gmail","Contact"],"Reusable forms")
