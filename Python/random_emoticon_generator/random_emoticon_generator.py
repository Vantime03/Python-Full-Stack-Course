'''

Lab 5: Random Emoticon Generator
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

Example output:

:-P

'''
#import module
import random

#list of variables
eyes = [":", ";", "8", "X"]
noses = ["-", "^"]
mouths = [")", "(", "O", "||", "D", "]"]
emoticon_list = []

#functions

def emoticon_gen():
    emoticon_list = []
    for x in range (1, 6):
        mouth = random.choice(mouths)
        eye = random.choice(eyes)
        nose = random.choice(noses)
        emoticon_list.append(eye+nose+mouth)
    display_result(emoticon_list)

def display_result(a_list):
    print(f"\nHere is the random generated emoticon for today:\n")
    for emoticon in a_list:
        print(emoticon)

def play_again():
    generate_more = input("\nWould you like to randomly generate more emoticons (yes/no)? ")
    if generate_more in ["yes", "y"]:
        main()
    else:
        print("Thank you for playing!!!")
        exit()

def main():
    emoticon_gen()
    play_again()


print("Welcome to Emoticon Generator!")
main()
