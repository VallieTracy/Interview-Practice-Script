# 1. import Flask
from flask import Flask, render_template
import random
from random import choice
import time
import practice

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('index.html')


# 4. Define what to do when a user hits the /about route
@app.route("/questions")
def scrape():
    desired = practice.scrape()
    return desired

@app.route("/practicepy")
def test():
    interview_questions = ['A', 'B', 'C', 'D']
    return interview_questions[2]


if __name__ == "__main__":
    app.run(debug=True)
