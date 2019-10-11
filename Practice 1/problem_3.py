'''
problem 3:

Write a function that returns True if a number within 10 of 100.

def near_100(num):
    ...
near_100(50) → False
near_100(99) → True
near_100(105) → True
'''
def between_10_to_100 (numb):
    if  10 <= numb <= 100:
        return True
    else:
        return False

def main():
    numb = int(input("Enter an integer: "))
    is_10_100 = between_10_to_100(numb)
    print(f"The number between 10 to 100 is {is_10_100}")

main()