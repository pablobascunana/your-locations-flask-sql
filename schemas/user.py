from config.marshmallow import marshmallow as ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("name", "lastName", "email", "password", "registerDate", "loginAttempts")
