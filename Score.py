# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the winnings of the
# user.
# Amount of points for winning a game is as follows:
#                                                   POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
#
#
# Each time the user is winning a game, the points he one will be added to his current amount of point saved in a file.
#
#
# Methods:
#   add_score - The function’s input is a variable called difficulty. The function will try to read
#               the current score in the scores file, if it fails it will create a new one and will use it to save
#               the current score.

import Utils as uti

total_score = 0
POINTS_OF_WINNING = 0


def add_score(difficulty):
    add_points = (difficulty*3)+5
    try:
        score_file = open(uti.SCORES_FILE_NAME, 'r')
        content = score_file.read()
        if content:
            _sum = int(content) + add_points
            content = str(_sum)
            open(uti.SCORES_FILE_NAME, 'w').write(content)
    except IOError:
        score_file = open(uti.SCORES_FILE_NAME, 'w')
        score_file.write(str(add_points))
    finally:
        score_file.close()
    return True