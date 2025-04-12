#coding: utf-8
from quark import Quark

# 创建一个app
app = Quark(__name__)

# 创建路由
@app.route('/')
def index() -> str:
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
