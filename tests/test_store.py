import pytest

from dotenv import load_dotenv

load_dotenv()

from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from models.store import StoreModel
from schemas.store import StoreSchema
from utils.commons import generate_uuid_4


MOCKED_DB_NAME = 'test'
store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)


@pytest.fixture
def store():
    return store_schema.load({
        "name": "Shop 1",
        "userUuid": "6cda4e61-49ab-4170-a8da-80c8f3846280",
        "email": "youmldevelop+1@gmail.com",
        "cif": "G86202198",
        "phone": "+34666777888"
    }, partial=True)


def insert_store(store):
    store.uuid = generate_uuid_4()
    session = UnifiedAlchemyMagicMock()
    session.add(store)
    return session, store.uuid


def test_add_and_get_store(store):
    session, store_uuid = insert_store(store)
    stores = session.query(StoreModel).all()
    assert type(stores) == list
    assert type(stores[0].uuid) == str
    assert stores[0].uuid == store_uuid
    assert type(stores[0].name) == str
    assert stores[0].name == store.name
    assert type(stores[0].email) == str
    assert stores[0].email == store.email
    assert type(stores[0].cif) == str
    assert stores[0].cif == store.cif
    assert type(stores[0].phone) == str
    assert stores[0].phone == store.phone
    assert type(stores[0].userUuid) == str
    assert stores[0].userUuid == store.userUuid


def test_delete_store(store):
    session, store_uuid = insert_store(store)
    deleted = session.query(StoreModel).delete()
    assert deleted == 1
    no_deleted = session.query(StoreModel).delete()
    assert no_deleted == 0
