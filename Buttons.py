from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x400")
# add some widgets avilable inly in tkinter and some in tkinter, we will see the differnce here with the buttons


button1 = Button(root, text="click me!") #button created using tkinter
button2 = ttk.Button(root, text="click me pls!") # button created using ttk
# if you run in now you will see an empty GUI the buttons do not show up,
# have to use geometry manger to be able to see the button, here we will use .pack to show our buttons

button1.pack()
button2.pack()
