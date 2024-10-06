import os
import pytest

from dotenv import load_dotenv


load_dotenv()

from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema
from utils.commons import generate_uuid_4
from utils.constants import JWT_ALGORITHM, JWT_IDENTITY_CLAIM


MOCKED_DB_NAME = 'test'
item_schema = ItemSchema()


@pytest.fixture
def item():
    return item_schema.load({
        "name": "Cubo de Rubik",
        "price": "95.5",
        "imageURL": "https://picsum.photos/200/300",
        "description": "Cubo de Rubik con un diseño nuevo."
    }, partial=True)


@pytest.fixture
def item_to_edit():
    return {
        "name": "Cubo de Rubik",
        "price": "95.5",
        "imageURL": "https://picsum.photos/200/300",
        "description": "Cubo de Rubik con un diseño nuevo.",
        "uuid": ""
    }


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


def insert_item(item):
    item.uuid = generate_uuid_4()
    item.storeUuid = generate_uuid_4()
    session = UnifiedAlchemyMagicMock()
    session.add(item)
    return session, item.storeUuid


def edit_item(session, item):
    item_to_edit = session.query(ItemModel).filter(ItemModel.uuid == item['uuid']).one()
    item_to_edit.name = item_to_edit.name + ' 2'
    session.commit()
    return session, item_to_edit


def test_insert_and_get_item(item):
    session, store_uuid = insert_item(item)
    db_item = session.query(ItemModel).all()
    assert type(db_item[0].uuid) == str
    assert len(db_item[0].uuid) == 36
    assert db_item[0].name == item.name
    assert db_item[0].price == item.price
    assert db_item[0].imageURL == item.imageURL
    assert db_item[0].description == item.description
    assert db_item[0].storeUuid == store_uuid
    dumped_item = item_schema.dump(db_item[0])
    assert len(dumped_item) == 5
    assert dumped_item['name'] == item.name
    assert dumped_item['price'] == item.price
    assert dumped_item['imageURL'] == item.imageURL
    assert dumped_item['description'] == item.description
    assert dumped_item['uuid'] == item.uuid


def test_edit_item(item, item_to_edit):
    session, store_uuid = insert_item(item)
    db_item = session.query(ItemModel).all()
    item_to_edit['uuid'] = db_item[0].uuid
    session, edited_item = edit_item(session, item_to_edit)
    edited_db_item = session.query(ItemModel).all()
    assert edited_db_item[0].name == edited_item.name


def test_delete_item(item):
    session, store_uuid = insert_item(item)
    deleted = session.query(ItemModel).delete()
    assert deleted == 1
    no_deleted = session.query(ItemModel).delete()
    assert no_deleted == 0
