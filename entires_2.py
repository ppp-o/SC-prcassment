from tkinter import * # imports everthing from TK
from tkinter import ttk

root=Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("your name is :" +val1)
    print("your password is:" +val2)

#create entry boxes
entry = ttk.Entry(root, width=30) #size of the index
entry2 = ttk.Entry(root, width=30)
entry.insert(0,"please enter your name: ") #0 is the index
entry.config(show="*")

#add a button to the window
button=ttk.Button(root,text="click me!" ,commad=callback)
#when youn put in a commad you need to write a fincation under root

entry.pack()
entry2.pack()
button.pack()
