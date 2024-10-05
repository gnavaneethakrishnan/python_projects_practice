# Select Random number between 1 to 100
# Ask the user to guess a number between 1 to 100
# Loop the below logic till the user gets the number
# if the guess < number then too low
# too high

import random


def guess_number():
    print("THIS IS A NUMBER GUESSING GAME, I HAVE NUMBER, TRY GUESSING THE NUMBER, WILL PROMPT YOU WITH HELP")
    print("To quit the game at anytime, enter 0 instead of number")
    print("You can choose the difficulty level, if difference between min and max is high, difficulty is high")

    max_count = 5
    best_score = []
    count = 0
    
    while True:

        if count == 0:
            try:
                min_number = int(input(
                    "Enter the min number above which the random number to guess will be generated: "))
                max_number = int(input(
                    "Enter the max number below which the random number to guess will be generated: "))

            except ValueError:
                print("Enter a min and max positive number other than 0")

            number = random.randint(min_number, max_number)
            print(number)

        try:
            guess = int(input(f"Guess the number between {min_number} to {max_number}: "))
            count += 1

            if count > max_count:
                print("You exceeed your attempts, better luck next time")
                break

            if guess == number:
                print(f'Congrats! you guessed the number in {count} attempts')
                best_score.append(count)
                print(f"The best score is {min(best_score)}")
                count = 0

            elif guess == 0 and count > 0:
                print("Thanks for playing the game..!!!")
                break

            elif guess == 0 and count == 0:
                print(
                    "It is unfortunate you dont want to play...!!!, its fine, come back if you change your mind")
                break

            elif guess < number:
                print("Too low! try again")

            else:
                print("Too high! try again")

        except ValueError:
            print("Enter a number between 1 to 100")


guess_number()

# 13 , 13 < 25
