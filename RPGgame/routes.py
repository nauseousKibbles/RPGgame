from RPGgame import app
from flask import render_template, url_for
from RPGgame.forms import HuntButtomForm


@app.route("/")
def home():
    return render_template("home.html")