import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emoji_map = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}
choices = tuple(emoji_map.keys())


def selection():
    while True:
        user_choice = input("Rock, paper or scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice")


def display_choice(user_choice, computer_choice):
    print(f"You choose {emoji_map[user_choice]}")
    print(f"Computer choose {emoji_map.get(computer_choice)}")


def determine_winner(user_choice, computer_choice):
    if (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win..!!")
        return "user"

    elif user_choice == computer_choice:
        print("Its draw..!!")
        return "draw"
    else:
        print("You loose..!!")
        return "computer"


def play_rock_paper_scissor():

    count = 0
    user_wins = 0
    computer_wins = 0
    draws = 0
 
    while True:
        user_choice = selection()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        else:
            draws += 1
        # user_wants_to_continue = input(
        #     "Do you want to continue? (y/n)").lower()
        # # if user_wants_to_continue == 'n':
        #     break
        count += 1
        if count == 3:
            break
    if user_wins > computer_wins:
        print(f"Overall Winner is USER..!!")
    elif user_wins == computer_wins:
        print()
        print(f"Overall its draw")
    else:
        print("Overall the COMPUTER WON..!!")
    
    print(f"Summary: You win {user_wins} times, Computer win {
          computer_wins} times and draws is {draws}")


play_rock_paper_scissor()
