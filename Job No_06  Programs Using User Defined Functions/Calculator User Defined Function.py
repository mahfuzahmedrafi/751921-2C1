def addition(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def division(num1, num2):
    return num1/num2


def multiplication(num1, num2):
    return num1*num2


def show(n1, n2):
    print(f'{n1}+{n2} = {addition(n1,n2)}')
    print(f'{n1}-{n2} = {subtract(n1, n2)}')
    print(f'{n1}/{n2} = {division(n1, n2)}')
    print(f'{n1}*{n2} = {multiplication(n1, n2)}')


show(int(input('A:')), int(input('B:')))
