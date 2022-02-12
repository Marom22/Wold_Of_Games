# Memory Game

# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose

# Methods:
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The
#                        list length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
#                         will be in the size of difficulty.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will
#                    return True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
#           lost or won.
import random

def generate_sequence(length):
    list_to_generate = []
    for i in range(0, length):
        list_to_generate.append(random.randint(1, 101))
    return list_to_generate


def get_list_from_user():
    user_input = input("Please enter your answer to the game: \n")
    user_list = []
    for i in user_input.split(","):
        user_list.append(int(i))
    return user_list

def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

def play(difficulty):
    import sys
    import time
    sequence = generate_sequence(difficulty)
    sys.stdout.write(str(sequence))
    sys.stdout.flush()
    time.sleep(0.7)
    sys.stdout.write("\r")
    sys.stdout.flush()
    user_list = get_list_from_user()
    answer = is_list_equal(sequence, user_list)
    return answer
