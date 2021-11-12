# Math Functions project
# 11 November 2021
# Version 1.1
# Wayne Caissie

border_amount = 30
program_title = "Math Functions"

def main():
    """ The purpose of this program is to demonstrate how to perform calculations
        with Python's inbuilt mathematical tools.  A user inputs their favourite 2
        numbers and the program outputs the operation being done as well as the output
        for that operation.  If they wish to conduct another round, they may do so by
        indicating that at the prompt asking them at the end of the program."""

    student_info()
    
    print("""Welcome, this program will take two integers of your choosing and
will conduct a series of mathematical operations on them.\n""")

    choice()                                                                            #Start the flow of control
        
        
def begin():
    a, b = "", ""                                                                       #Placeholders only until user inputs something for them
    print("\n")
    
    while type(a) != int:
            a = input("What is your first number? >>>  ")                               #Collects first and second numbers for the math
            b = input("What is your second number? >>>  ")
                 
            try:
                int(a)                                                                  #Checks to see if the user keyed legal characters
                int(b)
                a, b = int(a), int(b)                                                   #If so, change the variables into integers from string
                
            except:
                a = ""                                                                  #If not, reset both a and b to the placeholder string
                b = ""
                print("You must select an integer for both!")                           #And print out a warning

    print("\nAddition: {} + {} =".format(a, b), str(a + b))                             #Conduct the math
    print("Subtraction: {} - {} =".format(a, b), str(a - b))
    print("Multiplication: {} * {} =".format(a, b), str(a * b))
    
    try:
        print("Division: {} / {} =".format(a, b), str(a / b))                           #Check for division by 0 and allow it to happen if not
    except:
        print("You cannot divide by zero!")                                             #Prints the division by zero warning
        
    print("Exponentiation: {} ** {} =".format(a, b), str(a ** b))
    
    try:
        print("Modulo: {} % {} =".format(a, b), str(a % b))                             #Checks for modulo by 0 and allow it to happen if not
    except:
        print("You cannot modulo by zero either!!!")                                    #Prints another warning if it is by 0
        
    print("\n")

    choice()

def goodbye():
    print("Goodbye! See you next time.")

    
def choice():
    user_choice = "unknown"                                                             #Checks for willingness to participate
    while user_choice == "unknown":
        user_choice = input("Do you wish to continue? (y/n) >>> ").lower()
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

    
    
if __name__ == "__main__":                                              #Checks if file was imported or is main
    main()
