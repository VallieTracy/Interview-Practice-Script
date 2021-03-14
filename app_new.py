# 1. import Flask
from flask import Flask, render_template, redirect, url_for
import random
from random import choice
import time
import practice

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    question1 = practice.scrape()
    templateData = render_template('index.html')
    redirect_url = '/testing_page'
    return render_template('index.html', question1 = question1, redirect_url = redirect_url)


# 4. Define what to do when a user hits the /about route
@app.route("/questions")
def questions():
    desired = practice.scrape()
    return desired

@app.route("/testing_page")
def testing_page():
    question1 = practice.scrape()
    question2 = practice.scrape2()
    something3 = practice.scrape3()
    return render_template("questions.html", text=question1, text2=question2, text3=something3)

@app.route("/time_delay")
def time_delay():
    templateData = render_template('delay.html')
    redirect_url = '/'
    return render_template('delay.html', redirect_url=redirect_url)
    
    

if __name__ == "__main__":
    app.run(debug=True)
