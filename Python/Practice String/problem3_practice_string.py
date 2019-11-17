'''
Return the letter that appears the latest in the english alphabet.

>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
the latest letter is v.

'''
import string

def latest_letter(user_string):
    char_ind = 0
    for c in user_string:
        if string.ascii_lowercase.index(c) > char_ind:
            char_ind = string.ascii_lowercase.index(c)
    return string.ascii_lowercase[char_ind]

def main():
    user_string = (input("Type in a word or a phrase: ")).lower()
    print(f"The latest letter is {latest_letter(user_string)}.")

main()