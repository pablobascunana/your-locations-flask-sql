from flasgger import swag_from
from flask import request
from flask_jwt_extended import jwt_required
from models.item import ItemModel
from flask_restful import Resource
from schemas.store import StoreSchema
from models.store import StoreModel
from utils.commons import generate_uuid_4
from utils.constants import SWAGGER_PATH
from utils.responses import created, no_content, ok

store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)
SWAGGER_STORE_PATH = SWAGGER_PATH + 'store/'


class Store(Resource):
    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'store-get.yml')
    def get(cls, user_uuid):
        stores = StoreModel.get_stores(user_uuid)
        return ok(store_list_schema.dump(stores))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'store-post.yml')
    def post(cls, user_uuid):
        store = store_schema.load(request.get_json(), partial=True)
        store.uuid = generate_uuid_4()
        StoreModel.insert(store)
        return created(store_schema.dump(store))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'store-delete.yml')
    def delete(cls, user_uuid):
        ItemModel.delete_all_items(request.get_json()["uuid"])
        StoreModel.delete(request.get_json()["uuid"])
        return no_content()
