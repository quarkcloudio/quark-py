from datetime import datetime, timedelta
from typing import Optional
from fastapi import Request, HTTPException
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist
from ..models.user import User
from ..services.user import UserService
from ..utils import verify_password
from .. import config


class AuthService:

    def __init__(self, request: Request):
        self.request = request

    def create_token(
        self, data: dict, expires_delta: Optional[timedelta] = None
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now() + (
            expires_delta or timedelta(seconds=24 * 60 * 60 * 30)
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, config.get("APP_SECRET_KEY"))

    def get_token(self) -> str:
        auth_header = self.request.headers.get("Authorization")
        if auth_header is None:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        try:
            scheme, token = auth_header.split()
            if scheme.lower() != "bearer":
                raise HTTPException(
                    status_code=401, detail="Invalid authentication scheme"
                )
        except ValueError:
            raise HTTPException(
                status_code=401, detail="Invalid authorization header format"
            )

        return token

    async def login(
        self, username: str, password: str, guard_name: str = "user"
    ) -> str:
        user = await UserService().get_info_by_username(username)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="用户名或密码错误")

        # 更新最后登录
        await UserService().update_last_login(
            user.id, self.get_real_ip(self.request), datetime.now()
        )

        # 构造 JWT payload
        claims = {
            "id": user.id,
            "username": user.username,
            "nickname": user.nickname,
            "sex": user.sex,
            "email": user.email,
            "phone": user.phone,
            "avatar": user.avatar,
            "guard_name": guard_name,
            "iss": "QuarkCloud",
            "sub": "UserToken",
        }
        return self.create_token(claims)

    # 验证并返回当前用户
    async def get_current_user(self, guard_name: str = "user") -> User:
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(self.get_token(), config.get("APP_SECRET_KEY"))
            user_id: int = payload.get("id")
            token_guard: str = payload.get("guard_name")
            if user_id is None or token_guard != guard_name:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        try:
            user = await User.get(id=user_id)
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="User not found")

        if user.status != 1:
            raise HTTPException(status_code=403, detail="User is disabled")
        return user

    def get_real_ip(self, request: Request):
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            ip = forwarded_for.split(",")[0]
        else:
            ip = request.client.host
        return ip
