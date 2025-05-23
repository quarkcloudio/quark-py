# coding: utf-8
from .quark import Quark

# 创建一个app
app = Quark(__name__)

# 设置debug模式
app.config["DEBUG"] = True

# 配置数据库
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:fK7xPGJi1gJfIief@localhost:3306/quarkpy"
)

# 配置 JWT
app.config["JWT_SECRET_KEY"] = "your-secret-key"  # 替换为你的密钥


# 创建路由
@app.route("/")
def index() -> str:
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
