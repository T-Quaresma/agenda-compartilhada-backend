from functools import wraps
from flask import request, g
from services.auth import validate_access_token


def require_auth(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        access_token = request.cookies.get("access_token")

        user, status = validate_access_token(access_token)

        if status == 503:
            return {
                "Message": "Authentication service unavailable."
            }, 503

        if status != 200:
            return {
                "Message": "Unauthorized."
            }, 401

        g.user = user

        return function(*args, **kwargs)

    return wrapper