from termcolor import colored
import copy
import random

CURRENT_PLAYER = colored('X', 'green')
x_wins = 0
o_wins = 0
ROWS = 3
COLUMNS = 3

new_board = [
    [' ' for _ in range(COLUMNS)]
    for _ in range(ROWS)
]


def print_board(board):
    line = '+---+---+---+'
    print(line)
    for row in board:
        print(f'| {row[0]} | {row[1]} | {row[2]} |')
        print(line)


def is_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_full(board):
    for row in board:
        if ' ' in row:
            return False

    return True


def get_position(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value == 9:
                return value
            if value < 0 or value > 3:
                raise ValueError
            return value

        except ValueError:
            print("Invalid Input. Please enter a between 0-2")


def player_move(current_player, board):

    while True:
        if (current_player == CURRENT_PLAYER):
            s = colored("Your turn", "green")
            print(f"{s}: ")
            row = get_position('Enter row (0-2): ')
            if row == 9:
                return None, None
            col = get_position('Enter column (0-2): ')
            if col == 9:
                return None, None

            if board[row][col] == ' ':
                board[row][col] = current_player
                print_board(board)
                break
            print("Position is already occupied. Re-enter a free position")
            continue

        else:
            while True:
                p = colored("Computer's turn", "red")
                print(f"{p}: ")
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    print_board(board)
                    break
                print("Position is already occupied. Re-enter a free position")

        return row, col


def switch_player(current_player):
    if current_player == CURRENT_PLAYER:
        current_player = colored('0', 'red')
        return current_player
    else:
        current_player = CURRENT_PLAYER
        return current_player


def main():
    board = copy.deepcopy(new_board)
    print_board(board)
    current_player = CURRENT_PLAYER
    global x_wins, o_wins

    while True:
        move = player_move(current_player, board)
        if move == (None, None):
            print("New game started...")
            board = copy.deepcopy(new_board)
            print_board(board)
            continue

        if is_winner(board):
            if current_player == CURRENT_PLAYER:
                print(f"You're the WINNER..!!!")
                x_wins = x_wins + 1
            else:
                print(f"Computer is the WINNER..!!!")
                o_wins += 1

            break

        if is_full(board):
            print("The board is full and the game is a draw...")
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    print("tic-tac-toe game begins")
    print("press 9 at any point of time to restart the game")
    while True:
        main()
        user_choice = input(
            "Do you want to continue or start a new game (y/n): ").lower()
        if user_choice == 'n':
            break

    print(f"You have won {x_wins} times")
    print(f"Computer has won {o_wins} times")
