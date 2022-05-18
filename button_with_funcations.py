from tkinter import * # imports everyting form tk

root =Tk() #top level window
def callback():
    label.config(text="you clicked me!" ,fg="white" , bg="purple")
#here i have added font colour and background colour on click

#create Label
label = Label(root, text="hello python")
label.pack()

#create button(now with the command function)
button= Button(root, text = "click me!", command=callback)
button["state"]="disabled"  #can disable the button
button["state"]="normal" #back to normal
button.pack()

root.geometry("350x300")
root.mainloop()
