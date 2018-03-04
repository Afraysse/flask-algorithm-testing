from flask import Flask, render_template, redirect
from model import User

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    """ A simple login screen. """
    return render_template('login.html')

@app.route('/', methods=['GET'])
def homepage():
    """ A simple homepage. """
    return render_template('homepage.html')


##################################################
if __name__ == "__main__":
    app.run(debug=True)
