from RPGgame import app, db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)


    coins = db.Column(db.Integer, default=100)
    defence = db.Column(db.Integer, default=1)
    health = db.Column(db.Integer, default=1)