from RPGgame import app, db
from flask import render_template, url_for, redirect
from RPGgame.forms import SignUpForm
from RPGgame.models import Character

#BORING STUFF AND CAN ALSO BE DANGEROUS
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/list")
def list_of_characters():
    characters = Character.query.all()
    return render_template("list.html", characters=characters)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_character = Character(name=form.name.data, password=form.password.data)
        db.session.add(new_character)
        
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("signup.html", form=form)


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