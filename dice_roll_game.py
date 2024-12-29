import random


def dice_game():
   
    count = 0
    
    while True:
        user_input = input("Roll the dice? (y/n)")
        try:
            if user_input.lower() == 'y':
                user_input = input(
                    "How many dice do you want to roll? choose between 1 to 6")
                if int(user_input) <= 0 and int(user_input) > 6:
                    print("Your input is invalid, please enter between 1 to 6")
                else:
                    print(*[(random.randint(1, 6), random.randint(1, 6))
                            for num in range(int(user_input))])
                
                    count += 1

            elif user_input.lower() == 'n' and count == 0:
                print("Please did not play the game")
                break

            elif user_input.lower() == 'n' and count >= 1:
                break

            else:
                print("Enter a valid input y or n")
                

        except ValueError as e:
            print("Please enter a number")

    if count != 0:
        print(f"You rolled {count} times")
    


dice_game()
