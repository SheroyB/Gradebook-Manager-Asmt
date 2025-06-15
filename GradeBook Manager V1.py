#This program is the first version of a student gradebook manager, it is very basic but completes it's purpose

code = input("Please enter your teacher code: ") #Asks user for their teacher code
print() #Empty print statements to create space and make the program less congested
subject = input("Please enter the subject that the grade is for: ") #Asks user for Subject code
print()
name = input("Please enter the student's fullname: ") #Asks user for student's name
print()
grade = input("Please enter the student's grade (NA, A, M, E): ") #Asks user to enter the grade for the student
print()

while True: #While loop asks the user if they want to enter more grades
    more = input("Would you like to enter more students? (yes/no): ")
    print()
    if more == 'yes':
        name = input("Please enter the student's fullname: ")
        print()
        grade = input("Please enter the student's grade (NA, A, M, E): ")
        print()
    else: #If user wishes not to enter more students
        break
print("Thank you, the grades have been entered.")
