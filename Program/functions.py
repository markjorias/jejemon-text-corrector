# Description: This file contains the functions for the calculator program
#This contains the operations of the basic calculator
def addition(num1,num2):
    result = num1 + num2 #result is the sum of num1 and num2
    print("{0} + {1} = {2}".format(num1,num2,result)) #format is used to print the result in the format of num1 + num2 = result

def subtraction(num1,num2):
    result = num1 - num2 #result is the difference of num1 and num2
    print("{0} - {1} = {2}".format(num1,num2,result))

def multiplication(num1,num2):
    result = num1 * num2 #result is the product of num1 and num2
    print("{0} * {1} = {2}".format(num1,num2,result))

def division(num1,num2):
    if num2 == 0.0: #if num2 is 0, the program will print "Cant Do Divide by Zero"
        print("Cant Do Divide by Zero")
    else: #if not, the program will print the quotient of num1 and num2
        result =  num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,result))

def correct_jejemon(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Correct the numbers
    content = content.replace("0", "o")
    content = content.replace("1", "i")
    content = content.replace("3", "e")
    content = content.replace("4", "a")
    content = content.replace("5", "s")
    content = content.replace("7", "t")

    # Create a new file path for the corrected file
    new_file_path = file_path.replace(".txt", "_corrected.txt")

    # Write the corrected content to the new file
    with open(new_file_path, 'w') as file:
        file.write(content)

    return new_file_path