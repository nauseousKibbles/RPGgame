from RPGgame import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    health = db.Column(db.Integer, default=100)
    defence = db.Column(db.Integer, default=1)

    def __repr__(self):
       return f"User('{self.name}', '{self.password}', '{self.id}')"





