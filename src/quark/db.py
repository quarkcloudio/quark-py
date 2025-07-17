from typing import Iterable, Any
from tortoise import Tortoise


async def init(
    config: dict | None = None,
    config_file: str | None = None,
    db_url: str | None = None,
    modules: dict[str, Iterable[Any]] | None = None,
) -> None:
    """初始化数据库配置"""
    await Tortoise.init(
        config=config,
        config_file=config_file,
        db_url=db_url,
        modules=modules,
    )
    await Tortoise.generate_schemas()
