import jwt
from datetime import datetime, timedelta
from typing import Tuple, Optional
from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity
from ..model.user import User
from ..service.user import UserService
from ..utils.bcrypt import check_password

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
            'iss': 'QuarkCloud',
            'sub': 'UserToken'
        }
        return create_access_token(identity=user.username, additional_claims=user_claims, expires_delta=timedelta(seconds=expire_second))

    def login(self, username: str, password: str, guard_name: str) -> str:
        user_service = UserService()
        user = user_service.get_info_by_username(username)
        if not check_password(password, user.password):
            raise ValueError("the username or password is incorrect")
        token = self.make_token(user, guard_name, 24 * 60 * 60)
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        user_service.update_last_login(user.id, client_ip, datetime.now())
        return token

    def get_info(self, guard_name: str) -> User:
        user_claims = get_jwt_identity()
        if user_claims['guard_name'] != guard_name:
            raise ValueError("401 unauthorized")

        user_info = UserService().get_info_by_id(user_claims['id'])
        if user_info.status != 1:
            raise ValueError("the user has been disabled")
        return user_info

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