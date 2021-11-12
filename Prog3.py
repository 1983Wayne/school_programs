# Loops and If conditions project
# 11 November 2021
# Version 1.0
# Wayne Caissie


border_amount = 30
famous_ladies = "madonna cher kerrigan".split()
name_first = "Wayne"
name_last = "Caissie"
password = "hello"
program_title = "Loops and if conditions project"

def main():
    """ The purpose of this program is to demonstrate Python's looping and
        conditionals for branching inside a program."""

    student_info()
    
    print("""Welcome, this program will only allow program access to users who
can demonstrate that they know the super duper secret password.""")

    choice()                                                                            #Start the flow of control

def second_half():
    user_name = input("What is your first name? >>> ")                                  #Ask for the user's name
    if user_name.lower() in famous_ladies:                                              #Check if an esteemed lady, if so ask
        print("CAN I GET YOUR AUTOGRAPH MA'AM!?")                                       #For their autograph                                            
    elif user_name.lower() == name_first.lower():                                       #If user's first name is same as project                                   
        print("What a great name!")                                                     #maker, compliment them
    else:
        print("{}, that's a nice name.".format(user_name.capitalize()))                 #Otherwise give a generic response
        
def begin():
    password_attempt = input("What is the password? >>> ")                              #Check if user knows the password
    if password_attempt == password:
        print("\nWelcome to the second part of the program, human!")                    #If possible to pass the check, send
        second_half()                                                                   #the user to the next half of the program
    else:
        print("That is not a correct password!")
    choice()
    

def goodbye():
    print("Goodbye! See you next time.")
    

def choice():
    user_choice = "unknown"                                                             #Checks for willingness to participate
    while user_choice == "unknown":
        user_choice = input("\nDo you wish to continue? (y/n) >>> ").lower()
        if user_choice == "y" or user_choice == "yes":
            begin()
        elif user_choice == "n" or user_choice == "no":
            goodbye()
        else:
            user_choice = "unknown"
            print("You must select y for yes or n for no.")
    

def student_info():                                                                     #Project information for professor
    """This function will print out the particulars for the project start."""
    print("\n")
    print("#" * border_amount)
    print("\nProgram_Author:", name_first, name_last)
    print("Student ID number : 3558688")
    print("Program title:", program_title, "\n")
    print("#" * border_amount)
    print("\n")

    
    
if __name__ == "__main__":                                                              #Checks if file was imported or is main
    main()
