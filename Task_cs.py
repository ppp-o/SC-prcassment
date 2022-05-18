from tkinter import * # imports everything from TK
from tkinter import ttk

root = Tk()

def callback():
    print("Your first name is :"+entry.get())
    print("Your last name is :"+entry2.get())
    if chvar.get()  == 1:
        print("print not selected")
    else:
        print("print selected")
     

# Create entry boxes
entry = ttk.Entry(root, width=20) # size of the field for entry
entry2 = ttk.Entry(root,width=20)
entry.insert(0, '') # 0 is the index - first character

# Add a button to the window
button = ttk.Button(root, text='Print')
button.config(command=callback)

# add a button named quit 
button2 = ttk.Button(root, text="quit")
button2.grid(row=0, column=1)


lblname = ttk.Label(text='Your first name:')
lblpass = ttk.Label(text='Your last name:')
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=0, column=2, sticky=E, pady=5)

# checkbox
chvar = IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked



root.geometry('500x450') # the size of the window
root.mainloop()
