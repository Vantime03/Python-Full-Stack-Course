'''
Problem 2
Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

Enter a number (or 'done'): 5
Enter a number (or 'done'): 34
Enter a number (or 'done'): 515
Enter a number (or 'done'): done
[5, 34, 515]
'''
import string

def take_input():
    user_input = ""
    ls = []

    while user_input != "done":
        user_input = input("Enter a number (or \'done\'): ")
        if user_input == "done":
            return ls
        ls.append(user_input)

def main():
    print(f"list of numbers: {take_input()}")

main()