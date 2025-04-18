from flask import Blueprint
from ..core import class_loader

# 创建蓝图
login_bp = Blueprint('login', __name__)

# 登录页面渲染
@login_bp.route('/api/admin/login/<resource>/index', methods=['GET'])
def index(resource):
    return class_loader.load_resource_object('Login').index_render()