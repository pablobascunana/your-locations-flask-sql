from config.sql_alchemy import db
from typing import List


class StoreModel(db.Model):
    __tablename__ = "stores"

    uuid = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    cif = db.Column(db.String(9), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)

    userUuid = db.Column(db.String(128), db.ForeignKey("users.uuid"), nullable=False)

    items = db.relationship("ItemModel", lazy="dynamic")

    @classmethod
    def insert(cls, store: "StoreModel"):
        db.session.add(store)
        db.session.commit()

    @classmethod
    def get_stores(cls, user_uuid: str) -> List["StoreModel"]:
        return cls.query.filter_by(userUuid=user_uuid).all()

    @classmethod
    def delete(cls, store_uuid: str):
        deleted = cls.query.filter_by(uuid=store_uuid).delete()
        if deleted == 1:
            db.session.commit()
