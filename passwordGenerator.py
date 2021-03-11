from tkinter import *
import random

root = Tk()
root.geometry('800x500')
root.title('Password Generator')
# ---------------------------------------------------------

# Title
title = Label(root, text = 'Password Generator', font = ('Comicsans', 20)).grid(row = 0, column = 0)

# Lower Case
lowerCaseVar = StringVar()
lowerCaseCheckBox = Checkbutton(root, text = 'Lower Case', variable = lowerCaseVar, onvalue = 'On', offvalue = 'Off')
lowerCaseCheckBox.grid(row = 1, column = 0)
lowerCaseCheckBox.deselect()

# Upper Case
upperCaseVar = StringVar()
upperCaseCheckBox = Checkbutton(root, text = 'Upper Case', variable = upperCaseVar, onvalue = 'On', offvalue = 'Off')
upperCaseCheckBox.grid(row = 1, column = 1)
upperCaseCheckBox.deselect()

# Numbers 
numbersVar = StringVar()
numbersCheckBox = Checkbutton(root, text = 'Numbers', variable = numbersVar, onvalue = 'On', offvalue = 'Off')
numbersCheckBox.grid(row = 1, column = 2)
numbersCheckBox.deselect()

# Special Characters
specialCharVar = StringVar()
specialCharCheckBox = Checkbutton(root, text = 'Special Characters', variable = specialCharVar, onvalue = 'On', offvalue = 'Off')
specialCharCheckBox.grid(row = 1, column = 3)
specialCharCheckBox.deselect()

# Length
lengthTitle = Label(root, text = 'Length: ').grid(row = 2, column = 0)
lengthScale = Scale(root, from_ = 1, to = 100, orient = HORIZONTAL)
lengthScale.grid(row = 2, column = 1)

# Generate Button
generateButton = Button(root, text = 'Generate').grid(row = 3, column = 0)

# ---------------------------------------------------------
root.mainloop()