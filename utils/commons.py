import bcrypt
import uuid


def generate_uuid_4():
    return str(uuid.uuid4())


def generate_hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
