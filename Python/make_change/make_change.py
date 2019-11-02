'''
Lab 8: Make Change
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered
conditionals, comparisons
arithmetic
Version 1
Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2
Have the user enter a dollar amount (1.36), convert this to the total in pennies.
'''

def conversion(dollars):
    pennies = dollars*100
    remainder = 0
    print(f"\nHere is your change:")
    if pennies >= 25:
        quarters = pennies // 25
        pennies = pennies % 25
        print(f"Quarter(s): {quarters}")
    if pennies >= 10:
        dimes = pennies // 10
        pennies = pennies % 10
        print(f"dime(s): {dimes}")
    if pennies >= 5:
        nickes = pennies // 5
        pennies = pennies % 5
        print(f"nickle(s): {nickes}")
    if pennies >= 1:
        print(f"Penny(ies): {pennies}")

def main():
    print("Welcome to Make Change!\n    ")
    user_input_dollar = float(input("Enter a dollar amount (e.g. 1.36): "))
    conversion(user_input_dollar)

main()
