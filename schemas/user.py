from config.marshmallow import marshmallow as ma
from models.user import User as UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("uuid", "name", "lastName", "email", "password", "registerDate", "loginAttempts")
