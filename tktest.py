from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, 100)
    e2.delete(0, 100)


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(root, text="First Name").grid(row=0)
ttk.Label(root, text="Last Name").grid(row=1)
e1 = ttk.Entry(root)
e2 = ttk.Entry(root)
e1.insert(10, "Miller")
e2.insert(10, "Jill")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
ttk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=4, 
                                    column=0, 
                                     pady=4)
ttk.Button(root, 
          text='Show', command=show_entry_fields).grid(row=4, 
                                                       column=1, 
                                                      
                                                       pady=4)

root.mainloop()