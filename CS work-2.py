from tkinter import * #imports everything fomr TK

root = Tk() # top level window

# create Label
label = Label(root, text="hello python")
label.pack()

# create button(without command does not do anything)
button = Button(root, text="click me!")
button.pack()

root.geometry("350x300")
root.mainloop() # this is always at the end of the code 
