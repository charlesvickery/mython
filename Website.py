from flask import Flask
import random


app = Flask(__name__)
random.seed(0)
words = ["red","blue","green","brown"]



@app.route("/")
def hello():
    return words[random.randint(0,3)]

if __name__ == "__main__":
    app.run()
