# Program that performs operations on an integer (initial value 0). The program displays the value of the integer
# and then displays the following menu:
# 1. Add
# 2. Multiply
# 3. Subtraction
# 4. Exit
# The program then asks the user to type an integer between 1 and 4. If the user types a value between 1 and 4, the operation
# is performed, the new value of the integer is displayed and then the menu is displayed again and so on until you type 4.
# When you type 5, the program ends.
# Caution: You must use a function to define each operation. You must use a switch box. You must validate the user input,
# in the event of an erroneous input, the application displays: enter an integer. And repeats the operation.
#########################################Answer################################################
def add():
    try:
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        result = num1 + num2
    except ValueError:
        print("enter an integer.")
    else:
        print(f'Result is: {result}')
def Division():
    try:
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        if num2 == 0:
            print("Cannot divide by 0")
    except ValueError:
        print("enter an integer.")
    else:
        print(f'Result is: {result}')
def Subtraction():
    try:
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        result = num1 - num2
    except ValueError:
        print("enter an integer.")
    else:
        print(f'Result is: {result}')
def Multiply():
    try:
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        result = num1 * num2
    except ValueError:
        print("enter an integer.")
    else:
        print(f'Result is: {result}')
def Menu():
    ans = True
    while ans:
        print("""
        1 - add.
        2 - Division.
        3 - Subtraction.
        4 - Multiply.
        5 - Exit.
        """)
        choice = input("Enter your option:")
        match choice:
            case '1':
                add()
            case '2':
                Division()
            case '3':
                Subtraction()
            case '4':
                Multiply()
            case '5':
                exit()
Menu()