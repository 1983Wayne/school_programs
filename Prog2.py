# Using Input project
# 11 November 2021
# Version 1.0
# Wayne Caissie

border_amount = 30
program_title = "Using Input project"

def main():
    """ The purpose of this program is to demonstrate Python's ability to handle user input
        in the form of strings and produce output based on the input."""

    student_info()
    
    print("""Welcome, this program will take two strings of your choosing, two
integers, and then output the concatenation of the strings and multiplication
of the two integers on successive lines.""")

    choice()                                                                            #Start the flow of control

        
def begin():
    string_one = input("\nWhat is your first string? >>> ")                             #Gets first and second strings
    string_two = input("What is your second string? >>> ")
    
    a, b = "", ""                                                                       #Placeholders only until user inputs something for them
    
    while type(a) != int:                                                               #Checks type(a) instead of both for brevity
            a = input("\nWhat is your first integer? >>>  ")                            #Collects first and second numbers for the math
            b = input("What is your second integer? >>>  ")
                 
            try:
                int(a)                                                                  #Checks to see if the user keyed legal characters
                int(b)
                a, b = int(a), int(b)                                                   #If so, change the variables into integers from string
                
            except:
                a = ""                                                                  #If not, reset both a and b to the placeholder string
                b = ""
                print("You must select an integer for both!")                           #And print out a warning

    print("\nFirst and second strings concatenated:", string_one + string_two)
    print("Both integers multiplied together: {} * {} =".format(a, b), (a * b))
    
    choice()
    

def goodbye():
    print("Goodbye! See you next time.")
    

def choice():
    user_choice = "unknown"                                                             #Checks for willingness to participate
    while user_choice == "unknown":
        user_choice = input("\nDo you wish to continue? (y/n) >>> ").lower()
        if user_choice == "y" or user_choice == "yes":
            return begin()
        elif user_choice == "n" or user_choice == "no":
            return goodbye()
        else:
            user_choice = "unknown"
            print("You must select y for yes or n for no.")
    

def student_info():                                                                     #Project information for professor
    """This function will print out the particulars for the project start."""
    print("\n")
    print("#" * border_amount)
    print("\nProgram_Author: Wayne Caissie")
    print("Student ID number : 3558688")
    print("Program title:", program_title, "\n")
    print("#" * border_amount)
    print("\n")

    
    
if __name__ == "__main__":                                                              #Checks if file was imported or is main
    main()
