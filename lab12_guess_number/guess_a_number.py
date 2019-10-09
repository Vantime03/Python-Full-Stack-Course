'''
Lab 12: Guess the Number
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
'''
#version 2
import random

def guess(pc_number):
    guess_wrong = True
    while guess_wrong:
        guess_number = int(input("Enter a number to guess: "))
        if guess_number == pc_number:
            print(f"Your guess is {guess_number} and computer's number is {pc_number}. You are correct!!!")
            guess_wrong = False
        print("Try again!")

def main():
    print("Wecome to Guess-A-Number!!!\n")
    pc_number = random.randint(1,10)
    print("Computer has randomly selected a number from 1 to 10.")
    guess(pc_number)

main()
