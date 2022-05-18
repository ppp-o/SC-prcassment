from tkinter import *

root = Tk()
root.title("using Images")
root.geometry("350x350")

# in order to insert create a folder called "icons"
# where your tkinter files are saved and save some icons

# create label
lbl_text = Label(root, text="using images", font=(("Times"), 18))
lbl_text.pack()

#insert image
logo = PhotoImage(file="Icons/photo-camera.png")

#we will create a label to store the image
# which acts as a contanier for our image
lbl_image = Label(root, image=logo)
lbl_image.pack()

root.mainloop()
