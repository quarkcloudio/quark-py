from flask import Blueprint, request, jsonify

# 创建蓝图
resource_bp = Blueprint('resource', __name__)

# 定义路由
@resource_bp.route('/api/admin/<resource>/index', methods=['GET'])
def index(resource):
    return resource+" index"