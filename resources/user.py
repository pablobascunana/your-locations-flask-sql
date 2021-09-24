from flasgger import swag_from
from flask import request
from flask_restful import Resource
from schemas.user import UserSchema
from models.user import UserModel
from usecases.user import do_user_login
from utils.commons import generate_hash_password, generate_uuid_4
from utils.constants import SWAGGER_PATH
from utils.responses import created

user_schema = UserSchema()
SWAGGER_USER_PATH = SWAGGER_PATH + 'user/'


class User(Resource):
    @classmethod
    @swag_from(SWAGGER_USER_PATH + 'user.yml')
    def post(cls):
        user = user_schema.load(request.get_json(), partial=True)
        user.password = generate_hash_password(user.password)
        user.uuid = generate_uuid_4()
        UserModel.insert(user)
        return created(user_schema.dump(user))


class Login(Resource):
    @classmethod
    @swag_from(SWAGGER_USER_PATH + 'login.yml')
    def post(cls):
        user = user_schema.load(request.get_json(), partial=True)
        db_user = UserModel.get_user_by_username(user)
        return do_user_login(user, db_user)
