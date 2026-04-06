# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME: Sergio Alcazar
# EMAIL: smalcaza@uci.edu
# STUDENT ID: smalcaza 73371481

num1 = int(input("Enter num1(integer):"))
num2 = int(input("Enter num2(integer):"))
operator = str(input("Enter operator(+, -, *, /):"))

def operationSolver(num1, num2, operator):
    if operator == "+":
        print("num1 + num2 =", num1 + num2)
        return num1 + num2
    elif operator == "-":
        print("num1 - num2 =", num1 - num2)
        return num1 - num2
    elif operator == "*":
        print("num1 * num2 =", num1 * num2)
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            print("num1 / num2 =", num1 / num2)
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"
operationSolver(num1, num2, operator)
