import random

single_or_two_player = input("Would you like to play single player or two player(just say one or two):")
what_beats_what = {
    "paper": "rock",
    "rock": "scissors",
    "scissor": "paper"
}

computer_choices = ["paper", "rock", "scissor"]
if single_or_two_player == "one":
    computer_choice = random.choice(computer_choices)
    player_choice = input("What would you like to play:")
    player_beated = what_beats_what.get(player_choice)
    if player_beated == computer_choice:
        print("YOU WIN!!!!")
        print("The computer played: " + computer_choice + ".")
    elif player_choice == computer_choice:
        print("Tie.")
        print("The computer played: " + computer_choice + ".")
    else:
        print("you lose....")
        print("The computer played: " + computer_choice + ".")
elif single_or_two_player == "two":
    player_one_choice = input("Player 1 choice:")
    player_two_choice = input("Player 2 choice:")
    player_beated = what_beats_what.get(player_two_choice)
    if player_beated == player_one_choice:
        print("Player 2  WINS!!!!")
    elif player_two_choice == player_one_choice:
        print("Tie.")
    else:
        print("Player 1 WINS!!!!")