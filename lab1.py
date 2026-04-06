# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME: Sergio Alcazar
# EMAIL: smalcaza@uci.edu
# STUDENT ID: smalcaza 73371481

def operationSolver(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"


def main():
    while True:
        num1 = int(input("Enter num1(integer):"))
        num2 = int(input("Enter num2(integer):"))
        operator = input("Enter operator(+, -, *, /):")

        result = operationSolver(num1, num2, operator)
        print(result)

        again = input("Do another calculation? (y/n): ")
        if again.lower() != 'y':
            break


if __name__ == "__main__":
    main()
