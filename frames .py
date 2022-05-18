from tkinter import *
root = Tk()
root.title("Frames")

# create frame using frame constructor method
# to make frame visible - use background colour(bg)
frame = Frame (root, height=300, width=300, bg='SkyBlue2')
frame.pack() # using geometry manager for frame
root. geometry("650x650+450+2001")
root.mainloop()
