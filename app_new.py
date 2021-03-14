# 1. import Flask
from flask import Flask, render_template, redirect, url_for
import random
from random import choice
import time
import practice, practice_new

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    question1 = practice_new.scrape()
    templateData = render_template('index.html')
    redirect_url = '/question2'
    return render_template('index.html', question1 = question1, redirect_url = redirect_url)


# 4. Define what to do when a user hits the /about route
@app.route("/question2")
def questions():
    desired = practice_new.scrape2()
    return desired
  

if __name__ == "__main__":
    app.run(debug=True)
