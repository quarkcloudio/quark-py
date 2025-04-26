from bcrypt import hashpw, gensalt

def encrypt_password(password: str) -> str:
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

def check_password(password: str, hash_value: str) -> bool:
    return hashpw(password.encode('utf-8'), hash_value.encode('utf-8')) == hash_value.encode('utf-8')