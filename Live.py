# Live.py

def choose_game():
    print("Please choose a game to play: \n"
          "* Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
          "* Guess Game - guess a number and see if you choose like the computer \n"
          "* Currency Roulette - try and guess the value of a random amount of USD in ILS \n"
          "************************************************************************************************")
    while True:
        try:
            select_game = int(input("Select game: \n"
                                    "For Memory Game - press 1 \n"
                                    "For Guess Game - press 2 \n"
                                    "For Currency Roulette - press 3 \n"
                                    "Please press number between 1-3: "))
        except ValueError:
            print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")
        else:
            if select_game in range(1, 4):
                print(select_game)
                return select_game
            else:
                print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")


def choose_difficulty():
    while True:
        try:
            select_difficulty = int(input(
                "************************************************************************************************ \n"
                "Select Difficulty: \n"
                "Select a number between 1-5, \n"
                "1 is the easiest and 5 is the hardest \n"
                "Please press number between 1-5: "))
        except ValueError:
            print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")
        else:
            if select_difficulty in range(1, 6):
                return select_difficulty
            else:
                print("\n"
                      "********** A Wrong input was selected ********** \n"
                      "         ***** Please try again ***** \n"
                      "")


def welcome(name):
    print(f"Hello, {name} and welcome to World of Games (WoG). Here you can find many cool games to play.")


def load_game():
    game = choose_game()
    difficulty = choose_difficulty()

    if int(game) == 1:
        print("Welcome to Memory Game")
        print(f"The difficult level is: {difficulty}")
        print("")
        from MemoryGame import play
        answer_to_game = play(difficulty)
        if answer_to_game == True:
            print(f"You Won")
        else:
            print(f"You Lost")

    elif int(game) == 2:
        print("Welcome to Guess Game")
        print(f"The difficult level is: {difficulty}")
        print("")
        from GuessGame import play
        answer_from_game, secret_num = play(difficulty)
        if answer_from_game == True:
            print(f"You Won, the answer is: {secret_num}")
        else:
            print(f"You Lost, the answer is: {secret_num}")

    elif int(game) == 3:
        print("Welcome to Currency Roulette")
        print(f"The difficult level is: {difficulty}")
        from CurrencyRouletteGame import play
        answer_from_game = play(difficulty)
        if answer_from_game == True:
            print(f"You Won")
        else:
            print(f"You Lost")
