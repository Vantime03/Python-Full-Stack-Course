'''
Lab 14: Pick6
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

'''
#import module
import random

def num_matches(winning_numb, user_random_numb):
    match = 0
    winning_cash = 0
    x = 0

    while x < 6:
        if winning_numb[x] == user_random_numb[x]:
            match +=1
        x+=1
    if match == 1:
        winning_cash = 4
    elif match == 2:
        winning_cash = 7
    elif match == 3:
        winning_cash = 100
    elif match == 4:
        winning_cash = 50000
    elif match == 5:
        winning_cash = 1000000
    elif match == 6:
        winning_cash = 25000000
    return winning_cash


# winning_numb = [1, 2, 3, 4, 5, 6]
# user_random_numb = [1, 2, 3, 4, 6, 8]
# result = num_matches(winning_numb, user_random_numb)
# print(result)


#variables
winning_numb = []
user_random_numb = []
total_winning = 0
total_times = 0
play_count = 0
win_count = 0

#greeting
print("Welcome to Pick6!\n\nPick6 provide a simulation of lotter winning chances by random lottery pick (your number) and random winning number. You will enter the total amount of time that you want to play. Pick6 simulate the random number picks for your number and winning number. It will provide your winning ratio, the total amount win based on the following rules:\n\nA ticket costs is $2\nif 1 number matches, you win $4\nif 2 numbers match, you win $7\nif 3 numbers match, you win $100\nif 4 numbers match, you win $50,000\nif 5 numbers match, you win $1,000,000\nif 6 numbers match, you win $25,000,000\n\n")

play_count = int(input("Enter the number of plays (e.g. 1000): "))
print("Please wait...\n\n")

while total_times < play_count:
    #random pick 6 number from 1 to 99 for winning number
    x=0
    while x < 6:
        rand = random.randint(1, 99)
        winning_numb.append(rand)
        # print(winning_numb)
        x +=1
    # test print(winning_numb)

    #random pick 6 number from 1 to 99 for user number
    x = 0
    while x < 6:
        rand = random.randint(1, 99)
        user_random_numb.append(rand)
        # test print(user_random_numb)
        x +=1
    # test print(user_random_numb)
    winning_current = num_matches(winning_numb, user_random_numb)
    if winning_current != 0:
        win_count +=1
    total_winning +=winning_current
    total_times +=1

    #reset the value for the next play
    winning_numb = []
    user_random_numb = []
    # print(total_times)
print(f"***Result***\nWin ratio: {round(((win_count/total_times)*100), 2)}%")
print(f"Total winning: ${total_winning}")
print(f"Total cost for buying {total_times} tickets: ${total_times*2}")
print(f"Profit margin (positive = gain, negative = loss): {((total_winning - (total_times*2))/(total_times*2))*100}% ")
