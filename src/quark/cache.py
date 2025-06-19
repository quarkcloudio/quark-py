from typing import Any
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend


def init(prefix: str) -> None:
    """初始化缓存"""
    FastAPICache.init(InMemoryBackend(), prefix=prefix)


async def set(key: str, value: Any, expire: int | None = None) -> None:
    await FastAPICache.get_backend().set(key, value, expire)


async def get(key: str) -> Any:
    return await FastAPICache.get_backend().get(key)
