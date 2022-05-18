#this program shoes grid manger- whivh helps us to orgainse our widgets

from tkinter import *
from tkinter import ttk

root = Tk()

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

# create placeholder
entry.insert(0, "please enter your name")
entry2.insert(0, "please enter your password")

#create button and labels
button = ttk.Button(root, text="enter")
lbltitle = ttk.Label(text="our title here", font=(("Arial"), 22))
lblname = ttk.Label(text="your name:")
lblpass = ttk.Label(text="your password")

#position of the buttons, labels and entries as outcome
lbltitle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1)

root.geometry( '500x400' )
root.mainloop()




                                                    
