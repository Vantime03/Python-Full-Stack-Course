#simple calculator app

import operator

dic_operator = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
} #https://docs.python.org/3/library/operator.html

def calculate(first_numb, operation_input, second_numb):
    print(f"{first_numb} {operation_input} {second_numb} = {dic_operator[operation_input](first_numb, second_numb)}")

def main():
    print("Welcome to Simple calculator!\n")
    operation_input = input("Enter an operation you wish to perform (+, -, *, /): ")
    first_numb = float(input("Enter the first number: "))
    second_numb = float(input("Enter the second number: "))
    calculate(first_numb, operation_input, second_numb)

main()
