#This program is the third version of a student gradebook manager, it uses buttons where needed and displays a graph at the end.

from easygui import* #Import all from Easygui
import pandas as pd #To create the graph
import matplotlib.pyplot as plt #To create the graph

while True: #While loop to gather teacher code from the user
    try:
        code = enterbox("Please enter your teacher code: ")
        if len(code) != 3: #Checks that user entered only 3 characters
            msgbox("Teacher code must be exactly 3 letters")
            continue
        if not code.isalpha(): #Checks that user entered only letters
            msgbox("Teacher code must not include numbers")
            continue
        break
    except TypeError:
        continue

while True: #While loop to get the subject code from the user
    try:
        subject = enterbox("Please enter the code for the subject you wish to enter: ")
        if len(subject) != 3: #Checks that user entered only 3 characters
            msgbox("Subject code must be exactly 3 letters")
            continue
        if not subject.isalpha(): #Checks that user entered only letters
            msgbox("Subject code must not include numbers")
            continue
        break
    except TypeError:
        continue

while True: #While loop to get students' info
    while True:
        try:
            first_name = enterbox("Please enter the student's first name: ")
            if not first_name.isalpha(): #Checks that user entered only letters
                msgbox("First name must only contain letters")
                continue
            
            last_name = enterbox("Please enter the student's last name: ")
            if not last_name.isalpha(): #Checks that user entered only letters
                msgbox("Last name must only contain letters")
                continue
            break
        except TypeError:
            continue

    name = first_name + " " + last_name #Combines student's first and last names to create their fullname

    while True: #While loop to get marks for the students
        try:
            marks = int(enterbox("Please enter the student's marks (out of 100): "))
            if marks < 0 or marks > 100: #Checks if user enters a number from 0 to 100
                msgbox("Marks must be from 0 to 100")
                continue
            break
        except (ValueError, TypeError): #Doesn't allow the user to enter strings or leave the question blank
            msgbox("Please enter a valid number")

    if marks < 40: #Categorising the grades for the amount of marks entered
        grade = 'NA'
    elif marks < 60:
        grade = 'A'
    elif marks < 80:
        grade = 'M'
    else:
        grade = 'E'

    with open("gradebook.txt", "a") as gradebook_file: #Saving the inputs into an external txt file
        gradebook_file.write(f"\n{code},{subject},{name},{marks},{grade}")

    more = buttonbox("Would you like to enter more students? : ", choices = ["Yes", "No"])
    if more != 'Yes':
        break #If the user clicks the Yes button then the loop ends and the program goes back to asking the user for the student's name
    else:
        continue
msgbox("Thank you, the grades have been entered.")

df = pd.read_csv('gradebook.txt') #Loading marks from text file
colors = ["red", "green", "yellow", "purple"] #Assigning colors to the bars
df.plot(x = 'name', y = 'marks', kind = 'bar', color = colors) #Plotting the results
plt.show() #Show the graph
