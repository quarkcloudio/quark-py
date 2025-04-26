from flask import Blueprint
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt, jwt_required
)
from .quark import Quark
from .config import config
from .cache import cache
from .db import db