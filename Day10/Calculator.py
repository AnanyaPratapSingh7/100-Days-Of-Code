import os


def calc(number1, number2, operation):
    if operation=='+':
        return number1+number2
    elif operation=='-':
        return number1-number2
    elif operation=='*':
        return number1*number2
    elif operation=='/':
        return number1/number2
    return 0

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    answer = 0
    number1 = int(input("What's the first number?: "))
    answer = number1

    next ='y'
    while next=='y':
        operation = input("+\n-\n*\n/\nPick an operation : ")

        number2 = int(input("What's the next number?: "))

        answer = calc(number1, number2, operation)

        print(f"{number1} {operation} {number2} = {answer}")

        number1 = answer

        next = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")