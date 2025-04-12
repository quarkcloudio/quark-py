#coding: utf-8
from typing import Any
from flask import Flask
from quark.dal import db
from quark.template import module
from quark.template.controller.resource import resource_bp
import i18n

class Quark(Flask):

    # 初始化
    def __init__(self, __name__):
        super().__init__(__name__)

        # 模块加载路径
        self.config["MODULE_PATH"] = '/app'

        # 模块加载路径
        self.config["LOCALE"] = 'zh'

    # 初始化数据库
    def init_db(self) -> None:
        db.init(self.config["DB_URI"])

    # 初始化 locale
    def init_locale(self) -> None:
        # 设置 locale 路径
        i18n.load_path.append('locales')

        # 设置默认语言
        i18n.set('locale', self.config["LOCALE"])

    # 解析蓝图
    def parse_blueprint(self) -> None:
        self.register_blueprint(resource_bp)

    # 加载应用
    def bootstrap(self) -> None:

        # 初始化数据库
        self.init_db()

        # 初始化 locale
        self.init_locale()

        # 安装模版
        module.install()

        # 解析蓝图
        self.parse_blueprint()
    
    # 启动服务
    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: Any) -> None:
        
        # 加载应用
        self.bootstrap()

        # 启动服务
        super().run(host, port, debug, load_dotenv, **options)