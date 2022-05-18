#user input
your_name = input("Enter your name: ")
your_age = int(input("Enter your age: "))
#use int(input to have only integers and remember to close brackets

#defining the function
def say_hi():
    print("Hello" , your_name , "you are" , your_age)

#these brackets are to add a new line
print()
#calling the funcion
say_hi()
