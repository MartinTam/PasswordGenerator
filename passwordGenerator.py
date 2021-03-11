from tkinter import *
import random

root = Tk()
root.geometry('1250x500')
root.title('Password Generator')
# ---------------------------------------------------------

# Title
title = Label(root, text = 'Password Generator', font = ('Comicsans', 20)).grid(row = 0, column = 0, columnspan = 4, pady = 50)

# Lower Case
lowerCaseVar = StringVar()
lowerCaseCheckBox = Checkbutton(root, text = 'Lower Case', variable = lowerCaseVar, onvalue = 'On', offvalue = 'Off')
lowerCaseCheckBox.grid(row = 1, column = 0, padx = 20)
lowerCaseCheckBox.deselect()

# Upper Case
upperCaseVar = StringVar()
upperCaseCheckBox = Checkbutton(root, text = 'Upper Case', variable = upperCaseVar, onvalue = 'On', offvalue = 'Off')
upperCaseCheckBox.grid(row = 1, column = 1, padx = 20)
upperCaseCheckBox.deselect()

# Numbers 
numbersVar = StringVar()
numbersCheckBox = Checkbutton(root, text = 'Numbers', variable = numbersVar, onvalue = 'On', offvalue = 'Off')
numbersCheckBox.grid(row = 1, column = 2, padx = 20)
numbersCheckBox.deselect()

# Special Characters
specialCharVar = StringVar()
specialCharCheckBox = Checkbutton(root, text = 'Special Characters', variable = specialCharVar, onvalue = 'On', offvalue = 'Off')
specialCharCheckBox.grid(row = 1, column = 3, padx = 20)
specialCharCheckBox.deselect()

# Length
lengthTitle = Label(root, text = 'Length: ').grid(row = 2, column = 0, columnspan = 4, pady = (20, 0))
lengthScale = Scale(root, from_ = 1, to = 100, orient = HORIZONTAL)
lengthScale.grid(row = 3, column = 0, columnspan = 4)

# Entry Box to show the password
password = Entry(root, width = 150)
password.grid(row = 5, column = 0, columnspan = 4, padx = 20)


# Check user choices
def checkBoxOn():
    onset = []
    if lowerCaseVar.get() == 'On':
        onset.append(0)
    if upperCaseVar.get() == 'On':
        onset.append(1)
    if numbersVar.get() == 'On':
        onset.append(2)
    if specialCharVar.get() == 'On':
        onset.append(3)
    
    return onset

# Generate the password
def generator():

    # Lists of characters 
    lowerCases = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    specialCharacters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '>', '=', '?', '@', '[', ']', '\\', '^', '_', '`', '{', '}', '|', '~']

    allCases = [lowerCases, upperCases, numbers, specialCharacters]

    generatedPassword = ''

    # Try to generate the password
    try:
        for x in range(0, lengthScale.get()):
            
            userChoice = checkBoxOn()
            randomList = random.choice(userChoice)

            randomChar = allCases[randomList][random.randint(0, len( allCases[randomList] ) - 1 )]
            generatedPassword += randomChar 
    except:
        pass

    # Show the password
    password.delete(0, END)
    password.insert(0, generatedPassword)

# Generate Button
generateButton = Button(root, text = 'Generate', fg = 'white', bg = 'green', command = generator).grid(row = 4, column = 0, columnspan = 4, pady = 40)

# ---------------------------------------------------------
root.mainloop()