from flask_jwt_extended import create_access_token

def admin_login(username, password):

    # 添加角色到 claims 中
    claims = {"username": username}
    access_token = create_access_token(identity=username, additional_claims=claims)
    return access_token