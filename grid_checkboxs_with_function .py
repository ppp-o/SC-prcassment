from tkinter import * # imports everything from TK
from tkinter import ttk

root = Tk()

def callback():
    print("Your Name is :"+entry.get())
    print("Your Password is :"+entry2.get())
    if chvar.get()  == 1:
        print("remember not selected")
    else:
        print("not selected")
     

# Create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0, 'Please enter your name:') # 0 is the index - first character

# Add a button to the window
button = ttk.Button(root, text='Enter')
button.config(command=callback)

# Add label title
lbltitle = ttk.Label(text='Our Title Goes Here', font=(('Arial'), 22))

lblname = ttk.Label(text='Your Name:')
lblpass = ttk.Label(text='Your Password:')
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E, pady=5)

# checkbox
chvar = IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# checkbox variable
cbox = Checkbutton(root, text="Remember Me", variable=chvar,
font="Arial 16").grid(row=4, column=0)
# sticky=E, columnspan=2 # in order to get it algin right

root.geometry('500x450') # the size of the window
root.mainloop()

