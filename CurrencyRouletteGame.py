# Currency Roulette

# This game will use the free currency API to get the current exchange rate from USD to ILS.
# Your code will do the following:
#     ● Generate a random number between 1 and 100 and multiply it by the USD to ILS rate,
#       which is the value that you’ll assign to the variable named t.
#     ● Money interval definition: values in the range of t - (5 - difficulty) and t + (5 - difficulty).
#     ● Ask a user to input his guess and check whether that value is in the range of values from
#       the previous section.

# random number * USD exchange rate = t

# Methods:
# 1. get_money_interval -Will generate an interval as follows:
#                        For a given difficulty d, and the total value of money t the interval will be:
#                        (t - (5 -d), t + (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
#                          value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
#           lost or won.

print("Welcome to Currency Roulette Game")
import random
rand_num = int(random.randint(0,101))


def get_money_interval(difficulty):
    from currency_converter import CurrencyConverter
    c = CurrencyConverter()
    t = rand_num * c.convert(1, "USD", "ILS")
    interval_min = t - (5 - difficulty)
    interval_max = t + (5 - difficulty)
    return interval_min, interval_max


def get_guess_from_user():
    while True:
        try:
            guess_number = int(input(f"Please enter a guess to the value of ILS to the number {rand_num} USD:  "))
        except ValueError:
            print("\n"
                      "         ***** Please try again ***** \n"
                      "")
        else:
            return guess_number


def play(difficulty):
    min, max = get_money_interval(difficulty)
    guess = get_guess_from_user()
    if guess > min and guess < max:
        return True
    else:
        return False



