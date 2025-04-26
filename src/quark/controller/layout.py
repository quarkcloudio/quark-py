from flask import Blueprint
from .. import loader

# 创建蓝图
layout_bp = Blueprint('layout', __name__)

# layout组件渲染
@layout_bp.route('/api/admin/layout/<resource>/index', methods=['GET'])
def index(resource):
    return loader.load_resource_object('Layout').render()
