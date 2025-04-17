from flask import Blueprint, request, jsonify

# 创建蓝图
login_bp = Blueprint('login', __name__)

# 定义路由
@login_bp.route('/api/admin/login/<resource>/index', methods=['GET'])
def index(resource):
    return resource+" index"