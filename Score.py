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
