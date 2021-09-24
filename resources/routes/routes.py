from resources.status import IsAlive, Version
from resources.store import Store
from resources.item import Item
from resources.user import Login, User

API_PATH = '/api/v1'


def create_resources(api):
    api.add_resource(IsAlive, "/isalive")
    api.add_resource(Login, API_PATH + "/login")
    api.add_resource(Store, API_PATH + "/store/<string:user_uuid>")
    api.add_resource(Item, API_PATH + "/item/<string:store_uuid>")
    api.add_resource(User, API_PATH + "/user")
    api.add_resource(Version, "/version")
