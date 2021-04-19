from flask import Flask, make_response, Blueprint, request, render_template
from game_utils.rock_paper_scissors import *
import os

app = Flask(__name__)
game_routes = Blueprint("game_routes", __name__)

@app.route('/', methods=['GET'])
def hello():
    return "microservice is running"

@app.route("/results", methods=["GET", "POST"])
def results(choice=None):
    options = ["rock", "paper", "scissors"]

    computer_choice = random_choice(options)

    return computer_choice

if __name__ == '__main__':
    app.run(port=5001, debug=False)