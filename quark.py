#coding: utf-8
from typing import Any
from flask import Flask
from template.controller.resource import resource_bp

class Engine:
    def __init__(self):
        self.flask = Flask(__name__)

    def register_blueprint(self, bp):
        self.flask.register_blueprint(bp)

    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: Any):
        self.flask.run(host, port, debug, load_dotenv, **options)