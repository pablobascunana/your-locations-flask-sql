from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db_tables(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
