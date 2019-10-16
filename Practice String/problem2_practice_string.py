'''
Problem 2
Write a function that takes a string, and returns a list of strings, each missing a different character.

missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

test case: ittenkttenkitenkitenkittnkitte
test case: itten ktten kiten kiten kittn kitte
'''

def kitten_spellcheck(kitten_string):
    possible_missing_char = ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
    current_list_missing_char = []

    for n in possible_missing_char:
        count = kitten_string.count(n)
        if count >= 1:
            current_list_missing_char.append(n)
    return current_list_missing_char

def main():
    kitten_string = (input("Enter a kitten string as fast as you can: ")).lower()
    print(f"Here is the list of miss-spelled string: {kitten_spellcheck(kitten_string)}")

main()