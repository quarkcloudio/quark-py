## 介绍
QuarkPy是一个基于FastAPI + Ant Design Pro 前后端分离的管理后台

## 快速开始

1. 创建 demo 文件夹，进入该目录中执行如下命令，初始化项目：
``` bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate
```
2. 创建 main.py 文件
3. 在 main.py 文件中添加如下代码：
```python
from quark import Quark, Response

# 创建对象
app = Quark()

# 配置数据库
app.config["DB_URL"] = "sqlite://data.db"

# 配置应用密钥
app.config["APP_SECRET_KEY"] = "abcdefghijklmnopqrstuvwxyz"

# 创建路由
@app.get("/")
def index():
    return Response(content="Hello World!", media_type="text/html")


if __name__ == "__main__":

    # 启动应用
    app.run("main:app", host="0.0.0.0", port=3000, reload=True)

```
4. 拉取依赖
``` bash
pip install quark-py
```
5. 启动服务
``` bash
python main.py
```

后台地址： ```http://127.0.0.1:3000/admin/```

账号：```administrator```
密码：```123456```

## 特别注意
1. **后台用户认证使用了APP_SECRET_KEY作为JWT的加密密串，生产环境请务必更改**

## 技术支持
为了避免打扰作者日常工作，你可以在Github上提交 [Issues](https://github.com/quarkcloudio/quark-py/issues)

相关教程，你可以查看 [在线文档](http://quarkcloud.io/quark-py/)

## License
QuarkPy is licensed under The MIT License (MIT).