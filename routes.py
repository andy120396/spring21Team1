from flask import Blueprint, request, render_template
from game_utils.rock_paper_scissors import *

game_routes = Blueprint("game_routes", __name__)

@game_routes.route("/")
def index():
    print("VISITING THE START PAGE")
    return render_template("index.html")

@game_routes.route("/results", methods=["GET", "POST"])
def results(choice=None):
    print("VISITING THE RESULTS PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    print("REQUEST VALUES:", dict(request.values))

    options = ["rock", "paper", "scissors"]

    if "choice" in request.args:
        user_choice = request.args["choice"]
    elif "choice" in request.values:
        user_choice = request.values["choice"]
    else:
        user_choice = "rock"

    if user_choice not in options:
        user_choice = "rock"

    computer_choice = random_choice(options)
    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            results_message = WIN_MESSAGE
        elif winning_choice == computer_choice:
            results_message = LOSE_MESSAGE
    else:
        results_message = TIE_MESSAGE

    return render_template("final.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        results_message=results_message
    )

#Edited by Xinjie Lin 4/7/2021 6:38 PM
@game_routes.route('/')
def index():
    random_number = random.randint(1,1000)
    return render_template('index.html',random_number = random_number)
#End of Edit