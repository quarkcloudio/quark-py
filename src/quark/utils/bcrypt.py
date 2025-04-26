from bcrypt import hashpw, gensalt, checkpw

def encrypt_password(password: str) -> str:
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    return checkpw(password.encode('utf-8'), hashed.encode('utf-8'))