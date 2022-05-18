#In this program we witt learn how to use Place Geometry Manager.
#Place Geometry Manager allows us exact control over thewidget locations
#and sizes.We can use absolute position and size for our widgets
#We will create a login form for our application"''"

from tkinter import *

root = Tk()

title = Label(root,text="Place Geometry Manager",
              font=( ("Verdana"), 15))
name_txt = Label(root,text="Name :")
pass_txt = Label(root, text="Password :")
name_input = Entry(root, width=30)
pass_input = Entry(root, width=30)

# create button
button = Button(root, text='Save')

# Use Geometry Manager to show our widgets
title.place(x=100, y=20) #x and y are in pixels - and that
# distance from the edges of the window.
# Run your application to see the placement of the widget.

# palcement of other widgets
name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)
pass_txt.place(x=20,y=110)
pass_input.place(x=100, y=110)

# placement of button
button.place(x=250, y=150)

root.geometry("450x450+650+350")
# here the 650+350 means that we
# will locate our window on our screen. This means our tkinter window's
#x location is 650 and y location

#button2.place(x=300, y=300)

# Create a Label Widget 
button = Button(root, text="click me!") #what you see #on screen

# font colour, config is for properties
button.config(text="Click me!", fg="white",bg="red")
#button.config(bg="red") #background colour
button.config(font='Times 20')
button.place(x=400, y=400) #placement needs to be fixed 


# showing it on screen
button.pack()
root.geometry("360x250") # size of window you'll see 

root.mainloop()

#You also need to write a callback function for the labels and the buttons created.
