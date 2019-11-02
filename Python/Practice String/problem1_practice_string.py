'''
Problem 1
Get a string from the user, print out another string, doubling every letter.

>>> Enter some text: hello
hheelloo
'''
def double_string(user_input):
    new_string = ""
    for char in user_input:
        new_string += char*2
    return new_string

def main():
    user_input = input("Type a phrase or word: ")
    print(f"Result: {double_string(user_input)}")

main()