import jwt
from datetime import datetime, timedelta
from typing import Tuple, Optional
from flask_jwt_extended import create_access_token
from ..model.user import User
from ..service.user import UserService

class AuthService:
    def __init__(self):
        pass

    def make_token(self, user: User, guard_name: str, expire_second: int) -> str:
        user_claims = {
            'id': user.id,
            'username': user.username,
            'nickname': user.nickname,
            'sex': user.sex,
            'email': user.email,
            'phone': user.phone,
            'avatar': user.avatar,
            'guard_name': guard_name,
            'exp': datetime.now() + timedelta(seconds=expire_second),
            'iat': datetime.now(),
            'nbf': datetime.now(),
            'iss': 'QuarkCloud',
            'sub': 'UserToken'
        }
        return create_access_token(identity=user.username, additional_claims=user_claims)

    def login(self, username: str, password: str, guard_name: str) -> Tuple[str, Optional[Exception]]:
        user_service = UserService()
        user, err = user_service.get_info_by_username(username)
        if err:
            return '', err
        if not check_password_hash(user.password, password):
            return '', ValueError("the username or password is incorrect")
        token, err = self.make_token(user, guard_name, 24 * 60 * 60)
        if err:
            return '', err
        err = user_service.update_last_login(user.id, self.ctx.client_ip(), datetime.now())
        return token, err

    def get_info(self, guard_name: str) -> Tuple[User, Optional[Exception]]:
        try:
            user_claims = jwt.decode(self.ctx.jwt_token, self.ctx.jwt_secret, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return User(), ValueError("Token expired")
        except jwt.InvalidTokenError:
            return User(), ValueError("Invalid token")

        if user_claims['guard_name'] != guard_name:
            return User(), ValueError("401 unauthorized")

        user_info, err = UserService().get_info_by_id(user_claims['id'])
        if user_info.status != 1:
            return User(), ValueError("the user has been disabled")
        return user_info, err

    def get_id(self, guard_name: str) -> Tuple[int, Optional[Exception]]:
        user, err = self.get_info(guard_name)
        return user.id, err

    def admin_login(self, username: str, password: str) -> Tuple[str, Optional[Exception]]:
        return self.login(username, password, 'admin')

    def get_admin(self) -> Tuple[User, Optional[Exception]]:
        return self.get_info('admin')

    def get_admin_id(self) -> Tuple[int, Optional[Exception]]:
        return self.get_id('admin')

    def user_login(self, username: str, password: str) -> Tuple[str, Optional[Exception]]:
        return self.login(username, password, 'user')

    def get_user(self) -> Tuple[User, Optional[Exception]]:
        return self.get_info('user')

    def get_uid(self) -> Tuple[int, Optional[Exception]]:
        return self.get_id('user')