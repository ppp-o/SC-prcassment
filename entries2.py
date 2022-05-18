from tkinter import * #imports everything form TK
from tkinter import ttk

root=Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :" +val1)
    print("Your password is :" +val2)

#Create entry boxes
entry = ttk.Entry(root, width=30)  #size of the field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "please enter your name") #0 is the index - first character
entry2.config(show='*') #this will hide the password for the text entered

#add a button to the window
button=ttk.Button(root,text='Click me!' ,command=callback)
#when you put in a command you need to write a function under root


entry.pack()
entry2.pack()
button.pack()
