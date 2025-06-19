from typing import Any

# 全局配置变量
config: dict[str, Any] = {}


def init(getConfig: dict[str, Any]) -> None:
    """初始化全局配置"""
    global config
    config = getConfig


def set(key: str, value: Any) -> None:
    config[key] = value


def get(key: str, default: Any = None) -> Any:
    return config.get(key, default)
