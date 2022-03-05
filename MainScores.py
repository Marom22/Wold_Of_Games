from flask import Flask
import os
app = Flask(__name__)

wins_file = "HTML_files/HTML_wins.html"
errors_file = "HTML_files/HTML_errors.html"


def scores_saver():
    try:
        f_res = open("Scores.txt", "r")
        score = f_res.read()
        f_res.close()
        return int(score)
    except IOError as Err:
        return repr(Err)


@app.route("/", methods=["GET"])
def index():
    res_score = scores_saver()
    try:
        content_templet = open(os.path.join(os.getcwd(), wins_file), "r")
        string = content_templet.read()
        string = string.replace("{SCORE}", str(res_score))
    except ValueError:
        content_templet = open(os.path.join(os.getcwd(), errors_file), "r")
        string = content_templet.read()
        string = string.replace("{ERROR}", str(res_score))
    return string


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=8080)