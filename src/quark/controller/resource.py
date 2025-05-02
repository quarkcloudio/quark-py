from flask import Blueprint
from .. import loader

# 创建蓝图
resource_bp = Blueprint('resource', __name__)

# 列表
@resource_bp.route('/api/admin/<resource>/index', methods=['GET'])
def index(resource):
    return loader.load_resource_object('Resource').index_render()

# 表格行内编辑
@resource_bp.route('/api/admin/<resource>/editable', methods=['GET'])
def editable(resource):
    return loader.load_resource_object('Resource').editable_render()

# 执行行为
@resource_bp.route('/api/admin/<resource>/action/<uriKey>', methods=['GET'])
def action_render(resource):
    return loader.load_resource_object('Resource').action_render()

# 行为表单值
@resource_bp.route('/api/admin/<resource>/action/<uriKey>/values', methods=['GET'])
def action_values_render(resource):
    return loader.load_resource_object('Resource').action_values_render()

# 创建页面
@resource_bp.route('/api/admin/<resource>/create', methods=['GET'])
def creation_render(resource):
    return loader.load_resource_object('Resource').creation_render()

# 创建方法
@resource_bp.route('/api/admin/<resource>/store', methods=['POST'])
def store_render(resource):
    return loader.load_resource_object('Resource').store_render()

# 编辑页面
@resource_bp.route('/api/admin/<resource>/edit', methods=['GET'])
def edit_render(resource):
    return loader.load_resource_object('Resource').edit_render()

# 获取编辑表单值
@resource_bp.route('/api/admin/<resource>/edit/values', methods=['GET'])
def edit_values_render(resource):
    return loader.load_resource_object('Resource').edit_values_render()

# 保存编辑值
@resource_bp.route('/api/admin/<resource>/save', methods=['POST'])
def save_render(resource):
    return loader.load_resource_object('Resource').save_render()

# 导入数据
@resource_bp.route('/api/admin/<resource>/import', methods=['POST'])
def import_render(resource):
    return loader.load_resource_object('Resource').import_render()

# 导出数据
@resource_bp.route('/api/admin/<resource>/export', methods=['GET'])
def export_render(resource):
    return loader.load_resource_object('Resource').export_render()

# 详情页
@resource_bp.route('/api/admin/<resource>/detail', methods=['GET'])
def detail_render(resource):
    return loader.load_resource_object('Resource').detail_render()

# 获取详情页值
@resource_bp.route('/api/admin/<resource>/detail/values"', methods=['GET'])
def detail_values_render(resource):
    return loader.load_resource_object('Resource').detail_values_render()

# 导入模板
@resource_bp.route('/api/admin/<resource>/import/template', methods=['GET'])
def import_template_render(resource):
    return loader.load_resource_object('Resource').import_template_render()

# 表单页
@resource_bp.route('/api/admin/<resource>/form', methods=['GET'])
def form_render(resource):
    return loader.load_resource_object('Resource').form_render()