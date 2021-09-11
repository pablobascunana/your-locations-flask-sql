import os
import pytest

from dotenv import load_dotenv


load_dotenv()

from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from models.user import User as UserModel
from schemas.user import UserSchema
from utils.commons import generate_hash_password, generate_uuid_4

MOCKED_DB_NAME = 'test'
user_schema = UserSchema()


@pytest.fixture
def load_user():
    return user_schema.load({
        "userName": "test",
        "name": "Pepe",
        "lastName": "Perez Lopez",
        "email": "uncorreo@email.com",
        "password": "1234"
    }, partial=True)


def test_insert_user(load_user):
    load_user.password = generate_hash_password(load_user.password)
    load_user.uuid = generate_uuid_4()
    session = UnifiedAlchemyMagicMock()
    session.add(load_user)
    user = session.query(UserModel).all()
    assert type(user[0].uuid) == str
    assert len(user[0].uuid) == 36
    assert user[0].userName == load_user.userName
    assert user[0].name == load_user.name
    assert user[0].lastName == load_user.lastName
    assert user[0].email == load_user.email
    assert type(user[0].password) == str
    dumped_user = user_schema.dump(load_user)
    assert len(dumped_user) == 1
    assert dumped_user['userName'] == load_user.userName
