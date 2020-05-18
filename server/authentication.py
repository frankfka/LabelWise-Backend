from functools import wraps

from flask import request
from flask_restful import abort

from config import AppConfig

API_KEY_ARG = "key"


# TODO: Use something more advanced: https://flask-httpauth.readthedocs.io/en/latest/
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        if request.args.get(API_KEY_ARG) and request.args.get(API_KEY_ARG) == AppConfig().api_key:
            return func(*args, **kwargs)
        abort(401)
    return wrapper