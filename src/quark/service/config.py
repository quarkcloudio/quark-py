from ..dal import db
from ..model.config import Config
import threading

# 假设的ConfigService类
class ConfigService:
    def __init__(self):
        self.web_config = {}
        self.mu = threading.Lock()

    def refresh(self):
        configs = Config.query.filter_by(status=1).all()
        with self.mu:
            self.web_config = {config.name: config.value for config in configs}

    def set_value(self, key, value):
        config = Config.query.filter_by(name=key).first()
        if config:
            config.value = value
        else:
            config = Config(name=key, value=value, status=1)
            db.session.add(config)
        db.session.commit()
        self.refresh()

    def get_value(self, key):
        if not self.web_config:
            self.refresh()
        return self.web_config.get(key, "")