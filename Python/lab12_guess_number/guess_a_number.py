'''
Lab 12: Guess the Number
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
'''
#version 4 - tell user wheter the current guess is closer to the previous guess
import random

#this will evaluate high and low
def evaluate_high_low(current_guess, last_guess, pc_number):
    if abs(current_guess-pc_number) < abs(last_guess-pc_number):
        print("Your current guess is closer to the target compared to the previous guess!")
    else:
        print("Your current guess is farther to the target compared to the previous guess!")

def guess(pc_number):
    current_guess = 0
    last_guess = 0
    guess_wrong = True
    while guess_wrong:
        current_guess = int(input("Enter a number to guess: "))
        if current_guess == pc_number:
            print(f"Your guess is {current_guess} and computer's number is {pc_number}. You are correct!!!")
            break
        print("Try again!")
        evaluate_high_low(current_guess, last_guess, pc_number)
        last_guess = current_guess
def main():
    print("Wecome to Guess-A-Number!!!\n")
    pc_number = random.randint(1,10)
    print("Computer has randomly selected a number from 1 to 10.")
    guess(pc_number)

main()
