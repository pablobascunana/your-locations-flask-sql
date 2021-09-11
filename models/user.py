from config.sql_alchemy import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"

    uuid = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)
    userName = db.Column(db.String(45), unique=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    lastName = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    loginAttempts = db.Column(db.Integer, nullable=False, default=0)
    registerDate = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    @classmethod
    def insert(cls, user: "User"):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def get_user_by_username(cls, user: "User") -> "User":
        return cls.query.filter_by(userName=user.userName).one()
