'''
Lab 19: Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

'''
playing_cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "j": 10,
    "q": 10,
    "k": 10,
}

def display_result(sum):
    if sum == 21: 
        print(f"{sum} \'Blackjack\'")
    elif sum > 21:
        print(f"{sum} \'Already Busted\'")
    elif sum < 17:
        print(f"{sum} \'Hit\'")
    elif 17 <= sum < 21:
        print(f"{sum} \'Stay\'")


    
def process_points(first, second, third):
    list_card =  [first, second, third]
    sum = 0
    first_a = False
    
    for card in list_card:
        point = 0
        if card == "a" and first_a == False:
            point = 11
            first_a = True
        elif card == "a" and first_a == True:
            point = 1
        else:
            point = playing_cards.get(card)
        sum += point
    if sum >= 22 and first_a == True: 
        sum -= 10
    display_result(sum)

def main():
    print("Welcome to Blackjack Advisor!")
    first_card = (input("What is your first card? (e.g. A=Ace, J=Jack, Q=Queen, K=King) ")).lower()
    second_card = (input("What is your second card? ")).lower()
    third_card = (input("What is your third card? " )).lower()
    process_points(first_card, second_card, third_card)

main()

