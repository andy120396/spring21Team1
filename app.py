from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Rock Paper Scissor simulator</h1><p>This site is a prototype API for rock paper scissor game.</p>"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

#Andy Liu
#Anzar Anwar
#Jenna Gorman
#Xinjie Lin
#Huaiyuan Fan