from flask import Blueprint
from .. import loader

# 创建蓝图
login_bp = Blueprint('login', __name__)

# 登录页面渲染
@login_bp.route('/api/admin/login/<resource>/index', methods=['GET'])
def index(resource):
    return loader.load_resource_object('Login').render()

# 获取验证码id
@login_bp.route('/api/admin/login/<resource>/captchaId', methods=['GET'])
def captcha_id(resource):
    return loader.load_resource_object('Login').captcha_id()

# 获取验证码
@login_bp.route('/api/admin/login/<resource>/captcha/<id>', methods=['GET'])
def captcha(resource, id):
    return loader.load_resource_object('Login').captcha(id)

# 登录
@login_bp.route('/api/admin/login/<resource>/handle', methods=['POST'])
def handle(resource):
    return loader.load_resource_object('Login').handle()

# 退出
@login_bp.route('/api/admin/login/<resource>/logout', methods=['POST'])
def logout(resource):
    return loader.load_resource_object('Login').logout()