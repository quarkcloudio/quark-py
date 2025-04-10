#coding: utf-8
from flask import Flask
from api.detect import detect_bp
from api.ocr import ocr_bp

# 创建一个app
app = Flask(__name__)

# 设置debug模式
app.config["DEBUG"] = True

# 注册蓝图
app.register_blueprint(detect_bp)
app.register_blueprint(ocr_bp)

# 创建路由
@app.route('/')
def index() -> str:
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)