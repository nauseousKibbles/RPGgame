from flask import render_template, url_for, redirect, request
from basicflasksetup import app, db
from basicflasksetup.forms import SignupForm, LoginForm
from basicflasksetup.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.password.data)
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
        if user and user.password == form.password.data:
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
