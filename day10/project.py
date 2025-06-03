print("hi! its a calculator project")


def add(num1, num2):
    return float(num1) + float(num2)


def subtract(num1, num2):
    return float(num1) - float(num2)


def multiply(num1, num2):
    return float(num1) * float(num2)


def divide(num1, num2):
    return float(num1) / float(num2)


def main():
    while True:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        operator = input("Enter operator (+, -, *, /): ")
        operation = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        answer = operation[operator](num1, num2)
        print(f"the result of {num1} {operator} {num2} is {answer}")
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() == "no":
            break


main()
