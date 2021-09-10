from resources.status import IsAlive, Version

API_PATH = '/api/v1'


def create_resources(api):
    api.add_resource(IsAlive, "/isalive")
    api.add_resource(Version, "/version")
