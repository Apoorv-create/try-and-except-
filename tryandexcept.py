from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("600x400")

list_name = ["Micky Mouse", "Donald Duck", "Jack", "Kate"]
dict_name = {"name" : "tony",
             "age" : "8"}

try:
    print(list_name[5])
    
    print(dict_name["Bucky"])
    
except KeyError:
    messagebox.showinfo("This Name is not specified")
    
except IndexError:
    messagebox.showinfo("This Index is not specified")

root.mainloop()