from RPGgame import db, login_manager
from flask_login import UserMixin




inv = {"Health Potions":1,"Lols":5,"Scss":5,"gfsd":2}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    darkmode = db.Column(db.Boolean, default=False)

    attack = db.Column(db.Integer, default=1)
    health = db.Column(db.Integer, default=100)
    defence = db.Column(db.Integer, default=1)
    coins = db.Column(db.Integer, default=100)

    inventory = db.Column(db.PickleType(), default = inv)
    

    def __repr__(self):
       return f"User('{self.name}', '{self.password}', '{self.id}')"





