from ..db import db
from ..model.user import User
from .attachment import AttachmentService
from .menu import MenuService

# UserService类
class UserService:
    def __init__(self):
        self.attachment_service = AttachmentService()
        self.menu_service = MenuService()

    def get_info_by_id(self, user_id):
        user = User.query.filter_by(status=1, id=user_id).first()
        if not user:
            raise Exception("用户不存在")
        return user

    def get_info_by_username(self, username):
        user = User.query.filter_by(status=1, username=username).first()
        if not user:
            raise Exception("用户不存在")
        if user.avatar:
            user.avatar = self.attachment_service.get_image_url(user.avatar)
        return user

    def get_menu_list_by_id(self, user_id):
        return self.menu_service.get_list_by_user_id(user_id)

    def update_last_login(self, user_id, last_login_ip, last_login_time):
        user = User.query.get(user_id)
        if not user:
            raise Exception("用户不存在")
        user.last_login_ip = last_login_ip
        user.last_login_time = last_login_time
        db.session.commit()
        return None
    
    def count(self):
        return User.query.count()