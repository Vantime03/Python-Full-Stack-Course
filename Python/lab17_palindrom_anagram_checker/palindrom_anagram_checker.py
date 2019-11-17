'''
lab 17: Palindrom and Anagram checker
Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

'''

def check_palindrome(input_string):
    reverse_input_string = ""
    for n in range (1, len(input_string)+1):
        reverse_input_string += input_string[-n]
    if input_string == reverse_input_string:
        return True
    else: 
        return False

def main():
    print("Welcome to Palindrome checker!")
    input_string = (input("Enter a string to check for palindrome: ")).lower()
    if check_palindrome(input_string) is True:
        print(f"\"{input_string}\" is a palindrome")
    else:
        print(f"\"{input_string}\" is not a palindrome")

main()

