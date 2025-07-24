from fastapi import APIRouter, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from .quark import Quark
from . import cache, config, utils
from .template.layout import Layout
from .template.login import Login
from .template.dashboard import Dashboard
from .template.resource import Resource
