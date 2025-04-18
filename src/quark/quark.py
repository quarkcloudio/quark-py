#coding: utf-8
from typing import Any
import os
from flask import Flask, send_from_directory
from .dal import db
from .template import module
from .controller import login, resource
from .config import config
import i18n

class Quark(Flask):

    # 初始化
    def __init__(self, __name__):
        super().__init__(__name__)

        # 获取当前文件的绝对路径
        self.current_dir_path = os.path.dirname(os.path.abspath(__file__))

        # 模块加载路径
        self.config["MODULE_PATH"] = 'app/'

        # 设置语言
        self.config["LOCALE"] = 'zh-hans'

        # 设置静态文件路径
        self.config["STATIC_PATH"] = 'web/app/'

    # 初始化数据库
    def init_db(self) -> None:
        db.init(self.config["DB_URI"])

    # 初始化 locale
    def init_locale(self) -> None:
        locales_path = os.path.abspath(os.path.join(self.current_dir_path, 'locales'))

        # 设置 locale 路径
        i18n.load_path.append(locales_path)

        # 设置默认语言
        i18n.set('locale', self.config["LOCALE"])

    # 初始化配置
    def init_config(self) -> None:
        config.update(self.config)

    # 静态资源和首页
    def serve_static(self, path):
        # 获取静态资源路径
        static_path = os.path.join(self.current_dir_path, self.config["STATIC_PATH"])

        # 判断是否存在index.html
        full_path = os.path.join(static_path, path)
        index_path = os.path.join(full_path, "index.html")
        if os.path.isfile(index_path):
            return send_from_directory(full_path, "index.html")
        else:
            return send_from_directory(self.config["STATIC_PATH"], path)

    # 初始化静态资源
    def init_serve_static(self):
        self.add_url_rule('/<path:path>', view_func=self.serve_static, methods=['GET'])

    # 初始化模块
    def init_module(self) -> None:
        module.install()

    # 解析蓝图
    def parse_blueprint(self) -> None:
        self.register_blueprint(login.login_bp)
        self.register_blueprint(resource.resource_bp)

    # 加载应用
    def bootstrap(self) -> None:

        # 初始化数据库
        self.init_db()

        # 初始化 locale
        self.init_locale()

        # 初始化配置
        self.init_config()

        # 初始化模块
        self.init_module()

        # 初始化静态资源
        self.init_serve_static()

        # 解析蓝图
        self.parse_blueprint()
    
    # 启动服务
    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: Any) -> None:
        
        # 加载应用
        self.bootstrap()

        # 启动服务
        super().run(host, port, debug, load_dotenv, **options)