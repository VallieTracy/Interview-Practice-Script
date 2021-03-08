# 1. import Flask
from flask import Flask, render_template
import random
from random import choice
import time

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('index.html')


# 4. Define what to do when a user hits the /about route
@app.route("/questions")
def about():
    print("Server received request for 'Questions' page...")
    return "List of Questions:"

@app.route("/test")
def test():
    interview_questions = ['A', 'B', 'C', 'D']
    return interview_questions[0]


if __name__ == "__main__":
    app.run(debug=True)
