#This is a program written by Andrew Taylor
#This program was made to try to learn a bit about tkinter
#This program takes two number and compares them (>, <, or =) and then displays the 
#result using the tkiner canvas in a way that looks like a seven segment display.

import tkinter as tk


#x, y, and z are used for setting the default position of the zeros, because I was too 
#lazy to write +110, +330, and +440 that many times.
x = 110
y = 330
z = 440

#Used to space out the numbers later when writing on the canvas
Spacing = -110

#Ended up making this as a counter to make sure nothing prints when an error appears.
Error = 0

#setting up the default position of the numbers for future use (such as starting and 
#clearing)
def default():
    canvas.create_rectangle(20, 10, 100, 10,) 
    canvas.create_rectangle(10, 20, 10, 100,)
    canvas.create_rectangle(10, 120, 10, 200,)
    canvas.create_rectangle(20, 110, 100, 110)
    canvas.create_rectangle(20, 210, 100, 210)
    canvas.create_rectangle(110, 20, 110, 100)
    canvas.create_rectangle(110, 120, 110, 200)

    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(10+x, 120, 10+x, 200,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)

    canvas.create_rectangle(20+y, 10, 100+y, 10,) 
    canvas.create_rectangle(10+y, 20, 10+y, 100,)
    canvas.create_rectangle(10+y, 120, 10+y, 200,)
    canvas.create_rectangle(20+y, 110, 100+y, 110)
    canvas.create_rectangle(20+y, 210, 100+y, 210)
    canvas.create_rectangle(110+y, 20, 110+y, 100)
    canvas.create_rectangle(110+y, 120, 110+y, 200)

    canvas.create_rectangle(20+z, 10, 100+z, 10,) 
    canvas.create_rectangle(10+z, 20, 10+z, 100,)
    canvas.create_rectangle(10+z, 120, 10+z, 200,)
    canvas.create_rectangle(20+z, 110, 100+z, 110)
    canvas.create_rectangle(20+z, 210, 100+z, 210)
    canvas.create_rectangle(110+z, 20, 110+z, 100)
    canvas.create_rectangle(110+z, 120, 110+z, 200)


#This function clears the text in the entry fields and resets the canvas
def ClearText():
    canvas.delete(tk.ALL)
    default()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    Error = 0

#Creating function that will try to work as exeption handling.    
def UserError():
    canvas.delete(tk.ALL)
    default()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, "Please input a valid")
    entry2.insert(0, "Number")
    Error = Error + 1
    
#All functions named after a number are telling the gui where do draw lines to make 
#numbers
def zero(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(10+x, 120, 10+x, 200,)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)

def one(x):
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def two(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 120, 10+x, 200,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    
def three(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def four(x):
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def five(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 200, 100+x, 200)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def six(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(10+x, 120, 10+x, 200,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def seven(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def eight(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100,)
    canvas.create_rectangle(10+x, 120, 10+x, 200,)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(20+x, 210, 100+x, 210)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)
    
def nine(x):
    canvas.create_rectangle(20+x, 10, 100+x, 10,) 
    canvas.create_rectangle(10+x, 20, 10+x, 100)
    canvas.create_rectangle(20+x, 110, 100+x, 110)
    canvas.create_rectangle(110+x, 20, 110+x, 100)
    canvas.create_rectangle(110+x, 120, 110+x, 200)

    
#The functions named after booleans are all in fixed positions because there is only
# ever one place they should be.
def GreaterThan():
    canvas.create_line(310, 50, 390, 100)
    canvas.create_line(310, 150, 390, 100)

def LessThan():
    canvas.create_line(390, 50, 310, 100)
    canvas.create_line(390, 150, 310, 100)
    
def EqualTo():
    canvas.create_line(310, 75, 390, 75)
    canvas.create_line(310, 125, 390, 125)
    

#Making a command for later, that converts the numbers and booleans into a canvas #drawing    
def CharIdentity(Character, Spacing):
    if Character == '0':
        zero(Spacing)
        
    elif Character == '1':
        one(Spacing)
        
    elif Character == '2':
        two(Spacing)
        
    elif Character == '3':
        three(Spacing)
        
    elif Character == '4':
        four(Spacing)
        
    elif Character == '5':
        five(Spacing)
        
    elif Character == '6':
        six(Spacing)
        
    elif Character == '7':
        seven(Spacing)
        
    elif Character == '8':
        eight(Spacing)
        
    elif Character == '9':
        nine(Spacing)
        
    elif Character == ">":
        GreaterThan()
        
    elif Character == "<":
        LessThan()
        
    elif Character == "=":
        EqualTo()
        
    else:
        UserError()
        Sentence = ''

#Clears canvas, and takes input from entry boxes, then compares them (>, <, or =)        
def Compare(Spacing):
        canvas.delete(tk.ALL)
        Number1 = entry1.get()
        Number2 = entry2.get()

        #This was implemented April 30th to fix a bug where 3 would look > 22.
        #Also fixes an error with the visuals where the second value of the second
        #Number wouldn't 'print' if the first number was single digit
        if int(Number1) < 10:
            Number1 = '0'+Number1
        else:
            pass
        if int(Number2) < 10:
            Number2 = '0'+str(Number2)
        else:
            pass
        Error = 0

        print(Number1)
        print(Number2)
    
        if Number1 > Number2:
            Sentence = str(Number1)+">"+str(Number2)
            print("one")
        elif Number1 < Number2:
            Sentence = str(Number1)+"<"+str(Number2)
            print("two")
        else:
            Sentence = str(Number1)+"="+str(Number2)
            print("three")

        #This prints to termnial, just as a quick check that the code works.
        print(Sentence)
        
        #Calls that conversion function previously defined, and adds spacing for each 
        #number
        for x in Sentence:
            print(x)
        
            #If there is one erro while printing, this makes sure nothing extra will print
            if Error == 1:
                pass
                #Properly moves the starting number closer if it is single digit as opposed 
                #to double digit
            else:
                while x == str(Number1):
                    if len(str(Number1)) == 1:
                        Spacing = Spacing + 110
                        break
                    elif len(str(Number1)) == 2:
                        Spacing = -110
                
                    #Preventing more than 2 characters from being entered
                    elif len(str(Number1)) > 2:
                        UserError()
                    
                #Preventing more than 2 characters from being entered.
                if len(str(Number2)) > 2:
                    UserError()
                else:
                    pass
                
                if Spacing == 220:
                    Spacing = Spacing + 220
                else:
                    Spacing = Spacing + 110
                CharIdentity(x, Spacing)
        
#Creating a genericly named window in tkinter
window = tk.Tk()

#Replacing that awful default grey with white.
window.configure(background='white')

#Labeling the entry boxes so you know what you are supposed to be entering
tk.Label(window, text="First Number").grid(row=0)
tk.Label(window, text="Second Number").grid(row=1)

#Creating the prevoiusly mentioned entry boxes and placing them next to the 
#appropriate labels
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


#Creating the canvas where the drawn out numbers go
canvas = tk.Canvas(window, width=670, height=220, bg='white')
canvas.grid(row=2)

#Setting the canvas to be all zeros
default()

    
#Creating buttons that compare the values of the text boxes, quit the program, or clear 
#the text while reseting the canvas.
CompareButton = tk.Button(window, text="Compare", command=lambda: Compare(Spacing))
ClearButton = tk.Button(window, text="Clear", command=lambda: ClearText())
QuitButton = tk.Button(window, text="Quit", fg='red', bg='white', command=quit)

CompareButton.grid(row=0, column=2)
ClearButton.grid(row=1, column=2)
QuitButton.grid(row=3, column=2)

#Opening the window
window.mainloop()


#TEST
'''
First Number = 1
Second Number = 2

*Press Compare*

The "Display" shows 1 < 2
'''
