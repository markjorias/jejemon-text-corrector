from functions import *

while True:
    print("What do you want to do?")
    print ("------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print ("------------------------")
    print("Enter 0 to Exit")
#The program will ask the user to enter his/her choice.
    choice = input("Enter Your Choice : ")
#If the user enters Q or q, the program will exit.
    if choice == '0':
        break
#if not, the program will ask the user to enter two numbers.
    while True:
        while True:
            num1 = input("Enter Number 1 : ")
            num2 = input("Enter Number 2 : ")
            #If the user enters a non-numeric value, the program will ask the user to enter a number again.
            if num1.isdigit():
                num1 = float(num1)
            elif num2.isdigit():
                num2 = float(num2)
            else:
                print("Invalid input. Please enter a number.")
#The program will then call the appropriate function based on the user’s choice.
        if choice == '1':
            addition(num1,num2)
        elif choice == '2':
            subtraction(num1,num2)
        elif choice == '3':
            multiplication(num1,num2) 
        elif choice == '4':
            division(num1,num2)
        else:
            print("Invalid Choice")
#After the function is executed, the program will ask the user to enter his/her choice again.            
        print("\n")
        
#Faced Challenges:
#- non pro efficient in python programming resulting in a lot of syntax errors until i got the hang of it1