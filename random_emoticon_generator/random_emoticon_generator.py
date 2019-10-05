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

print("Welcome to Emoticon Generator!")

print(f"\nHere is the random generated emoticon for today: {random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}")

#advanced version 2
while True:
    generate_more = input("\nWould you like to randomly generate more emoticons (yes/no)? ")
    if generate_more in ["yes", "y"]:
        print(f"Here is the five random emoticons:\t{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}\t{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}\t{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}\t{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}\t{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}")
    else:
        print("Thank you for playing!")
        break
