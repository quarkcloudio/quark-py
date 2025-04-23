from flask import Blueprint
from ..core import class_loader

# 创建蓝图
login_bp = Blueprint('login', __name__)

# 登录页面渲染
@login_bp.route('/api/admin/login/<resource>/index', methods=['GET'])
def index(resource):
    return class_loader.load_resource_object('Login').render()

# 获取验证码id
@login_bp.route('/api/admin/login/<resource>/captchaId', methods=['GET'])
def captcha_id(resource):
    return class_loader.load_resource_object('Login').captcha_id()

# 获取验证码
@login_bp.route('/api/admin/login/<resource>/captcha/<id>', methods=['GET'])
def captcha(resource, id):
    return class_loader.load_resource_object('Login').captcha(id)