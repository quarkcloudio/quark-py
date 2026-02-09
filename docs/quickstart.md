## 快速开始

1. 创建 demo 文件夹，进入该目录中执行如下命令，初始化项目：
``` bash
# Use uv create virtual environment
uv init demo

# Activate the virtual environment
uv venv

# Add QuarkPy
uv add quark-py
```
2. 打开 main.py 文件，在 main.py 文件中添加如下代码：
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

3. 启动服务
``` bash
uv run main.py
```

后台地址： ```http://127.0.0.1:3000/admin/```

账号：```administrator```
密码：```123456```