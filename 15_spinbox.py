'''In this program, we will create a function for our button so when you hit the button you can get the values entered.'''

from tkinter import *
from tkinter import ttk

root=Tk()

def callback(): #callback function for outcome
    print("Your name: " + entry.get())
    print("Your password: " + entry2.get())
    if chvar.get()== 1: #means the checkbox is checked
        print("Remember Me - selected")
    else:
        print("Remember Me - not selected")
    print("Your gender: " + gender.get()) #gender value to show when we run the program
    print(months.get())
    print(year.get())

#create entry boxes
entry = ttk.Entry(root, width=30) #size of field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, " ") #0 is the index, first character
entry2.insert(0, " ")

#add a button to the window
button = ttk.Button(root, text="Enter")
button.config(command=callback) #**configuring button with the callback function**

#add lablel title
lbltitle = ttk.Label(text="Our Title Goes Here", font=(("Arial"),22))

lblname = ttk.Label(text="Your name: ")
lblpass = ttk.Label(text="Your password: ")
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

#checkbox
chvar = IntVar() #checkbox variable
chvar.set(0) #set to 0 (zero) means not checked

#checkbox variable
cbox = Checkbutton(root, text="Remember Me", variable=chvar,
                   font="Arial 16").grid(row=4,column=0, sticky=E, columnspan=2) #in order to align it to the right

#create another variable
gender = StringVar()

#create radio button
#to get value from our radio button - in the callback function
ttk.Radiobutton(root, text="Female", value="Female", var=gender).grid(row=5,column=0)
ttk.Radiobutton(root, text="Male", value="Male",var=gender).grid(row=5,column=1)

"""create comobox where our frist paramter will be root and the secound will be textvariabe
(months) and use grid geomentry map for the comobox (where it will be on the window)
when the appiaction is run teh combo box is empty need ti create varables for our combo
box which will we will do now"""
months= StringVar() # StringVar is my function
ComboBox = ttk.Combobox(root, textvariable=months,
                         values=("jan", "feb", "mar", "apr")).grid(row=6, column=0)

#there is a problem that when we run the program and click on the months
#we can actually write over ot and delete it

"""ComoboBox = ttk.Comobobox(root, textvariable=months,
                       values=("jan", "feb", "mar", "apr"),
                       state="readonly").grid(row=6, column=0)"""
# tuple of values

#create a spinbox- from is a special keyword for python so we need to use_after it
year = StringVar()
Spinbox(root,from_=1900, to=2022,textvariable=year,state="readonly").grid(row=6,column=1)
#use grid geometry manager to use our window but we aew able to edit the values in the spinbox so you need to add the "readonly" function for spinbox
#Spinbox(root, from_1990, to=2022, textvariable=year, state="readonly").grid(row=6, column=1)
#to get teh value to print out whne the program is run add a print statement in function (print(year.get())



root.geometry("500x450") #size of window
root.mainloop()

