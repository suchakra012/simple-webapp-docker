import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/where do you live')
def hello():
    return 'I live in India'

if __name__ == "__main__":
    app.run()
