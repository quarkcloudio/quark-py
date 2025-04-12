#coding: utf-8
from typing import Any
from flask import Flask
from quark.dal import db
from quark.template.controller.resource import resource_bp

class Quark(Flask):
    def __init__(self, __name__):
        super().__init__(__name__)
        db.init('mysql+pymysql://root:fK7xPGJi1gJfIief@localhost:3306/quarkpy')
        self.register_blueprint(resource_bp)
    
    def run(self, host: str = '0.0.0.0', port: int = 5000, debug: bool = False, **options: Any) -> None:
        super().run(host, port, debug, **options)