from flask import render_template, url_for, redirect, request, flash
from RPGgame import app, db, bcrypt
from RPGgame.forms import SignupForm, LoginForm
from RPGgame.models import User
import RPGgame.game.list
from flask_login import login_user, current_user, logout_user, login_required

import random


# VIDEO GAME TIME YEAH BOIII

@app.route("/hunt")
def hunt():
    if not current_user.is_authenticated:
        flash("Please login before trying to play the game.")
        return redirect(url_for('home'))
    # Random Monster
    monster = random.choice(RPGgame.game.list.monsters)
    # Actual database changing
    healthchange = random.randint(0,10)
    coinsgained = random.randint(0,10)
    current_user.health += healthchange
    current_user.coins += coinsgained
    db.session.commit()

    return render_template("game/hunt.html", healthchange=healthchange, coinsgained=coinsgained, monster=monster)


@app.route("/fish")
def fish():
    if not current_user.is_authenticated:
        flash("Please login before trying to play the game.")
        return redirect(url_for('home'))
    
    fish_ammount = random.choice(RPGgame.game.list.fish_ammount_weight)
    fish_level = random.choice(RPGgame.game.list.fish_weighted_level)
    fish_type = random.choice(RPGgame.game.list.fish)

    # INVENTROY ADDITIONS
    if fish_level == 1:
        current_user.level_1_fish += fish_ammount
    if fish_level == 2:
        current_user.level_2_fish += fish_ammount
    if fish_level == 3:
        current_user.level_3_fish += fish_ammount
    db.session.commit()
    return render_template("game/fish.html", fish_ammount=fish_ammount, fish_type=fish_type, fish_level=fish_level)

@app.route("/shop")
def shop():
    if not current_user.is_authenticated:
        flash("Please login before trying to play the game.")
        return redirect(url_for('home'))

    return render_template("game/shop.html", disabled="")


# ADMIN STUFF LOLLOOLLOL----------------------------------------------------------------------------
@app.route("/change/<type>/<int:id>/<ammount>")
def change(type, id, ammount):
    change_user = User.query.get_or_404(id)
    if type == "coins":
        change_user.coins = int(ammount)
    if type == "health":
        change_user.health = int(ammount)
    if type == "defence":
        change_user.defence = int(ammount)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/changeinv/<item>/<int:id>/<ammount>")
def changeinv(item, id, ammount):
    change_user = User.query.get_or_404(id)

    if item == "healthpotions":
        change_user.inventory['Health Potions'] = int(ammount)
        

    db.session.commit()
    return redirect(url_for('showlist'))


# ------------------------------------------------------------------------------------------------------
# ONLY BORING STUFF BEYOND THIS POINT WARNING!!!!!! WARNING!!!!! -------------------------------------
@app.route("/")
@app.route('/home')
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            pass #You can flash here
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/list")
def showlist():
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/create")
def create():
    db.create_all()
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/destroy")
def destroy():
    db.drop_all()
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/darkmode")
def darkmode():
    if current_user.darkmode:
        current_user.darkmode = False
        db.session.commit()
        return redirect(url_for('home'))
    if not current_user.darkmode:
        current_user.darkmode = True
        db.session.commit()
        return redirect(url_for('home'))
