from flasgger import swag_from
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from schemas.item import ItemSchema
from models.item import ItemModel
from utils.commons import generate_uuid_4
from utils.constants import SWAGGER_PATH
from utils.responses import created, no_content

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)
SWAGGER_STORE_PATH = SWAGGER_PATH + 'item/'


class Item(Resource):
    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'item-get.yml')
    def get(cls, store_uuid):
        items = ItemModel.get_items(store_uuid)
        return created(item_list_schema.dump(items))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'item-post.yml')
    def post(cls, store_uuid):
        item = item_schema.load(request.get_json(), partial=True)
        item.uuid = generate_uuid_4()
        item.storeUuid = store_uuid
        ItemModel.insert(item)
        return created(item_schema.dump(item))

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'item-put.yml')
    def put(cls, store_uuid):
        ItemModel.get_item_by_uuid_and_update_it(request.get_json())
        return no_content()

    @classmethod
    @jwt_required()
    @swag_from(SWAGGER_STORE_PATH + 'item-delete.yml')
    def delete(cls, store_uuid):
        ItemModel.delete(request.get_json()["uuid"])
        return no_content()
