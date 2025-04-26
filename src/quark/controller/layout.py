from flask import Blueprint
from ..core import class_loader

# 创建蓝图
layout_bp = Blueprint('layout', __name__)

# layout组件渲染
@layout_bp.route('/api/admin/layout/<resource>/index', methods=['GET'])
def index(resource):
    return class_loader.load_resource_object('Layout').render()
