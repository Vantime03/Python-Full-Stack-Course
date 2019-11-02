#simple calculator app
import string

def verify_injection(user_input):
    for n in user_input:
        if n in string.ascii_lowercase or n in string.ascii_uppercase:
            return True
        else:
            return False
def main():
    print("Welcome to Simple calculator!\n")
    expression = input("Enter an arithmetic expression (e.g. '2 + 3 + 5'): ")
    injection_boolean = verify_injection(expression)
    if injection_boolean is False:
        print(eval(expression))
    else:
        print("THAT IS AN INVALID expression!!!! NO INJECTION ALLOW!")

main()
