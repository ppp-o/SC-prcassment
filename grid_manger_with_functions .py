#this program shoes grid manger- whivh helps us ti orgainse our widgets

from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print("your name is : " + val1)
    print("your password is : " + val2)

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)


# create placeholder
entry.insert(0, "please enter your name")
entry2.insert(0, "please enter your password")

#create button and labels
button = ttk.Button(root, text="enter", command=callback)
lbltitle = ttk.Label(text="our title here", font=(("Arial"), 22))
lblname = ttk.Label(text="your name:")
lblpass = ttk.Label(text="your password")

#position of the buttons, labels and entries as outcome
lbltitle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E+W) #E+W spans it across yhe cell in that column 
button.grid(row=3, column=1, sticky=E) # this will have the button on the right 
button.grid(row=3, column=1, sticky=W) #this will put button on the left side 
button.grid(row=3, column=3, sticky=E, pady=5) 

#checkbox
chvar = IntVar() # cheakbox variable 
chvar.set(0) # set 0 to (zero) - means not cheeaked

#cheakbox variable - a box you can tick or not 
cbox = Checkbutton(root, text="Remember Me", variable=chvar,
font="Arial 16").grid(row=4, column=0)
# sticky=E, columnspan=2 # in order to get it algin right 

root.geometry( '500x400' )
root.mainloop()
