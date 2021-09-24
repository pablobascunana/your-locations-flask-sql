from config.marshmallow import marshmallow as ma
from models.store import StoreModel
from schemas.item import ItemSchema


class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = StoreModel
        load_instance = True
        include_fk = True
        load_only = ("userUuid", "items")
