from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "microservice is running"

if __name__ == '__main__':
    app.run(port=5001, debug=True)