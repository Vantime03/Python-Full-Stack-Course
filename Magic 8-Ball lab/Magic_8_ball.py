'''
Lab 4: Magic 8-Ball
Let's write a program to simulate the classic "Magic Eight Ball"

Concepts Covered
input, print
import
random.choice
Instructions
Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.

'''
#import module
import random

#list variables
responses_list = ["It is certain",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"]

print("Welcome to Magic 8-Ball!\n")

user_question = input("Ask the Magic 8-Ball a question: ")

print(f"\nThe prediction is: {random.choice(responses_list)}")
