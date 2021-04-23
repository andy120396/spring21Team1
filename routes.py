from flask import Blueprint, request, render_template
from game_utils.rock_paper_scissors import *
import os
import requests
import sys


game_routes = Blueprint("game_routes", __name__)

@game_routes.route("/")
def index():
    print("VISITING THE START PAGE")
    return render_template("index.html")

@game_routes.route("/results", methods=["GET", "POST"])
def results():
    try:
        options = ["rock", "paper", "scissors"]

        if "choice" in request.args:
            user_choice = request.args["choice"]
        elif "choice" in request.values:
            user_choice = request.values["choice"]
        else:
            user_choice = "rock"

        if user_choice not in options:
            user_choice = "rock"

        computer_choice = requests.get("http://127.0.0.1:5001/results")

        #computer_choice.text

        winning_choice = determine_winner(user_choice, computer_choice.text)

        if winning_choice:
            if winning_choice == user_choice:
               results_message = WIN_MESSAGE
            elif winning_choice == computer_choice.text:
                results_message = LOSE_MESSAGE
        else:
            results_message = TIE_MESSAGE
        return render_template("final.html",
            user_choice=user_choice,
            computer_choice=computer_choice,
            results_message=results_message
        )

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return "Something went wrong"