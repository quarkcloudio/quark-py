import warnings
from typing import Any, Iterable

from tortoise import Tortoise
from tortoise.contrib.fastapi import RegisterTortoise


async def init(
    app: Any,
    config: dict | None = None,
    config_file: str | None = None,
    db_url: str | None = None,
    modules: dict[str, Iterable[Any]] | None = None,
) -> None:
    """初始化数据库配置"""
    # 忽略表已存在的警告
    warnings.filterwarnings(
        "ignore", category=Warning, message=".*Table.*already exists.*"
    )
    await RegisterTortoise(
        app=app,
        config=config,
        config_file=config_file,
        db_url=db_url,
        modules=modules,
        generate_schemas=True,
        use_tz=False,
    )
