'''
Practice Problem 1
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even(a):
    ...
is_even(5) → False
is_even(6) → True
'''

def is_even(user_input):
    remainder = user_input % 2
    if remainder == 0:
        return True
    else:
        return False


def main():
    print("Note: this problem will determine whether if you number is odd or even.\n")
    user_input = int(input("Enter an integer number (e.g. 4): "))
    result = is_even(user_input)
    if result is True:
        print("This is even number!")
    else: 
        print("this is odd number!")

main()




