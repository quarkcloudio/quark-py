#coding: utf-8
from typing import Any
from flask import Flask
from template.controller.resource import resource_bp

class Engine(Flask):
    def __init__(self, __name__):
        super().__init__(__name__)