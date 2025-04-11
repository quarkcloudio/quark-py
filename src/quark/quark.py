#coding: utf-8
from typing import Any
from flask import Flask
from quark.template.controller.resource import resource_bp

class Quark(Flask):
    def __init__(self, __name__):
        super().__init__(__name__)
        self.register_blueprint(resource_bp)