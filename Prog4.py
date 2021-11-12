# Areas and Perimeters project
# 11 November 2021
# Version 1.0
# Wayne Caissie

border_amount = 30
program_title = "Areas and perimeters project"

def main():
    """ The purpose of this program is to use functions in a user friendly way
        to create a text based interface solving whole number area and perimeter problems."""

    student_info()
    
    print("""Welcome, this program will enable the user to select different
calculators from a menu of 6 options with a prompt to quit before and after.""")

    choice()                                                                                    #Start the flow of control

def calculate_rectangles(side_a, side_b, menu_choice):                                          #Calculate via formulas
    if menu_choice == '1' or menu_choice == '2':
        return print("The area of this polygon is", side_a * side_b, "square units.")
    else:
        return print("The perimeter of this polygon is", 2 * side_a + 2 * side_b, "units.")


def calculate_circles(radius, menu_choice):
    pi = 3.14159
    if menu_choice == '3':
        return print("The area of this circle is", pi * radius ** 2, "square units.")
    else:
        return print("The perimeter of the circle is", 2 * pi * radius, "units.")


def warning():                                                                                  #Program examples only allowed integers
    print("You must select integers only!")


def check_for_negative(n):                                                                      #Determine if n is negative or not
    if n < 0:
        return True
    else:
        return False


def reset_letter(a):
    a = ""
    return a

    
def begin():                                                                                    #Inits some variables for choosing and lengths
    a = ""
    b = ""
    decision = ""
    
    while decision == "":
        print("""\nWhat would you like to do:\n
1) AREA (SQUARE)

2) AREA (RECTANGLE)

3) AREA (CIRCLE)

4) PERIMETER (SQUARE)

5) PERIMETER (RECTANGLE)

6) PERIMETER (CIRCLE)

7) EXIT\n""")

        decision = input("Select a number from the list above >>> ")
        
        if decision not in "1 2 3 4 5 6 7".split():
            print("You must select a menu item by number without the bracket.\n")
            decision = ""

    if decision == '1' or decision == '2' or decision == '4' or decision == '5':
        while type(a) != int:                                                                   #Checks type(a) only instead of both for brevity
            a = input("\nIn a whole number, how long is the first side? >>>  ")                 #Collects first and second numbers for the math
            b = input("In a whole number, how long is the second side? >>>  ")
                 
            try:
                int(a)                                                                          #Checks to see if the user keyed legal side lengths
                int(b)
                a, b = int(a), int(b)                                                           #If so, change the variables into integers from string
                
            except:
                a, b = reset_letter(a), reset_letter(b)                                         #If not, reset both a and b to the placeholder string
                warning()                                                                       #And print out a warning

            if check_for_negative(a) or check_for_negative(b):
                print("Cannot use negatives!")
                a, b = reset_letter(a), reset_letter(b)
                
            elif a == 0 or b == 0:
                print("Cannot have 0 for a side length!")
                a, b = reset_letter(a), reset_letter(b)
                
        calculate_rectangles(a, b, decision)

    elif decision == '3' or decision == '6':                                                    #Checks for legal radius inputs for circle calcs
        while type(a) != int:
            a = input("\nIn a whole number, how long is the radius? >>>  ")

            try:
                int(a)
                a = int(a)

            except:
                a = ""
                warning()

            if check_for_negative(a):
                print("Cannot use negatives!")
                a = reset_letter(a)

            elif a == 0:
                print("Cannot have a size 0 radius!")
                a = reset_letter(a)

        calculate_circles(a, decision)                                                          #Calculates if inputs are legal

    elif decision == '7':
        return print("Have a great day!")
    
    choice()
    

def goodbye():
    print("Goodbye! See you next time.")
    

def choice():
    user_choice = "unknown"                                                                     #Checks for willingness to participate
    while user_choice == "unknown":
        user_choice = input("\nDo you wish to continue? (y/n) >>> ").lower()
        if user_choice == "y" or user_choice == "yes":
            begin()
        elif user_choice == "n" or user_choice == "no":
            goodbye()
        else:
            user_choice = "unknown"
            print("You must select y for yes or n for no.")
    

def student_info():                                                                             #Project information for professor
    """This function will print out the particulars for the project start."""
    print("\n")
    print("#" * border_amount)
    print("\nProgram_Author: Wayne Caissie")
    print("Student ID number : 3558688")
    print("Program title:", program_title, "\n")
    print("#" * border_amount)
    print("\n")

    
    
if __name__ == "__main__":                                                                      #Checks if file was imported or is main
    main()
