#coding: utf-8
from typing import Any
from flask import Flask
from quark.dal import db
from quark.template import module
from quark.template.controller.resource import resource_bp

class Quark(Flask):

    # 初始化
    def __init__(self, __name__):
        super().__init__(__name__)
        self.register_blueprint(resource_bp)

    # 初始化数据库
    def init_db(self) -> None:
        db.init(self.config["DB_URI"])

    # 初始化应用
    def init_app(self) -> None:

        # 初始化数据库
        self.init_db()
        
        # 安装模版
        module.install()
    
    # 启动服务
    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: Any) -> None:
        self.init_app()
        super().run(host, port, debug, load_dotenv, **options)