from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, Request
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist

from quark.models.role_has_permission import RoleHasPermission
from quark.models.user_has_role import UserHasRole
from quark.services.permission import PermissionService
from quark.services.role import RoleService

from .. import config
from ..models.user import User
from ..services.user import UserService
from ..utils import verify_password


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
            user_id: int = payload.get("id") or 0
            token_guard: str = payload.get("guard_name") or ""
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

    async def get_current_admin(self) -> User:
        return await self.get_current_user("admin")

    async def check_permission(self, path: str, method: str) -> bool:
        admin_info = await self.get_current_admin()
        role_ids = await RoleService().get_role_ids_by_user_id(admin_info.id)

        if not role_ids:
            return False

        placeholders = ",".join(str(role_id) for role_id in role_ids)
        rows = await RoleHasPermission.raw(
            f"""
            SELECT p.id, p.name, p.guard_name, p.path, p.method
            FROM role_has_permissions rhp
            JOIN permissions p ON rhp.permission_id = p.id
            WHERE rhp.role_id IN ({placeholders}) AND p.guard_name = 'admin' AND p.path = '{path}' AND p.method = 'Any'
            """
        )
        if rows:
            return True

        rows = await RoleHasPermission.raw(
            f"""
            SELECT p.id, p.name, p.guard_name, p.path, p.method
            FROM role_has_permissions rhp
            JOIN permissions p ON rhp.permission_id = p.id
            WHERE rhp.role_id IN ({placeholders}) AND p.guard_name = 'admin' AND p.path = '{path}' AND p.method = '{method}'
            """
        )

        if rows:
            return True
        return False

    def get_real_ip(self, request: Request):
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            ip = forwarded_for.split(",")[0]
        else:
            ip = request.client.host if request.client else ""
        return ip
