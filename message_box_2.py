"""In this program we are going to create a text editor using Tkinter"""

from tkinter import *

root= Tk()
textEditor = Text(root, width=30, height=10,)# 1st parameter is root
textEditor.grid(row=0, column=0, pady=20, padx=40)

button = Button(root, text='Save') # can use height and width properties
# for our button - button = Button(root, text='Save'width=10, height=1)

button.grid(row=3, column=0)

root.geometry("550x550")
root.mainloop() 
