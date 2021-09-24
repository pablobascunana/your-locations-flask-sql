from config.marshmallow import marshmallow as ma
from models.item import ItemModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True
        include_fk = True
        load_only = ("storeUuid",)
