import random


def play_turn(player_name):
    turn_score = 0
    print(f"{player_name}'s turn")

    while True:
        number = roll_a_die()
        print(f"You rolled {number}")
        if number == 1:
            return 0
        else:
            turn_score += number
            choice = input("Do you want to roll again: y or n: ").lower()
        if choice == "n":
           return turn_score

def roll_a_die():
    return random.randint(1,6)

def set_target(current_player):
    target = int(input(f"PLAYER-{current_player + 1} Set your target score: "))
    return target

def swtich_player(current_player, total):
    # print(f"CP: {current_player}, total: {total}")
    if current_player < total - 1:
         return current_player + 1
    else:
        return 0

        
        

if __name__ == '__main__':
    print("""This is game where the person who reaches 100 points first wins when throwing a die.
    The person can give the turn to the other person whenever he wishes. If throws a one he looses all his points""")
    number_of_players = int(input("How many players are going to play the game: "))
    scores = [0] * number_of_players
    target = [0] * number_of_players

    for current_player in range(number_of_players):
        target[current_player] = set_target(current_player)
        print(f"Player-{current_player + 1}Points to score to win: {target[current_player]}")
    
    print(f"scrores: {scores}")
    print(f"target: {target}")
    
    current_player = 0

    while True:

        player_name = f"Player {current_player + 1}'s"
        turn_score = play_turn(player_name)
        scores[current_player] += turn_score
        print(f"\nIn this TURN you scored {turn_score} points this turn")
        print("Current Scores: ")

        for p in range(number_of_players):
            print(f"Player-{p + 1}: {scores[p]} ", end=" ", sep=" ")
        print()
        
        if scores[current_player] >= target[current_player]:
            print(f'Player {current_player + 1} WINS ...!!!')
            break

        current_player = swtich_player(current_player, number_of_players)
        

