from config.sql_alchemy import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)

    storeUuid = db.Column(db.String(128), db.ForeignKey("stores.uuid"), nullable=False)
    store = db.relationship("StoreModel")
