from flask import Blueprint
from ..core import login_render

# 创建蓝图
login_bp = Blueprint('login', __name__)

# 定义路由
@login_bp.route('/api/admin/login/<resource>/index', methods=['GET'])
def index(resource):
    return login_render.index_render(resource)