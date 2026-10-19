from functions import *

while True:
    print("What do u want to do?")
    print ("------------------------")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter 0 to Exit")

    choice = input("Enter Your Choice : ") #The program will ask the user to enter his/her choice.

    if choice == 'Q' or choice == 'q': #If the user enters Q or q, the program will exit.
        break #if not, the program will ask the user to enter two numbers
    
    num1 = float(input("Enter Number 1 : ")) #The program will ask the user to enter two numbers.
    num2 = float(input("Enter Number 2 : "))
    

    if choice == '1': #The program will then call the appropriate function based on the user’s choice.
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        division(num1,num2)
    else: #If the user enters a non-numeric value, the program will ask the user to enter a number again.
        print("Invalid Choice") 

    print("\n") #After the function is executed, the program will ask the user to enter his/her choice again.