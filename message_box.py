"""in this program we will create a meassage box"""

# from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
# if we do not import we can not use meassge box for our applictaion
from tkinter import messagebox


root = Tk()


def callback():
    #1st parmrter will be title and then the text
    mbox = messagebox.askquestion("Delete", "Are you sure?", icon="warning")
    #can change icon by adding, icon="warning")
    if mbox == "yes" : 
        print("Deleted")
    else:
        print("Not deleted")


def callback2():
    messagebox.showinfo("Succes", "Well Done!")
    print("You clicked OK!")


button1 = ttk.Button(root, text="Delete", command=callback).grid(row=3, column=3)
#  command will be defintion name will but will need function
button2 = ttk.Button(
root, text="Info", command=callback2).grid(row=3, column=4)
# can not run without function


root.geometry("350x250")
root.mainloop()
