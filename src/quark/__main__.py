# coding: utf-8
from quark import Quark, Response

# 创建对象
app = Quark()

# 配置数据库
app.config["DB_URL"] = "mysql://root:fK7xPGJi1gJfIief@localhost:3306/quarkcloud"


# 创建路由
@app.get("/")
def index():
    return Response(content="Hello World!", media_type="text/html")


if __name__ == "__main__":

    # 启动应用
    app.run("quark.__main__:app", host="0.0.0.0", port=8080, reload=True)
