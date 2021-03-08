# 1. import Flask
from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)
