from flask import Blueprint
from ..core import class_loader

# 创建蓝图
dashboard_bp = Blueprint('dashboard', __name__)

# dashboard页面渲染
@dashboard_bp.route('/api/admin/dashboard/<resource>/index', methods=['GET'])
def index(resource):
    return class_loader.load_resource_object('Dashboard').render()
