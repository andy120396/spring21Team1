import os
from flask import Flask, render_template, Blueprint, request
from dotenv import load_dotenv
from routes import game_routes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def create_app():
    load_dotenv()
    app_enviro = os.environ.get("FLASK.ENV", "development")
    secret_key = os.environ.get("SECRET_KEY", "my super secret")
    testing = False
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(ENV=app_enviro, SECRET_KEY=secret_key, TESTING=testing)
    app.register_blueprint(game_routes)
    return app

if __name__ == '__main__':
    rps_app = create_app()
    rps_app.run()

#Edited by Xinjie Lin 4/7/2021 6:38 PM
#@app.route('/')
#def index():
#    random_number = random.randint(1,1000)
#    return render_template('index.html',random_number = random_number)
#End of Edit

#Andy Liu
#Anzar Anwar
#Jenna Gorman
#Xinjie Lin
#Huaiyuan Fan