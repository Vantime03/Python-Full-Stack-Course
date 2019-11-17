'''
Problem 6
Return the number of letter occurances in a string.

def count_letter(letter, word):
    ...
count_letter('i', 'antidisestablishmentterianism') → 5
count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2

'''
def get_string():
    input_str = (input("Enter a string: ")).lower()
    input_str = input_str.replace(" ", "")
    return input_str

def get_char():
    char = (input("Enter a char for count: ")).lower()
    char = char.replace(" ", "")
    if len(char) > 1:
        print("Only enter one character!!!")
        get_char()
    return char

def count_letter(input_str, char):
    return input_str.count(char)        

def main():
    input_str = get_string()
    char = get_char()
    print(f"the number of \"{char}\" in \"{input_str}\" is {count_letter(input_str, char)}")

main()


    
