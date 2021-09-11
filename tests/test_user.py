import os
import pytest

from dotenv import load_dotenv


load_dotenv()

from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from models.user import User as UserModel
from schemas.user import UserSchema
from usecases.user import do_user_login
from utils.commons import generate_hash_password, generate_uuid_4
from utils.constants import JWT_ALGORITHM, JWT_IDENTITY_CLAIM

'''
https://mock-alchemy.readthedocs.io/en/latest/user_guide/index.html
'''

MOCKED_DB_NAME = 'test'
user_schema = UserSchema()


@pytest.fixture
def register_user():
    return user_schema.load({
        "userName": "test",
        "name": "Pepe",
        "lastName": "Perez Lopez",
        "email": "uncorreo@email.com",
        "password": "1234"
    }, partial=True)


@pytest.fixture
def login_user():
    return user_schema.load({"userName": "test", "password": "1234"}, partial=True)


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_ALGORITHM'] = JWT_ALGORITHM
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=30)
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    app.config['JWT_IDENTITY_CLAIM'] = JWT_IDENTITY_CLAIM
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_KEY')
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    JWTManager(app)
    return app


def insert_user(user):
    user.password = generate_hash_password(user.password)
    user.uuid = generate_uuid_4()
    session = UnifiedAlchemyMagicMock()
    session.add(user)
    return session


def get_user_by_username(session, user):
    return session.query(UserModel).filter(UserModel.userName == user.userName).one()


def test_insert_user(register_user):
    session = insert_user(register_user)
    user = session.query(UserModel).all()
    assert type(user[0].uuid) == str
    assert len(user[0].uuid) == 36
    assert user[0].userName == register_user.userName
    assert user[0].name == register_user.name
    assert user[0].lastName == register_user.lastName
    assert user[0].email == register_user.email
    assert type(user[0].password) == str
    dumped_user = user_schema.dump(register_user)
    assert len(dumped_user) == 1
    assert dumped_user['userName'] == register_user.userName


def test_do_success_login(app, register_user, login_user):
    register_user.loginAttempts = 0
    session = insert_user(register_user)
    user = get_user_by_username(session, login_user)
    with app.app_context():
        response = do_user_login(login_user, user)
        assert 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9' in response[0].get("access_token")
        assert 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9' in response[0].get("refresh_token")
        assert response[1] == 200


def test_do_incorrect_login(register_user, login_user):
    login_user.password = "12344"
    session = insert_user(register_user)
    user = get_user_by_username(session, login_user)
    response = do_user_login(login_user, user)
    assert response[0].get("message") == 'Bad credentials'
    assert response[1] == 401
