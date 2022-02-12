# Guess Game

# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the
#   ● Difficulty
#   ● Secret number

# Methods:
# 1. generate_number - Will generate number between 1 to difficulty and save it
#                      to secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
#                          return the number.
# 3. compare_results - Will compare the secret generated number to the one
#                      prompted by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
#           lost or won.

import random
# from Live import choose_difficulty

# difficulty = choose_difficulty()



def generate_number(difficulty):
    secret_number = (random.randint(1,difficulty))
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        try:
            guess_number = int(input(f"Please enter a number between 1 and {difficulty}: "))
        except ValueError:
            print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")
        else:
            if guess_number in range(1, difficulty + 1):
                return guess_number
            else:
                print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")



def compare_results(number, secret_number):
    if number == secret_number:
        return True
    else:
        return False

def play(difficulty):
    secret_number = generate_number(difficulty)
    number_from_user = get_guess_from_user(difficulty)
    answer = compare_results(secret_number, number_from_user)
    return answer, secret_number

