'''
### rock paper scissor game ####
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper (you lose!)
rock vs scissors (you win!)
paper vs rock  (you win!)
paper vs paper (tie)
paper vs scissors (you lose!)
scissors vs rock (you lose!)
scissors vs paper (you win!)
scissors vs scissors (tie)

'''

#import module
import random

# list of vairables
choice = ["paper", "rock", "scissor"] # this is computer choice for random
total_games = 0
games_won = 0
games_lose = 0
games_tie = 0


game_result = {
"rockscissor": "You chose rock. Computer chose scissor. You win!",
"paperrock": "You chose paper. Computer chose rock. You win!",
"scissorpaper": "You chose scissor. Computer chose paper. You win!",
} #this is the dictionary list for game result

def main():
    choice = ['rock', 'paper', 'scissor']
    user_input = input("\nPlease enter your choice (rock, paper, scissor):  ").lower()
    computer_choice = random.choice(choice)

    if user_input == computer_choice:
        print(f"You chose {user_input} and computer chose {computer_choice}. It's a tie!")
    elif (user_input+computer_choice) == "rockscissor" or (user_input+computer_choice) == "paperrock" or (user_input+computer_choice) == "scissorpaper":
        print(f"{game_result[user_input+computer_choice]}")
    else:
        print(f"You chose {user_input} and computer chose {computer_choice}. You lost!")
main()

'''
def game_begin():

    global total_games
    global games_won
    global games_lose
    global games_tie

    user_input = input("\nPlease enter your choice (rock, paper, scissor):  ").lower()
    if user_input in choice:
        computer_input = random.choice(choice)

        # this is a test print: print(user_input+computer_input)
        print(game_result.get(user_input + computer_input))
        str_rec = statistic(user_input, computer_input, total_games, games_won, games_lose, games_tie)

        # reassign the updated valuse from statistic
        total_games = str_rec[0]
        games_won = str_rec[1]
        games_lose = str_rec[2]
        games_tie = str_rec[3]

        #ask user if they want to play again, if they do, the code will go back to the beginning
        play_again = input("\nDo you want to play again? (yes/no) ")
        if play_again in ("yes", "y"):
            game_begin()
    else:
        print("Invalid input! Please enter rock, paper, scissor.")
        game_begin()

#Game greeting
print("Hello! Welcome to Rock-Paper-Scissor with Statistic")
game_begin()
'''