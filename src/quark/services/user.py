from tortoise.exceptions import DoesNotExist

from ..models.user import User
from ..services.attachment import AttachmentService
from ..services.menu import MenuService


class UserService:
    def __init__(self):
        self.attachment_service = AttachmentService()
        self.menu_service = MenuService()

    async def get_info_by_id(self, user_id: int) -> User:
        try:
            user = await User.get(id=user_id, status=1)
            return user
        except DoesNotExist:
            raise Exception("用户不存在")

    async def get_info_by_username(self, username: str) -> User:
        try:
            user = await User.get(username=username, status=1)
            if user.avatar:
                user.avatar = await self.attachment_service.get_image_url(user.avatar)
            return user
        except DoesNotExist:
            raise Exception("用户不存在")

    async def get_menu_list_by_id(self, user_id: int):
        return await self.menu_service.get_list_by_user_id(user_id)

    async def update_last_login(
        self, user_id: int, last_login_ip: str, last_login_time
    ) -> None:
        try:
            user = await User.get(id=user_id)
            user.last_login_ip = last_login_ip
            user.last_login_time = last_login_time
            await user.save()
        except DoesNotExist:
            raise Exception("用户不存在")

    async def count(self) -> int:
        return await User.all().count()
