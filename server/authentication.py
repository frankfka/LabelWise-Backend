from functools import wraps

from flask import request
from flask_restful import abort

from config import AppConfig

API_KEY_ARG = "X-API-Key"


# TODO: Use something more advanced: https://flask-httpauth.readthedocs.io/en/latest/
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers.get(API_KEY_ARG) and request.headers.get(API_KEY_ARG) == AppConfig().api_key:
            return func(*args, **kwargs)
        abort(401)
    return wrapper