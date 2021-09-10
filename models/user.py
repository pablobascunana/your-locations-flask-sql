from config.sql_alchemy import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)
    userName = db.Column(db.String(45), unique=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    lastName = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    loginAttempts = db.Column(db.Integer, nullable=False, default=0)
    registerDate = db.DateTime(nullable=False, default=datetime.utcnow)
