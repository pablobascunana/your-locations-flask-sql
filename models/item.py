from config.sql_alchemy import db
from typing import Dict, List


class ItemModel(db.Model):
    __tablename__ = "items"

    uuid = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    imageURL = db.Column(db.String(512))
    description = db.Column(db.Text)

    storeUuid = db.Column(db.String(128), db.ForeignKey("stores.uuid"), nullable=False)
    store = db.relationship("StoreModel")

    @classmethod
    def insert(cls, item: "ItemModel"):
        db.session.add(item)
        db.session.commit()

    @classmethod
    def get_items(cls, store_uuid: str) -> List["ItemModel"]:
        return cls.query.filter_by(storeUuid=store_uuid).all()

    @classmethod
    def get_item_by_uuid_and_update_it(cls, item: Dict):
        cls.query.filter_by(uuid=item["uuid"]).with_for_update().update(item)
        db.session.commit()

    @classmethod
    def delete(cls, item_uuid: str):
        deleted = cls.query.filter_by(uuid=item_uuid).delete()
        if deleted == 1:
            db.session.commit()

    @classmethod
    def delete_all_items(cls, store_uuid: str):
        deleted = cls.query.filter_by(storeUuid=store_uuid).delete()
        if deleted > 0:
            db.session.commit()
