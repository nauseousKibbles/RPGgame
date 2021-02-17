from RPGgame import app, db
from flask import render_template, url_for, redirect
# from RPGgame.forms import SignUpForm, LoginForm
from RPGgame.models import Character


#BORING STUFF AND CAN ALSO BE DANGEROUS


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/list")
def list_of_characters():
    characters = Character.query.all()
    return render_template("list.html", characters=characters)




@app.route("/RESET_entire_DATABASE")
def REEEEEEE():
    
    db.drop_all()
    db.session.commit()

    db.create_all()
    db.session.commit()

    return redirect(url_for('home'))


#VIDEOGAME STUFF AND VIDEOGAME SIDE ONLY COOL STUFF BEYOND THIS POINT---------

@app.route("/hunt")
def hunt():
    pass