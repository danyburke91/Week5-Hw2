from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    day_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def updateProfile(self):
        db.session.commit()

    def catch(self, pokemon):
        db.session.commit()

#catch
class catch_Pokemon(db.Model):
    poke_id = db.Column(db.Integer, primary_key=True) 
    pokemon = db.Column(db.String(50), nullable=False, unique=True)
    ability = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.Integer, nullable = False)
    attack = db.Column(db.Integer, nullable = False)
    defense = db.Column(db.Integer, nullable = False)
    baseXP = db.Column(db.Integer, nullable = False)
    sprite = db.Column(db.String(200), nullable=False)
    
    #inside of the () you will make it a foregin key

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()