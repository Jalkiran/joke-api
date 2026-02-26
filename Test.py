import tkinter as tk
def calculator(fields,title):

    entries={}
#------WINDOWS------
    root=tk.Tk()
    root.title(title)
    root.geometry("400x500")
#-------to get numbers------
    def get_numbers():
       for field in entries:
          value=entries[field].get()
          if value.strip()=="":
             status_label.config(text="All fields must e filled",fg="red")
             return None
       try:
             num1=float(entries["num1"].get())
             num2=float(entries["num2"].get())
             return num1,num2
       except ValueError:
             status_label.config(text="Enter valid numbers",fg="red")
             return None
       
       status_label.config(text="",fg="red")
       return num1,num2
#--------Field-------
    for field in fields:
        label=tk.Label(root,text=field)
        label.pack(pady=5)
        entry=tk.Entry(root)
        entry.pack(pady=5)
        entries[field]=entry

    status_label=tk.Label(root,text="",fg="red")
    status_label.pack(pady=5)
#-------ADD-----------
    def add():
      nums=get_numbers()
      if not nums:
         return
      num1,num2=nums
      result_box.insert(tk.END,num1+num2)
      
    add_btn=tk.Button(root,text="ADD",command=add)
    add_btn.pack(pady=5)
#---------SUBTRACT-------
    def sub():
      nums=get_numbers()
      if not nums:
         return
      num1,num2=nums
      result_box.insert(tk.END,num1-num2)
    sub_btn=tk.Button(root,text="SUBTRACT",command=sub)
    sub_btn.pack(pady=5)   
#--------MULTIPLY------
    def mul():
      nums=get_numbers()
      if not nums:
         return
      num1,num2=nums
      result_box.insert(tk.END,num1*num2)
    mul_btn=tk.Button(root,text="MULTIPLY",command=mul)
    mul_btn.pack(pady=5)  
#--------DIVIDE--------
    def div():
      nums=get_numbers()
      if not nums:
         return
      num1,num2=nums
      if num2==0:
         status_label.config(text="Not divisible by zero",fg="red")
      else:
         result_box.insert(tk.END,num1/num2)
    div_btn=tk.Button(root,text="DIVIDE",command=div)
    div_btn.pack(pady=5)  
      
#--------SUBMIT--------
    def submit():
     data={}
     for field in entries:
        value=entries[field].get()
        '''if value.strip()=="":
            status_label.config(text="All fields mustt be filled",fg="red")
            return'''
        data[field]=value
     '''data[field]=entry.get()'''
     print(data)    
     status_label.config(text="Submitted",fg="green")
     for field in entries:
        entries[field].delete(0,tk.END)
     result_box.delete(0,tk.END)
#------BUTTON------
    submit_btn=tk.Button(root,text="SUBMIT",command=submit)
    submit_btn.pack(pady=5)
#------RESULT------
    result_box=tk.Listbox(root)
    result_box.pack(pady=5)
   
    
   
    root.mainloop()

calculator(["num1","num2"],"calculator")

