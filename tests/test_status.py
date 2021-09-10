import os
import pytest

from dotenv import load_dotenv

load_dotenv('../.env.testing')

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.routes.routes import create_resources
from resources.status import check_database_is_alive


@pytest.fixture(scope='session')
def client():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
    with app.test_client() as client:
        api = Api(app)
        create_resources(api)
        db = SQLAlchemy()
        db.init_app(app)
        yield client


def test_version(client):
    response = client.get('/version')
    assert b'##VersionNumber##' in response.data


def test_is_alive():
    status = check_database_is_alive()
    assert status
