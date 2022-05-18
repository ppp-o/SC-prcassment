from tkinter import * # imports everything from tkinter 
from tkinter import ttk #ttk is a sub module of tkninter

root = Tk() # top level window 

# Create a Label Widget 
label = Label(root, text="Hello Python") #what you see #on screen

# font colour, config is for properties
label.config(text="Hello Python", fg="white")
label.config(bg="purple") #background colour
label.config(font='Times 20')

label.config(text='python is a great program and we can do lots of things with it')
label.config(wraplength="150") #wrap text if long label 
label.config(justify="right")

# showing it on screen
label.pack()
root.geometry("360x250") # size of window you'll see 

root.mainloop() # GUI is always looping when you run your mouse over and you can click on any buttons/labels  
             
