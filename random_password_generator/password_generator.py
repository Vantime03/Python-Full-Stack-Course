'''
Lab 6: Password Generator
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered
input, print
looping
random.choice
the 'sting builder pattern'
Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.

Version 3 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.
'''

#import module
import random
from string import digits
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation

# variables
password = []
print("Welcome to password generator!\n")
num_len = int(input("How many characters do you want your password to have?"))
lower_len = int(input("How many characters do you want your password to have?"))
upper_len = int(input("How many characters do you want your password to have?"))
special_len = int(input("How many characters do you want your password to have?"))

#processing Password
n=0
while n < num_len:
    password.append(random.choice(digits))
    n+=1
n=0
while n < lower_len:
    password.append(random.choice(ascii_lowercase))
    n+=1
n=0
while n < upper_len:
    password.append(random.choice(ascii_uppercase))
    n+=1
n=0
while n < special_len:
    password.append(random.choice(punctuation))
    n+=1
random.shuffle(password)
str_password = "".join(password)

print(f"\nHere is your password: {str_password}")
