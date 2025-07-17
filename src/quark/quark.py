# coding: utf-8
import os
import uvicorn
import logging
import i18n
from typing import Any
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise import Tortoise
from contextlib import asynccontextmanager
from .routes import login, layout, dashboard, resource
from .install import setup_all
from . import config, cache, db


class Quark(FastAPI):

    # 配置
    config: dict[str, Any] = {
        "APP_NAME": "Quark",
        "APP_VERSION": "0.1.0",
        "APP_SECRET_KEY": "your-secret-key",
        "CACHE_PREFIX": "quark-cache",
        "MODULE_PATH": "app/",
        "LOCALE": "zh-hans",
        "DB_CONFIG": None,
        "DB_URL": None,
        "DB_MODULES": {
            "models": ["quark.models"],
        },
    }

    def __init__(self, *args, **kwargs):
        """初始化"""
        super().__init__(*args, lifespan=self.lifespan, **kwargs)

        self.logger = logging.getLogger(__name__)

        # 获取当前文件的绝对路径
        self.current_dir_path = os.path.dirname(os.path.abspath(__file__))

    def sync_config(self) -> None:
        """同步配置到全局变量"""
        config.init(self.config)

    def init_cache(self) -> None:
        """初始化缓存"""
        cache.init(self.config["CACHE_PREFIX"])

    # 初始化数据库
    async def init_db(self) -> None:
        """初始化数据库"""
        await db.init(
            config=self.config["DB_CONFIG"],
            db_url=self.config["DB_URL"],
            modules=self.config["DB_MODULES"],
        )

    def init_locale(self) -> None:
        """初始化 locale"""
        locales_path = os.path.abspath(os.path.join(self.current_dir_path, "locales"))

        # 设置 locale 路径
        i18n.load_path.append(locales_path)

        # 设置默认语言
        i18n.set("locale", self.config["LOCALE"])

    def register_routers(self) -> None:
        """注册路由"""
        self.include_router(login.router)
        self.include_router(layout.router)
        self.include_router(dashboard.router)
        self.include_router(resource.router)

    def load_static(self):
        """加载静态资源"""
        static_path = os.path.join(self.current_dir_path, "web", "app", "admin")
        self.mount(
            "/admin", StaticFiles(directory=static_path, html=True), name="admin"
        )

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        """生命周期"""

        # 应用启动时执行
        await self.startup()

        yield

        # 应用关闭时执行
        await self.shutdown()

    async def startup(self) -> Any:
        """启动服务"""

        # 同步配置到全局变量
        self.sync_config()

        # 初始化缓存
        self.init_cache()

        # 初始化 locale
        self.init_locale()

        # 设置静态资源
        self.load_static()

        # 注册路由
        self.register_routers()

        # 初始化数据库
        await self.init_db()

        # 安装应用
        await setup_all()

    async def shutdown(self) -> Any:
        """关闭服务"""
        await Tortoise.close_connections()

    def run(
        self,
        app: Any | None = None,
        host: str | None = None,
        port: int | None = None,
        reload: bool | None = None,
    ) -> None:
        """uvicorn启动应用"""

        # 获取应用
        if app is None:
            app = self

        # 启动服务
        uvicorn.run(app=app, host=host, port=port, reload=reload)
