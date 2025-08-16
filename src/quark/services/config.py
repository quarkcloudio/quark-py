import asyncio
from typing import Dict

from ..models.config import Config


class ConfigService:
    def __init__(self):
        self.web_config: Dict[str, str] = {}
        self._lock = asyncio.Lock()

    async def refresh(self):
        configs = await Config.filter(status=1).all()
        async with self._lock:
            self.web_config = {config.name: config.value for config in configs}

    async def set_value(self, key: str, value: str):
        config = await Config.get_or_none(name=key)
        if config:
            config.value = value
            await config.save()
        else:
            await Config.create(name=key, value=value, status=1)
        await self.refresh()

    async def get_value(self, key: str) -> str:
        if not self.web_config:
            await self.refresh()
        return self.web_config.get(key, "")
